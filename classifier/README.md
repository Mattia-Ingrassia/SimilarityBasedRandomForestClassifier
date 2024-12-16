# SimilarityBasedRandomForestClassifier

This model is a custom version of RandomForestClassifier that uses a similarity-based approach for sampling data.

Instead of taking random samples of data, this approach tries to improve the robustness and diversity inside the forest by selecting the samples with a similarity-based approach.

Each decision tree is trained on a weighted dataset derived from a seed instance, which are chosen by selecting data points which are the farthest possible from previously selected seeds.

## Table of Contents




## Code overview

Here is a brief overview of the main and internal methods, which will be explained later.

``` python

def fit(self, X, y): 
    # Implementation of the training method
 
def predict_proba(self, X): 
    # Implementation of the probability prediction method
    
def predict(self, X):  
    # Implementation of the class prediction method
 
def _select_seed(self, X): 
    # Implementation of the seed selection method
         
def _create_dataset(self, X, seed_instances): 
    # Implementation of the dataset creation method

def _train_single_tree(self, i, X, y):
    # Implementation for training a single decision tree

```

### Constructor (__init__)

``` python

class SimilarityBasedRandomForestClassifier: 
    
    def __init__(self, n_estimators=10, max_depth=None, random_state=None, distance_metric="euclidean", n_jobs=None): 
        
        # Initialize the parameters
        self.n_estimators = n_estimators  # Number of trees in the forest
        self.max_depth = max_depth  # Maximum depth of each decision tree
        self.random_state = random_state  # Seed for reproducibility
        self.distance_metric = distance_metric  # Distance metric for computing similarity
        self.n_jobs = n_jobs  # Number of parallel jobs for tree training

        self.classifiers = []  # List to store trained decision trees
        self.dataset_seed = None  # Array to store seed instances for each tree
        self.n_classes = None  # Number of classes in the target variable

```

The ```__init__``` method is the constructor of the class and initializes the following parameters:

- ```n_estimators```: Number of decision trees to create.
- ```max_depth```: The maximum depth of the decision trees.
- ```random_state```: Controls the randomness for reproducibility of results.
- ```distance_metric```: The distance metric used for computing similarity.
- ```n_jobs```: Number of parallel jobs for tree training.
- ```classifiers```: An empty list that will contain the trained decision trees.
- ```dataset_seed```: An array that will store the seed instances for each tree.
- ```n_classes```: The number of classes in the target variable.


## fit method

The fit method trains the algorithm on the training data given.

``` python

def fit(self, X, y):

        self.classifiers = []
        self.dataset_seed = np.zeros((self.n_estimators, X.shape[1])) 
        self.n_classes = len(np.unique(y)) 
         
        results = Parallel(n_jobs=self.n_jobs)(
            delayed(self._train_single_tree)(i, X, y) for i in range(self.n_estimators)
        )

        for seed, tree in results:
            self.dataset_seed[len(self.classifiers)] = seed
            self.classifiers.append(tree)

        return self

```

1. Initialize the ```classifiers``` and the ```dataset_seed``` lists;
2. Sets the ```n_classes``` attribute to the number of different classes in ```y```;
3. For each estimator (which the number is determined by ```n_estimators```), creates a thread (if ```n_jobs``` was specified in the ```__init__```) and trains a tree (the code is visible [there](#_train_single_tree-method)), saving each estimator and its seed in the ```results``` list;
4. For each estimator (tree) in ```results```, save the seed in the corresponding position in ```dataset_seed``` and appends the trained classifier to the ```classifiers``` list;
5. Returns ```self```.

## predict_proba method

This method computes probabilities for the input data using the trained forest.

```python
    
    def predict_proba(self, X):

        all_distances = pairwise_distances(X, self.dataset_seed, metric=self.distance_metric)
        all_similarities = 1 / (1 + all_distances)
        all_weights = all_similarities / np.sum(all_similarities, axis=1, keepdims=True)
        all_probas = np.zeros((X.shape[0], self.n_classes))

        for i, tree in enumerate(self.classifiers):
            tree_probas = tree.predict_proba(X)
            if tree_probas.shape[1] < self.n_classes:
                tree_probas = np.pad(tree_probas, ((0, 0), (0, self.n_classes - tree_probas.shape[1])))
            all_probas += all_weights[:, i][:, np.newaxis] * tree_probas
            
        return all_probas

```

1. It calculates the distances of X from the seed instances;
2. The similarities are calculated using those distances;
3. The similarities are normalized into weights;
4. ```all_probas``` is initialized to store combined probabilities;
5. For each tree in the forest, it predicts the probability of the current tree:
   - If the tree doesn't see all the classes, those probabilities are padded with 0;
   - The weighted probabilities are added to all_probas;
6. It returns ```all_probas```.

## predict method

This method predicts the class label for the input data.

```python
    
    def predict(self, X): 
        proba = self.predict_proba(X) 
        return np.argmax(proba, axis=1) 

```

1. It gets ```proba``` from the ```predict_proba``` method and returns the class with the highest probability.


## _select_seed method

This method selects a seed instance for the creation of a new tree.

```python

    def _select_seed(self, X): 
        if len(self.classifiers) == 0: 
            rng = np.random.default_rng(self.random_state)
            seed_index = rng.integers(0, len(X))
            return seed_index 
        else: 
            distances = pairwise_distances(X, self.dataset_seed[:len(self.classifiers)], metric=self.distance_metric)
            average_distances = np.mean(distances, axis=1)
            seed_index = np.argmax(average_distances)
            return seed_index 

```

1. If it is the first tree, the seed is randomly selected and returned;
2. If it is not the first tree, it calculates the average distances from previously selected seeds, selecting the farthest instance from the existing ones and returns the seed of it.


## _create_dataset method

This method creates a weighted dataset based on the seed instance.


```python

    def _create_dataset(self, X, seed_instances): 
        distances = pairwise_distances(X, [seed_instances], metric=self.distance_metric)
        similarities = 1 / (1 + distances)
        weights = similarities / np.sum(similarities)  

        rng = np.random.default_rng(self.random_state)
        selected_indexes = rng.choice(len(X), size=len(X), replace=True, p=weights.flatten())
        return selected_indexes

```

1. It computes the distances to the seed and convert them to similarities;
2. It normalizes the similarities to create the weights;
3. It samples the instances based on the calculated weights;
4. It returns the indexes of the sampled data.

## _train_single_tree method

This method trains a single decision tree classifier.

```python


    def _train_single_tree(self, i, X, y):

    seed_index = self._select_seed(X)
    seed_instance = X[seed_index]

    dataset_indexes = self._create_dataset(X, seed_instance)
    dataset_X, dataset_y = X[dataset_indexes], y[dataset_indexes]

    tree = DecisionTreeClassifier(max_depth=self.max_depth, random_state=self.random_state, ccp_alpha=0.00)
    tree.fit(dataset_X, dataset_y)

    return seed_instance, tree

```

1. It selects the seed instance for the current tree and its features;
2. It creates a weighted dataset based on the seed and extracts the sampled dataset into two variables;
3. It initializes and trains a decision tree using those two variables containing the features and the target of the weighted dataset;
4. It returns the seed instance and the trained tree.