import pytest

from characters_counter import count_characters_occurrence


class TestCharactersCounter:
    def test_count_characters_occurrence(self) -> None:
        # Given
        cases = [
            ("abbbcccdf", 3),
            ("aabbccdd", 0),
            ("!@#123abcdee", 10),
            ("", 0),
            ("aAbBcC", 6),
        ]
        # When
        for input_text, expected_result in cases:
            # Then
            assert count_characters_occurrence(input_text) == expected_result

    def test_count_characters_occurrence_raises_expected_error_when_unhashable_input_is_provided(self) -> None:
        # Given
        cases = [123, 30.6, [], {}, set()]
        # When
        for input_text in cases:
            # Then
            with pytest.raises(TypeError):
                count_characters_occurrence(input_text)


if __name__ == '__main__':
    pytest.main()
