import os
import numpy as np
import pandas as pd
from src.logger.logger import logging
from src.exception.exceptions import custom_ecxeption
import sys
from sklearn.metrics import r2_score
import pickle

# Loading the model
def load_model(filepath):
    try:
        with open(filepath, 'rb') as f:
            return pickle.load(f)
        logging.info('the model loading successfully')
    except Exception as e:
        logging.info('The model loading failed') 
        raise custom_ecxeption(e, sys)
    
# Saving the model
def save_model(filepath, obj):
    try:
        file = os.path.dirname(filepath)
        os.makedirs(file, exist_ok=True)
        with open(filepath, 'wb') as f:
            pickle.dump(obj, f)
        logging.info('The model is saved successfully') 
    except Exception as e:
        logging.info('The model saving failed')  
        raise custom_ecxeption(e, sys)

# Evaluation of the model
def evaluation(X_train, y_train, x_test, y_test, models):
    try:
        report = {}
        for name, ind_model in models.items():
            model = ind_model
            model.fit(X_train, y_train)
            y_pred = model.predict(x_test)
            r2 = r2_score(y_test, y_pred)
            report[name] = r2
        
        return report

    except Exception as e:
        logging.info('Evaluation of the model failed')  
        raise custom_ecxeption(e, sys)
