from data_processing import load_process_and_encode_data
from train_model import train_random_forest
from metrics_and_plots import evaluate_model
from predict import generate_predictions
import logging
import os

if not os.path.exists('logs'):
        os.makedirs('logs')
logging.basicConfig(filename='logs/output.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    if not os.path.exists('logs'):
        os.makedirs('logs')
    logging.basicConfig(filename='logs/output.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    logging.info("Démarrage du pipeline de traitement des données.")
    x_train, y_train, x_test = load_process_and_encode_data()
    
    logging.info("Début de l'entraînement du modèle.")
    model, X_val, y_val = train_random_forest(x_train, y_train)
    
    logging.info("Évaluation du modèle.")
    evaluate_model(model, X_val, y_val)
    
    logging.info("Prédiction sur le jeu de test.")
    generate_predictions(model, x_test, y_train)
    
    logging.info("Pipeline terminé avec succès. /n /n /n")

if __name__ == "__main__":
    main()