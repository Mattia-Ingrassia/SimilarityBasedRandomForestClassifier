# Spiegazione variante RandomForestClassifier

La classe utilizza la struttura che viene usata per i modelli di sklearn.

Viene quindi definito un costruttore come segue

``` python
class VariantOfRandomForestClassifier: 
    def __init__(self, n_estimators=10, max_depth=None, random_state=None): 
        self.n_estimators = n_estimators 
        self.max_depth = max_depth 
        self.random_state = random_state 
        self.classifiers = [] 
        self.dataset_seed = None 
```

La classe conterrà i metodi che sono necessari per implementare l'interfaccia di sklearn

``` python
def fit(self, X, y): 
# Implementazione del metodo di addestramento 
 
def predict_proba(self, X): 
# Implementazione del metodo di predizione delle probabilità 
 
def predict(self, X):  
# Implementazione del metodo di predizione delle classi  
 
def selected_seed(self, X): 
# Implementazione del metodo di selezione dei seed  
         
def create_dataset(self, X, seed_istances): 
# Implementazione del metodo di creazione dei dataset
```

## Metodo init

Il metodo init è il costruttore della classe e inizializza i seguenti parametri:

- n_estimators: numero di alberi decisionali da creare;
- max_depth: la profondità massima degli alberi decisionali;
- random_state: serve a controllare la generazione dei numeri casuali garantendo la
riproducibilità dei risultati;
- classifiers: una lista vuota che conterrà gli alberi decisionali;
- dataset_seed: una matrice che conterrà i seed selezionati per ogni albero.

## Metodo fit

Il metodo fit addestra l’algoritmo sui dati di training X e y:

1. Inizializza la lista classifiers e la matrice dataset_seed;
2. Per ogni albero decisionale:  
    - Seleziona un seed in base alla dissimilarità media
    - Costruisce un sottoinsieme del dataset in base al seed selezionato in  precedenza;
    - Addestra un albero decisionale su questo sottoinsieme e lo aggiunge alla lista classifiers

## Metodo predict_proba

Il metodo predict_proba calcola la probabilità delle classi per ciascuna istanza nel dataset X:

1. Inizializza una matrice all_proba per conservare le probabilità di ogni istanza;

2. Per ogni istanza x in X:
    - Calcola le distanze tra x e i seed dei vari alberi decisionali;
    - Calcola le similarità e le normalizza in pesi;
    - Calcola le probabilità predette dai vari alberi per x;
    - Media le probabilità predette utilizzando i pesi;
    - Conserva le probabilità mediate nella matrice all_proba.

3. Restituisce la matrice all_proba.


#TODO da sistemare