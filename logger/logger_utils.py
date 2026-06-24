import logging
from logging.handlers import RotatingFileHandler
import os


def setup_logger(name="app_logger", log_file="app.log", level=logging.INFO):
    """Function to centralize logger configuration."""
    # 1. Create a custom logger instance
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent log duplicate propagation to parent loggers
    logger.propagate = False

    # Clear existing handlers if function is called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()

    # 2. Define a reusable formatting style
    log_format = logging.Formatter(
        "%(asctime)s - %(name)s - [%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 3. Create a Console Handler (Outputs to terminal)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)

    # 4. Create a Rotating File Handler (Saves to a disk file)
    # Automatically rotates file when it hits 5MB; keeps last 3 backups
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
    )
    file_handler.setFormatter(log_format)
    file_handler.setLevel(logging.DEBUG)  # Capture deep debug logs in the file
    logger.addHandler(file_handler)

    return logger