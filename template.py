import os
from pathlib import Path

list_of_filepaths=[
    "github/workflow/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/logger/logger.py",
    "src/utils/utils.py",
    "src/exception/exceptions.py",
    "src/pipelines/__init__.py",
    "src/pipelines/training_pipeline.py",
    "src/pipelines/prediction_pipeline.py",
    "setup.py",
    "init_setup.sh",
    "setup.cfg",
    "tox.ini",
    "pyproject.toml",
    "experiments/experiment.ipynb",
    "requirements.txt",
    "requirements_dev.txt",
    "tests/unit_test/__init__.py",
    "tests/integrate_test/__init__.py"
]

for filepath in list_of_filepaths:
    filepath=Path(filepath)
    file_dir,file_name=os.path.split(filepath)
    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass


