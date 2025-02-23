import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import logging
import os

def evaluate_model(model, X_val, y_val):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    logging.basicConfig(filename='logs/output.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')    
    
    logging.info("Évaluation du modèle en cours...")
    y_pred = model.predict(X_val)
    mae = mean_absolute_error(y_val, y_pred)
    mse = mean_squared_error(y_val, y_pred)
    r2 = r2_score(y_val, y_pred)
    logging.info(f"MAE: {mae:.4f}\nMSE: {mse:.4f}\nR²: {r2:.4f}")

    # Graphiques de performances
    logging.info("Génération des graphiques...")
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.scatter(y_val, y_pred, alpha=0.5)
    plt.xlabel("Valeurs Réelles")
    plt.ylabel("Prédictions")
    plt.title("Vérités vs Prédictions")

    plt.subplot(1, 2, 2)
    errors = abs(y_val.values.ravel() - y_pred)
    plt.hist(errors, bins=50)
    plt.xlabel("Erreur Absolue")
    plt.title("Distribution des Erreurs Absolues")

    plt.tight_layout()
    plt.savefig("plots/plot_results.png")
    plt.close()
    logging.info("Graphiques enregistrés dans 'plots/plot_results.png'.")
