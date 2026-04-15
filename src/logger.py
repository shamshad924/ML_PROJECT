import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # log file name with date and time
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # log file path
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) # log file path with log file name


logging.basicConfig(filename=LOG_FILE_PATH,
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
# lets make some logging to test our logging configuration
# if __name__=="__main__":
#     logging.info("Logging has started")