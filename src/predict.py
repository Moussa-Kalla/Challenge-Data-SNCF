import tensorflow as tf

def prediction(model, x_test):
    
    x_test_tensor = tf.convert_to_tensor(x_test, dtype=tf.float32)
    
    y_pred = model.predict(x_test_tensor)
    y_pred = y_pred.flatten()
    
    return y_pred
