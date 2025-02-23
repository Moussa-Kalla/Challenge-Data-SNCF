from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import logging
import os


def train_random_forest(x_train, y_train):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    logging.basicConfig(filename='logs/output.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')    
    
    logging.info("Division des données en train/validation...")
    X_train, X_val, y_train_split, y_val_split = train_test_split(
        x_train, y_train, test_size=0.2, random_state=42
    )
    logging.info("Initialisation du modèle Random Forest...")
    model = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42, n_jobs=-1)
    logging.info("Entraînement du modèle en cours...")
    model.fit(X_train, y_train_split.values.ravel())
    logging.info("Entraînement terminé.")
    return model, X_val, y_val_split