import pandas as pd
import logging
import numpy as np
import os

def generate_predictions(model, x_test, y_train):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    logging.basicConfig(filename='logs/output.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')    
    
    logging.info("Génération des prédictions sur les données de test...")
    y_pred = model.predict(x_test)
    
    y_pred_df = pd.DataFrame(y_pred, columns=y_train.columns)

    sub = np.floor(y_pred_df['p0q0'])
    sub.to_csv("submissions/submission.csv")

    logging.info("Fichier de soumission enregistré sous 'submissions/submission.csv'")
