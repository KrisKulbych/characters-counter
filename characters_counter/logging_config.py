import logging


def setup_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel("DEBUG")
    formatter = logging.Formatter("{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M")

    console_handler = logging.StreamHandler()
    console_handler.setLevel("DEBUG")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
