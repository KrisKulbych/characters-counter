import pytest

from characters_counter import count_characters_occurrence


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
