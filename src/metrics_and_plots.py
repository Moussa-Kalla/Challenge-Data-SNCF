import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def metrics(x_train, y_train, model):
    mae = mean_absolute_error(y_train, model.predict(x_train))
    mse = mean_squared_error(y_train, model.predict(x_train))
    r2 = r2_score(y_train, model.predict(x_train))

    print(f"MAE: {mae:.4f}")
    print(f"MSE: {mse:.4f}")
    print(f"R² Score: {r2:.4f}")
    


def plots(x_train, y_train, model, history):
    model_predict = model.predict(x_train)
    
    plt.figure(figsize=(16, 5))
    plt.subplot(1, 3, 1)
    plt.plot(history.history['loss'], label='Train Loss (MAE)')
    plt.plot(history.history['val_loss'], label='Validation Loss (MAE)')
    plt.xlabel("Époques")
    plt.ylabel("Loss (MAE)")
    plt.title("Évolution de la Loss (MAE)")
    plt.legend()

    plt.subplot(1, 3, 2)
    plt.plot(history.history['mae'], label='Train MAE')
    plt.plot(history.history['val_mae'], label='Validation MAE')
    plt.xlabel("Époques")
    plt.ylabel("Mean Absolute Error (MAE)")
    plt.title("Évolution de MAE")
    plt.legend()

    plt.tight_layout()
    plt.show()

    plt.subplot(1, 3, 3)
    plt.scatter(y_train, model_predict, alpha=0.5)
    plt.xlabel("Valeurs Réelles (Y_train)")
    plt.ylabel("Prédictions")
    plt.title("Comparaison entre Vérités Terrains et Prédictions")
    plt.show()