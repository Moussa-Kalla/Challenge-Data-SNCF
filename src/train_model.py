import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def model_training(x_train, y_train):

    x_train_tensor = tf.convert_to_tensor(x_train, dtype=tf.float32)
    y_train_tensor = tf.convert_to_tensor(y_train.values, dtype=tf.float32)

    model = keras.Sequential([
        layers.Dense(128, activation='relu', input_shape=(x_train.shape[1],)),
        layers.Dense(64, activation='relu'),
        layers.Dense(32, activation='relu'),
        layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mae', metrics=['mae'])

    history = model.fit(x_train_tensor, y_train_tensor, epochs=5, batch_size=64, validation_split=0.2, verbose=1)
    
    return model, history
    
    