import os
import sys
from src.logger.logger import logging
from src.exception.exceptions import custom_ecxeption
import pandas as pd
from src.utils.utils import save_model
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransform


obj=DataIngestion()

train_data_path,test_data_path=obj.ingest_data()

dt=DataTransform()
train_arr,test_arr=dt.initialize_data_transformation(train_data_path,test_data_path)

print(train_arr,test_arr)