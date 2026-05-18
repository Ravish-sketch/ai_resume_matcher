import logging
import os

os.makedirs("outputs/logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("outputs/logs/app.log"),
        logging.StreamHandler()
    ]
)

def get_logger(name):
    return logging.getLogger(name)
