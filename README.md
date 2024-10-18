# MLopsProject
Germstone Price Prediction with MLOps

This project aimed to predict gemstone prices using machine learning models while integrating MLOps tools to automate, scale, and monitor the workflow efficiently.

** Data Collection and Versioning

The dataset containing features like carat weight, cut, color, and clarity was collected. DVC (Data Version Control) was used to track changes in the dataset, ensuring reproducibility throughout the pipeline.

** Data Preprocessing

Data cleaning and transformation steps were automated. This included encoding categorical features, handling missing values, and normalizing numerical data. By using a reproducible preprocessing pipeline, the workflow became more robust.

** Model Training

Multiple machine learning models (e.g., Decision Trees, Random Forest) were trained. MLflow was employed to track experiments, log hyperparameters, and save model artifacts for comparison.

** Model Evaluation

The models were evaluated using metrics like RMSE (Root Mean Squared Error) to ensure optimal performance. MLflow was essential for tracking these evaluations and selecting the best-performing model.

** Deployment with Docker and Airflow

After evaluation, the best model was containerized using Docker to ensure compatibility across different environments. The deployment and scheduling tasks were managed by Apache Airflow, automating the entire pipeline from data ingestion to model deployment.

** Monitoring with Evidently AI

To ensure that the model continued to perform well in production, Evidently AI was integrated for real-time monitoring. It provided reports on model drift, data quality issues, and other performance metrics, allowing for proactive retraining or adjustments when the model's performance declined.

