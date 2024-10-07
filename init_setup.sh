echo [$(date)]: "START"

echo [$(date)]: "creating env with python 3.10 version"

# Creating environment with Python 3.10
conda create -n mlenv python=3.10 -y

echo [$(date)]: "activating the environment"

# Activate the environment
conda activate mlenv

echo [$(date)]: "installing the dev requirements"

# Installing dev requirements from requirements_dev.txt
pip install -r requirements_dev.txt

echo [$(date)]: "END"
