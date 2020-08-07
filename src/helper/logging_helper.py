"""
.. module:: src.helper.logging_helper
   :synopsis: Configure a logger
"""
import os

from loguru import logger

LOG_PATH = os.path.join("logs", "flask_api.log")
logger.add(LOG_PATH, format="[{time:YYYY-MM-DD HH:mm:ss}] - [{level.no}] - [{level}] - [{message}]")
new_logger = logger
