from joblib import Parallel, delayed
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import pairwise_distances

class SimilarityBasedRandomForestClassifier:
    def __init__(self, n_estimators=10, max_depth=None, random_state=None, distance_metric="euclidean", n_jobs=None):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.random_state = random_state
        self.distance_metric = distance_metric
        self.n_jobs = n_jobs

        self.classifiers = []
        self.dataset_seed = None
        self.n_classes = None


    def fit(self, X, y):
        self.classifiers = []
        self.dataset_seed = []
        self.n_classes = len(np.unique(y))

        results = Parallel(n_jobs=self.n_jobs)(
            delayed(self._train_single_tree)(i, X, y) for i in range(self.n_estimators)
        )

        for seed, tree in results:
            self.dataset_seed.append(seed)
            self.classifiers.append(tree)

        self.dataset_seed = np.array(self.dataset_seed)

        return self


    def predict_proba(self, X):
        all_distances = pairwise_distances(X, self.dataset_seed, metric=self.distance_metric)
        all_similarities = 1 / (1 + all_distances)
        all_sum = np.sum(all_similarities, axis=1, keepdims=True)
        all_weights = all_similarities / all_sum
        all_probas = np.zeros((X.shape[0], self.n_classes))

        for i, tree in enumerate(self.classifiers):
            tree_probas = tree.predict_proba(X)
            if tree_probas.shape[1] < self.n_classes:
                padding = self.n_classes - tree_probas.shape[1]
                tree_probas = np.pad(tree_probas, 
                                     ((0, 0), (0, padding)))
            all_probas += all_weights[:, i][:, np.newaxis] * tree_probas

        return all_probas


    def predict(self, X):
        proba = self.predict_proba(X)
        return np.argmax(proba, axis=1)


    def _select_seed(self, X):
        if len(self.classifiers) == 0:
            # If it is the first dataset, randomly select the seed
            rng = np.random.default_rng(self.random_state)
            seed_index = rng.integers(0, len(X))
            return seed_index
        else:
            # Calculate the average distances to the previously selected datasets
            datasets_selected = self.dataset_seed[:len(self.classifiers)]
            distances = pairwise_distances(X, datasets_selected, metric=self.distance_metric)
            average_distances = np.mean(distances, axis=1)
            seed_index = np.argmax(average_distances)
            return seed_index

    def _create_dataset(self, X, seed_instances):

        distances = pairwise_distances(X, [seed_instances], metric=self.distance_metric)
        similarities = 1 / (1 + distances)
        weights = similarities / np.sum(similarities)

        # Randomly sample the dataset indices based on the weights
        rng = np.random.default_rng(self.random_state)
        selected_indexes = rng.choice(len(X), size=len(X), replace=True, p=weights.flatten())
        return selected_indexes


    def _train_single_tree(self, i, X, y):
        # Select randomly the seed using similarity-based approach
        seed_index = self._select_seed(X)
        seed_instance = X[seed_index]

        dataset_indexes = self._create_dataset(X, seed_instance)
        dataset_X = X[dataset_indexes]
        dataset_y = y[dataset_indexes]

        tree = DecisionTreeClassifier(max_depth=self.max_depth, random_state=self.random_state, ccp_alpha=0.00)
        tree.fit(dataset_X, dataset_y)

        return seed_instance, tree

