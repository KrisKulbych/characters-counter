import sys
from pathlib import Path
from typing import Annotated

from typer import Option, Typer

from charcounter import count_character_frequency

from .logging_config import logger

app = Typer()


@app.command()
def calculate(
    file: Annotated[Path | None, Option("--file", "-f")] = None,
    paragraph: Annotated[str | None, Option("--paragraph", "-p")] = None,
) -> None:
    if not (file or paragraph):
        logger.error("Error! Please provide either --file or --paragraph for character counting.")
        sys.exit(1)
    if file and paragraph:
        logger.warning("Warning! Both arguments are provided. Application will prioritize file.")
    if file:
        logger.debug("Calculating characters in file...")
        result = count_character_frequency(file)
    else:
        logger.debug("Calculating characters in paragraph...")
        result = count_character_frequency(str(paragraph))
    logger.info(result)
