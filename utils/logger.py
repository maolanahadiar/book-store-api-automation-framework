import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "reports/logs"
LOG_FILE = "api_test.log"

def get_logger(name):
    """Create logger for API test execution"""

    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    # Prevent duplicate logs from pytest
    logger.propagate = False

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = RotatingFileHandler(
        filename=os.path.join(LOG_DIR, LOG_FILE),
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger