from data_processing import load_process_and_encode_data
from train_model import model_training 
from predict import prediction
from metrics_and_plots import metrics, plots


if __name__ == "__main__":
    x_train, y_train, x_test = load_process_and_encode_data()
    model, history = model_training(x_train, y_train)
    y_pred = prediction(model, x_test, y_train)
    metrics(x_train, y_train, model)
    plots(x_train, y_train, model, history)