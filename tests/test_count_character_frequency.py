from pathlib import Path

import pytest

from characters_counter import CustomFileNotFoundError, count_character_frequency


class TestCharacterFrequency:

    EXPECTED_RESULT = {
        "Typer is a library for building CLI applications that users will love using and developers will "
        "love creating": {"i": 10, "l": 10, "e": 8},
        "Based on Python type hints": {"n": 3, "t": 3, "s": 2},
        "It's also a command line tool to run scripts, automatically converting them to CLI applications": {
            "t": 10,
            "o": 9,
            "a": 8,
        },
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
        self, data_input: str, expected_result: dict[str, dict[str, int]]
    ) -> None:
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
        self, existing_textfile: Path
    ) -> None:
        # Given
        expected_result = self.EXPECTED_RESULT
        # When
        actual_result = count_character_frequency(existing_textfile)
        # Then
        assert actual_result == expected_result

    def test_count_character_frequency_with_invalid_filepath(self) -> None:
        # Given
        invalid_filepath = Path("not_existed_file.txt")
        # When / Then
        with pytest.raises(
            CustomFileNotFoundError, match=f"Error! The file {invalid_filepath} is not found or cannot be opened."
        ):
            count_character_frequency(invalid_filepath)
