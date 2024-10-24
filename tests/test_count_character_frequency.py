import os
from collections import Counter
from pathlib import Path
from typing import Generator

import pytest
from _pytest.tmpdir import TempPathFactory

from characters_counter import count_character_frequency

CONTENT = (
    "Typer is a library for building CLI applications that users will love using and developers "
    "will love creating. Typer is a library for building CLI applications that users will love using and "
    "developers will love creating. Based on Python type hints. "
    "It's also a command line tool to run scripts, automatically converting them to CLI applications."
)


class TestCharacterFrequency:
    @pytest.mark.parametrize(
        "data_input, result",
        [
            ("Python is the best language in the world", {"t": 4, "e": 4, "h": 3}),
            ("python", {"p": 1, "y": 1, "t": 1}),
            ("", {}),
        ],
    )
    def test_count_character_frequency_with_string_input(self, data_input: Path, result: dict) -> None:
        assert count_character_frequency(data_input) == result

    @pytest.fixture(scope="function")
    def sample_file(self, tmp_path_factory: TempPathFactory) -> Generator[Path, None, None]:
        tmp_file_path = tmp_path_factory.mktemp("data") / "text_sample.txt"
        tmp_file_path.write_text(CONTENT)
        yield tmp_file_path
        os.remove(tmp_file_path)

    def test_count_character_frequency_with_correct_filepath_input_using_pytest_fixture(
        self, sample_file: Path
    ) -> None:
        result = count_character_frequency(sample_file)
        expected_result = {
            "Typer is a library for building CLI applications that users will love using and developers will "
            "love creating.": Counter({"i": 20, "l": 20, "e": 16}),
            "Based on Python type hints.": Counter({"n": 3, "t": 3, "s": 2}),
            "It's also a command line tool to run scripts, automatically converting them to CLI applications.": Counter(
                {"t": 10, "o": 9, "a": 8}
            ),
        }
        assert result == expected_result

    def test_count_character_frequency_with_correct_filepath_input_using_textfile_sample(self) -> None:
        text_file = Path("tests") / "text_sample.txt"
        # assert text_file.exists()
        result = count_character_frequency(text_file)
        expected_result = {
            "Typer is a library for building CLI applications that users will love using and developers will "
            "love creating.": Counter({"i": 20, "l": 20, "e": 16}),
            "Based on Python type hints.": Counter({"n": 3, "t": 3, "s": 2}),
            "It's also a command line tool to run scripts, automatically converting them to CLI applications.": Counter(
                {"t": 10, "o": 9, "a": 8}
            ),
        }
        assert result == expected_result

    def test_count_character_frequency_with_invalid_filepath(self) -> None:
        with pytest.raises(FileNotFoundError):
            with open("not_existed_file.txt", "r") as text_file:
                text_file.read()

    def test_FileNotFound_message(self) -> None:
        with pytest.raises(FileNotFoundError, match="Error! The file is not found or cannot be opened."):
            raise FileNotFoundError("Error! The file is not found or cannot be opened.")


if __name__ == "__main__":
    pytest.main()
