import logging
import os

from utils.config import LOG_DIR, LOG_FILE

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def get_logger():
    """
    Returns configured logger.
    """
    return logging.getLogger("ETL Logger")