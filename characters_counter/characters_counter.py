import collections
import re
from collections import Counter
from functools import cache
from pathlib import Path
from typing import Dict, Union

REQUIREMENT_OCCURRENCE = 1
NUM_OF_MOST_COMMON_CHARACTERS = 3


@cache
def count_characters_occurrence(string: str) -> int:
    """
    The function returns the number of characters in the string occuring only once.
    """
    characters_counts = Counter(string)
    unique_occurrences = filter(lambda occurrence: (occurrence == REQUIREMENT_OCCURRENCE), characters_counts.values())
    unique_characters_number = sum(unique_occurrences)
    return unique_characters_number


def count_character_frequency(data_input: Union[str, Path]) -> Dict[str, int]:
    """
    The function returns most used letters/symbols per sentence depending on NUM_OF_MOST_COMMON_CHARACTERS constant.
    Single word is considered as sentence as well.
    :param data_input: str or filepath
    :return: dict
    """
    if not isinstance(data_input, str):
        raise TypeError("Error! Data input must be a string or a filepath.")
    elif isinstance(data_input, str) and not Path(data_input).suffix:
        if data_input:
            count_characters = Counter(data_input.replace(" ", ""))
            character_frequency = dict(count_characters.most_common(NUM_OF_MOST_COMMON_CHARACTERS))
        else:
            raise ValueError("Error! Empty data input isn't allowed.")
    else:
        try:
            with open(data_input, "r") as file:
                text = file.read()
                sentences = re.findall(r"\w+.*?[.?!]", text)
                total: collections.Counter = Counter()
                for sentence in sentences:
                    count_characters = Counter(sentence.replace(" ", ""))
                    total.update(count_characters)
                character_frequency = dict(total.most_common(NUM_OF_MOST_COMMON_CHARACTERS))
                print(type(total))
        except IOError:
            raise FileNotFoundError("Error! File isn't found.")

    return dict(character_frequency)
