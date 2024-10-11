from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransform
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation
import datetime
import numpy as np
import pendulum
from textwrap import dedent
from airflow import DAG
from airflow.operators.python import PythonOperator

ingest_pipeline = DataIngestion()
transform_pipeline = DataTransform()
train_pipeline = ModelTrainer()
evaluate_pipeline = ModelEvaluation()

with DAG(dag_id='germ_stone_prediction',
         description='Germ stone price prediction using MLOps',
         start_date=pendulum.datetime(2024, 10, 3, tz='UTC'),
         catchup=True,
         tags=['germstone', 'regression', 'mlops'],
         schedule='@daily') as dag:

    dag.doc_md = __doc__

    def ingestion_dag(**kwargs):
        ti = kwargs['ti']
        train_path, test_path = ingest_pipeline.ingest_data()
        ti.xcom_push(key="data_ingestion_artifacts", value={'train_path': train_path, 'test_path': test_path})

    def transform_dag(**kwargs):
        ti = kwargs['ti']
        data_ingestion_artifacts = ti.xcom_pull(task_ids="ingestion_task", key="data_ingestion_artifacts")
        train_arr, test_arr = transform_pipeline.initialize_data_transformation(data_ingestion_artifacts['train_path'],
                                                                       data_ingestion_artifacts['test_path'])
        ti.xcom_push(key="data_transform_artifacts", value={'train_array': train_arr.tolist(), 'test_array': test_arr.tolist()})

    def train_dag(**kwargs):
        ti = kwargs['ti']
        data_transform_artifacts = ti.xcom_pull(task_ids="transform_task", key="data_transform_artifacts")
        train_array = data_transform_artifacts['train_array']
        test_array = data_transform_artifacts['test_array']
        # Call the model training method using the transformed data
        train_pipeline.initate_model_training(np.array(train_array), np.array(test_array))

    data_ingestion_task = PythonOperator(
        task_id="ingestion_task",
        python_callable=ingestion_dag,
        doc_md=dedent(
            """\
            ### Data Ingestion
            This task handles data ingestion.
            """
        )
    )

    data_transform_task = PythonOperator(
        task_id="transform_task",
        python_callable=transform_dag,
        doc_md=dedent(
            """\
            ### Data Transformation
            This task handles data transformation.
            """
        )
    )

    model_trainer_task = PythonOperator(
        task_id="trainer_task",
        python_callable=train_dag,
        doc_md=dedent(
            """\
            ### Model Training
            This task handles model training.
            """
        )
    )

    data_ingestion_task >> data_transform_task >> model_trainer_task
