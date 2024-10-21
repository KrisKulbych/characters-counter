from contextlib import nullcontext as does_not_raise
from typing import Any, Type

import pytest

from characters_counter import count_character_frequency, count_characters_occurrence


class TestCharactersCounter:
    @pytest.mark.parametrize(
        "input_text, expected_result", [("abbbcccdf", 3), ("aabbccdd", 0), ("!@#123abcdee", 10), ("", 0), ("aAbBcC", 6)]
    )
    def test_count_characters_occurrence(self, input_text: str, expected_result: str) -> None:
        assert count_characters_occurrence(input_text) == expected_result

    @pytest.mark.parametrize("input_text", [123, 30.6, [], {}, set()])
    def test_count_characters_occurrence_raises_TypeError_when_unhashable_input_is_provided(
        self, input_text: str
    ) -> None:
        with pytest.raises(TypeError):
            count_characters_occurrence(input_text)

    @pytest.mark.parametrize(
        "data_input, result, expectation",
        [
            ("Python is the best language in the world", {"t": 4, "e": 4, "h": 3}, does_not_raise()),
            ("python", {"p": 1, "y": 1, "t": 1}, does_not_raise()),
            ("tests\\text.txt", {"e": 80, "t": 72, "o": 64}, does_not_raise()),
            ("tests\\text_2.txt", {}, pytest.raises(FileNotFoundError)),
            (123, {}, pytest.raises(TypeError)),
            ({}, {}, pytest.raises(TypeError)),
            ("", {}, pytest.raises(ValueError)),
        ],
    )
    def test_count_character_frequency(self, data_input: Any, result: Any, expectation: Type) -> None:
        with expectation:
            assert count_character_frequency(data_input) == result

    def test_count_character_frequency_raises_ValueError_when_empty_data_is_provided(self) -> None:
        with pytest.raises(ValueError, match="Error! Empty data input isn't allowed."):
            raise ValueError("Error! Empty data input isn't allowed.")

    def test_count_character_frequency_raises_TypeError_when_wrong_data_is_provided(self) -> None:
        with pytest.raises(TypeError, match="Error! Data input must be a string or a filepath."):
            raise TypeError("Error! Data input must be a string or a filepath.")

    def test_count_character_frequency_raises_FileNotFoundError_when_filepath_is_not_existed(self) -> None:
        with pytest.raises(TypeError, match="Error! File isn't found."):
            raise TypeError("Error! File isn't found.")


if __name__ == "__main__":
    pytest.main()
