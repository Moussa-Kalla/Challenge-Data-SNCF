import tensorflow as tf
import numpy as np
import pandas as pd

def prediction(model, x_test, y_train):
    
    x_test_tensor = tf.convert_to_tensor(x_test, dtype=tf.float32)
    
    y_pred = model.predict(x_test_tensor)
    y_pred = y_pred.flatten()
    
    y_pred_reshaped = np.array(y_pred).reshape(-1, 1) 
    y_pred_df = pd.DataFrame(y_pred, columns=y_train.columns)

    sub = np.floor(y_pred_df['p0q0'])
    sub.to_csv('submissions/submission.csv')
    
    return y_pred
    