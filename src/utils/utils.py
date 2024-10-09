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
            model = pickle.load(f)
        logging.info('The model loaded successfully')
        return model
    except Exception as e:
        logging.error('The model loading failed')
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
        logging.error('The model saving failed')
        raise custom_ecxeption(e, sys)

# Evaluation of the model
def evaluation(X_train, y_train, x_test, y_test, models):
    """
    Evaluate the performance of multiple models using R² score.

    Parameters:
    X_train (array-like): Training feature data.
    y_train (array-like): Training target data.
    x_test (array-like): Testing feature data.
    y_test (array-like): Testing target data.
    models (dict): Dictionary of models to evaluate.

    Returns:
    dict: A dictionary containing model names and their corresponding R² scores.
    """
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
        logging.error('Evaluation of the model failed')
        raise custom_ecxeption(e, sys)
