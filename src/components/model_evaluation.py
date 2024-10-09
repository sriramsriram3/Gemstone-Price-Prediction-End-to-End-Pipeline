import os
import sys
import numpy as np
import pickle
from src.utils.utils import load_model,save_model
from urllib.parse import urlparse
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error
from src.logger.logger import logging
from src.exception.exceptions import custom_ecxeption
import mlflow
import mlflow.sklearn

class ModelEvaluation:
    def __init__(self):
        logging.info("evaluation started")

    def eval_metrics(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))# here is RMSE
        mae = mean_absolute_error(actual, pred)# here is MAE
        r2 = r2_score(actual, pred)# here is r3 value
        logging.info("evaluation metrics captured")
        return rmse, mae, r2

    def initiate_model_evaluation(self,train_array,test_array):
        try:
             X_test,y_test=(test_array[:,:-1], test_array[:,-1])

             model_path=os.path.join("artifacts","model.pkl")
             model=load_model(model_path)

             mlflow.set_tracking_uri("http://127.0.0.1:5000")  # Change set_registry_uri to set_tracking_uri

             
             logging.info("model has register")

             tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme

             print(tracking_url_type_store)



             with mlflow.start_run():

                prediction=model.predict(X_test)

                (rmse,mae,r2)=self.eval_metrics(y_test,prediction)

                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("r2", r2)
                mlflow.log_metric("mae", mae)

                 # Model registry does not work with file store
                if tracking_url_type_store != "file":

                    # Register the model
                    # There are other ways to use the Model Registry, which depends on the use case,
                    # please refer to the doc for more information:
                    # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                    mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")
                else:
                    mlflow.sklearn.log_model(model, "model")


        except Exception as e:
            raise custom_ecxeption(e,sys)