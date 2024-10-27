from pathlib import Path
from typing import Iterator

import pytest
from _pytest.tmpdir import TempPathFactory

CONTENT = (
    "Typer is a library for building CLI applications that users will love using and developers "
    "will love creating. Typer is a library for building CLI applications that users will love using and "
    "developers will love creating. Based on Python type hints. "
    "It's also a command line tool to run scripts, automatically converting them to CLI applications."
)


@pytest.fixture(scope="session")
def sample_textfile(tmp_path_factory: TempPathFactory) -> Iterator[Path]:
    base_temp = tmp_path_factory.getbasetemp()
    tmp_file_path = Path(base_temp) / "tmp_text_sample.txt"
    tmp_file_path.write_text(CONTENT)
    yield tmp_file_path


@pytest.fixture(scope="session")
def existed_textfile() -> Path:
    existed_textfile_path = Path("tests") / "text_sample.txt"
    return existed_textfile_path
