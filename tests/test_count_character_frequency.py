from collections import Counter
from pathlib import Path

import pytest

from characters_counter import count_character_frequency


class TestCharacterFrequency:

    EXPECTED_RESULT = {
        "Typer is a library for building CLI applications that users will love using and developers will "
        "love creating": Counter({"i": 20, "l": 20, "e": 16}),
        "Based on Python type hints": Counter({"n": 3, "t": 3, "s": 2}),
        "It's also a command line tool to run scripts, automatically converting them to CLI applications": Counter(
            {"t": 10, "o": 9, "a": 8}
        ),
        "": {},
    }

    @pytest.mark.parametrize(
        "data_input, expected_result",
        [
            (
                "Python is the best language in the world",
                {"Python is the best language in the world": {"t": 4, "e": 4, "h": 3}},
            ),
            ("python", {"python": {"p": 1, "y": 1, "t": 1}}),
            ("", {"": {}}),
        ],
    )
    def test_count_character_frequency_with_string_input(
        self, data_input: Path, expected_result: dict[str, Counter[str]]
    ) -> None:
        # Given: data_input: Path
        # When
        actual_result = count_character_frequency(data_input)
        # Then
        assert actual_result == expected_result

    def test_count_character_frequency_with_correct_filepath_input_using_pytest_fixture(
        self, sample_textfile: Path
    ) -> None:
        # Given
        expected_result = self.EXPECTED_RESULT
        # When
        actual_result = count_character_frequency(sample_textfile)
        # Then
        assert actual_result == expected_result

    def test_count_character_frequency_with_correct_filepath_input_using_textfile_sample(
        self, existed_textfile: Path
    ) -> None:
        # Given
        expected_result = self.EXPECTED_RESULT
        # When
        actual_result = count_character_frequency(existed_textfile)
        # Then
        assert actual_result == expected_result

    def test_count_character_frequency_with_invalid_filepath(self) -> None:
        # Given
        invalid_filepath = Path("not_existed_file.txt")
        # When: The count_character_frequency function is called
        # Then
        with pytest.raises(FileNotFoundError, match="Error! The file is not found or cannot be opened."):
            count_character_frequency(invalid_filepath)


if __name__ == "__main__":
    pytest.main()
