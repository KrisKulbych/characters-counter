from collections import Counter
from functools import cache

REQUIREMENT_OCCURRENCE = 1


@cache
def count_characters_occurrence(string: str) -> int:
    """
    The function returns the number of characters in the string occuring only
    once.
    """
    characters_counts = Counter(string)
    unique_occurrences = filter(lambda occurrence: (occurrence == REQUIREMENT_OCCURRENCE), characters_counts.values())
    unique_characters_number = sum(unique_occurrences)
    return unique_characters_number
