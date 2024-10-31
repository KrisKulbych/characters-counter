from pathlib import Path
from typing import Iterator

import pytest

CONTENT = (
    "Typer is a library for building CLI applications that users will love using and developers "
    "will love creating. Typer is a library for building CLI applications that users will love using and "
    "developers will love creating. Based on Python type hints. "
    "It's also a command line tool to run scripts, automatically converting them to CLI applications."
)


@pytest.fixture()
def sample_textfile(tmp_path: Path) -> Iterator[Path]:
    tmp_file_path = tmp_path / "tmp_text_sample.txt"
    tmp_file_path.write_text(CONTENT)
    yield tmp_file_path


@pytest.fixture(scope="session")
def existing_textfile() -> Path:
    existing_textfile_path = Path("tests") / "text_sample.txt"
    return existing_textfile_path
