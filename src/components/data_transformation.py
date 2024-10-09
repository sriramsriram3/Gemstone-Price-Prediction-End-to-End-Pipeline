# src/components/data_transformation.py
import os
import pandas as pd
from src.logger.logger import logging
from src.exception.exceptions import custom_ecxeption
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
import sys
import numpy as np
from src.utils.utils import save_model
from sklearn.pipeline import Pipeline

class DataTransformConfig:
    transform_path = os.path.join('artifacts', 'preprocessor.pkl')  # Path to save the transformation pipeline

class DataTransform:
    def __init__(self):
        self.transform_config = DataTransformConfig()  # Instance of configuration for data transformation

    def transformdata(self):
        """
        This method defines and returns the preprocessing pipeline.
        """
        try:
            logging.info('Data transformation initiated')

            # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['cut', 'color', 'clarity']
            numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']

            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']

            logging.info('Pipeline initiated')

            # Create pipelines for numeric and categorical features
            num_pipeline = Pipeline([
                ('imputer', SimpleImputer()),  # Handle missing values for numerical columns
                ('scaling', StandardScaler())  # Scale numerical features
            ])

            cat_pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy='most_frequent')),  # Handle missing values for categorical columns
                ('encoding', OrdinalEncoder(categories=[cut_categories, color_categories, clarity_categories])),  # Ordinal encoding
                ('scaling', StandardScaler())  # Scale categorical features
            ])

            # Combine both pipelines into a ColumnTransformer
            preprocess = ColumnTransformer([
                ('numpipeline', num_pipeline, numerical_cols),
                ('catpipeline', cat_pipeline, categorical_cols)
            ])

            logging.info('Data transformation completed')
            return preprocess

        except Exception as e:
            logging.error('Data transformation failed')
            raise custom_ecxeption(e, sys)

    def initialize_data_transformation(self,train_path,test_path):
        """
        This method reads the train and test data, applies the transformation, 
        and saves the transformation pipeline as a pickle file.
        """
        try:

            # Read train and test data from the provided paths
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Train and test data read successfully")
            logging.info(f'Train Dataframe Head:\n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head:\n{test_df.head().to_string()}')

            # Initialize the transformation pipeline
            preprocessing_obj = self.transformdata()

            # Identify target and drop columns
            target_column_name = 'price'
            drop_columns = [target_column_name, 'id']  # Make sure 'id' exists in your dataset

            # Split input features and target from train and test data
            input_feature_train_df = train_df.drop(columns=drop_columns, axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=drop_columns, axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing pipeline on training and testing datasets")

            # Apply the transformation pipeline to train and test data
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            # Combine input features and target variable for both train and test data
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            # Save the preprocessing object (pipeline) to a pickle file
            logging.info(f'Saving transformation pipeline to: {self.transform_config.transform_path}')
            save_model(
                filepath=self.transform_config.transform_path,
                obj=preprocessing_obj
            )

            logging.info("Preprocessing pickle file saved successfully")

            return train_arr, test_arr

        except Exception as e:
            logging.error(f"Exception occurred during data transformation: {e}")
            raise custom_ecxeption(e, sys)

if __name__ == '__main__':
    data_transform = DataTransform()
    data_transform.initialize_data_transformation()
