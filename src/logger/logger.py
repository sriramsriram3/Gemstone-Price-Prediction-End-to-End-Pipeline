import os
import logging 
from datetime import datetime

file_name=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.logs"

#creating a file inside the current working directory
log_path=os.path.join(os.getcwd(),"logs")
os.makedirs(log_path, exist_ok=True)

log_folder=os.path.join(log_path,file_name)

logging.basicConfig(
    level=logging.INFO, 
    filename=log_folder, 
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

logging.info("this is my first message")