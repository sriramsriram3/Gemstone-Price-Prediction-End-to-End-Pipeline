import numpy as np
import pandas as pd
from src.logger.logger import logging
from src.exception.exceptions import custom_ecxeption
import os
import sys
from sklearn.model_selection import train_test_split
from pathlib import Path
from dataclasses import dataclass

class DataIngestionConfig:
    def __init__(self):
        self.raw_data_path='artifacts/raw.csv'
        self.train_data_path='artifacts/train.csv'
        self.test_data_path='artifacts/test.csv'
        os.makedirs('artifacts',exist_ok=True)

    
class DataIngestion:
    def __init__(self):
        self.config=DataIngestionConfig()

    def ingest_data(self):
        try:
            logging.info('taking the dataset from the github')
            url=url = 'https://raw.githubusercontent.com/sriramsriram3/Datasets/main/raw.csv'
            data=pd.read_csv(url)
            logging.info('read the data from the git hub')

            data.to_csv(self.config.raw_data_path,index=False)
            logging.info('saved the raw dataset into the artifacts' )
            
            train,test=train_test_split(data,test_size=0.25,random_state=18)
            logging.info('splitted the data into train and test ')

            train.to_csv(self.config.train_data_path,index=False)
            test.to_csv(self.config.test_data_path,index=False)
            logging.info('saved the train and test into artifacts')

            return self.config.test_data_path,self.config.train_data_path



        except Exception as e:
            logging.info()
            raise custom_ecxeption(e,sys)
if __name__ == '__main__':
    ingest=DataIngestion()
    ingest.ingest_data()