from collections import Counter
from functools import cache


@cache
def count_characters_occurrence(string: str) -> int:
    """
    The function returns the number of characters in the string occuring only
    once.
    """
    characters_occurrence = Counter(string)
    single_occurrence = sum(
        [1 for v in characters_occurrence.values() if v == 1]
    )
    return single_occurrence


if __name__ == '__main__':
    cases = [
        ("abbbcccdf", 3),
        ("aabbccdd", 0),
        ("!@#123abcdee", 10),
    ]
    for input_string, expecter_result in cases:
        assert count_characters_occurrence(input_string) == expecter_result
