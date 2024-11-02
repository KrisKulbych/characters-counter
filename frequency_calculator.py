from pathlib import Path
from typing import Annotated

import typer
from typing_extensions import Optional

from characters_counter import count_character_frequency
from logging_config import setup_logging

app = typer.Typer()
logger = setup_logging()


@app.command()
def calculate(
    file: Annotated[Optional[Path], typer.Option("--file", "-f")] = None,
    paragraph: Annotated[Optional[str], typer.Option("--paragraph", "-p")] = None,
) -> None:
    if file and paragraph:
        logger.warning("Warning! Both arguments is provided. Application will prioritize file.")
        res = count_character_frequency(file)
        logger.info(res)
    elif file:
        logger.debug("Calculating characters in file...")
        res = count_character_frequency(file)
        logger.info(res)
    elif paragraph:
        logger.debug("Calculating characters in paragraph...")
        res = count_character_frequency(paragraph)
        logger.info(res)
    else:
        logger.error("Error! Please provide either --file or --paragraph for character counting.")


if __name__ == "__main__":
    app()
