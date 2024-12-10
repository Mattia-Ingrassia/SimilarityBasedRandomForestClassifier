import numpy as np 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import pairwise_distances 
 
class SimilarityBasedRandomForestClassifier: 
    def __init__(self, n_estimators=10, max_depth=None, random_state=None, distance_metric="euclidean"): 
        self.n_estimators = n_estimators 
        self.max_depth = max_depth 
        self.random_state = random_state 
        self.classifiers = [] 
        self.dataset_seed = None
        self.distance_metric = distance_metric
 
    def fit(self, X, y): 
        self.classifiers = []
        self.dataset_seed = np.zeros((self.n_estimators, X.shape[1])) 
        self.n_classes = len(np.unique(y)) 
         
        # Iterazione per creare e addestrare gli alberi decisionali 
        for i in range(self.n_estimators): 
            # Seleziona casualmente il seed in base alla dissimilarità media 
            seed_index = self.selected_seed(X)
            # print(f"EDITED-{i}: selected seed index output:", seed_index)
            seed_istances = X[seed_index] 
            self.dataset_seed[i, :] = seed_istances 
 
            dataset_indexes = self.create_dataset(X, seed_istances) 
            dataset_X, dataset_y = X[dataset_indexes], y[dataset_indexes] 

            tree = DecisionTreeClassifier(max_depth=self.max_depth, random_state=self.random_state, ccp_alpha=0.00) 
            tree.fit(dataset_X, dataset_y) 

            self.classifiers.append(tree) 
 
        return self 
 
    def predict_proba(self, X): 
        # Inizializza la struttura per memorizzare predizioni, numero di casi di test X numero di classi
        all_proba = np.zeros((X.shape[0], self.n_classes))
        # per ogni caso di test (i-esima entry(x) di X)  
        for i, x in enumerate(X): 
            # Calcola le distanze rispetto al dataset selezionato in precedenza 
            distances = pairwise_distances([x], self.dataset_seed, metric=self.distance_metric).squeeze()  
            similarities = 1 / (1 + distances)            
            # Utilizza la similarità normalizzata come peso per le predizioni degli alberi 
            weights = similarities / np.sum(similarities) 
            # Calcola le probabilità predette dai vari alberi 
            tree_probas = []
            for tree in self.classifiers:
                proba = tree.predict_proba([x])[0]
                # print("proba i:",i,", x:",len(x)," = ",proba.shape)
                if len(proba) < self.n_classes:
                    padded_proba = np.zeros(self.n_classes)
                    padded_proba[:len(proba)] = proba
                    proba = padded_proba
                
                tree_probas.append(proba)
            
            tree_probas = np.array(tree_probas).squeeze()

            # Non dovrebbe essere necessario
            # flattened_weights = weights.flatten() 
    
            # Mediare le predizioni degli alberi utilizzando i pesi 
            weighted_probas = np.average(tree_probas, weights=weights, axis=0) 
            all_proba[i] = weighted_probas 
 
        return all_proba 
 
    def predict(self, X): 
        proba = self.predict_proba(X) 
        return np.argmax(proba, axis=1) 
     
    def selected_seed(self, X): 
        if len(self.classifiers) == 0: 
            # Se è il primo dataset, seleziona casualmente il seed 
            rng = np.random.default_rng(self.random_state)
            index = rng.integers(0, len(X))
            return index 
        else: 
            # Calcola le distanze medie rispetto ai dataset selezionati in precedenza 
            distances = pairwise_distances(X, self.dataset_seed[:len(self.classifiers), :], metric=self.distance_metric)
            average_distances = np.mean(distances, axis=1) 
            seed_index = np.argmax(average_distances) 
            return seed_index 
         
    def create_dataset(self, X, seed_istances): 
 
        distances = pairwise_distances(X, [seed_istances], metric=self.distance_metric) 
        similarities = 1 / (1 + distances) 
        weights = similarities / np.sum(similarities) 

        # Campiona casualmente gli indici del dataset basandosi sui pesi 
        rng = np.random.default_rng(self.random_state)

        selected_indexes = rng.choice(len(X), size=len(X), replace=True,  p=weights.flatten())
        return selected_indexes