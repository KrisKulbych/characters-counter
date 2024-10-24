import collections
import re
from collections import Counter, defaultdict
from functools import cache
from pathlib import Path

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


def get_frequent_characters_per_sentence(sentence: str) -> dict:
    """
    The helper function counts the frequency of each character in the input sentence, excluding spaces.
    Single word is considered as a sentence as well.
    The number of characters returned is controlled by the global constant "NUM_OF_MOST_COMMON_CHARACTERS".
    :param sentence: str
    :return: dict[str, int]
    """
    count_characters = Counter(sentence.replace(" ", ""))
    return dict(count_characters.most_common(NUM_OF_MOST_COMMON_CHARACTERS))


def count_character_frequency(data_input: Path) -> defaultdict[str, Counter[str]] | dict[str, int] | None:
    """
    The function counts most used letters/symbols in each sentence from the given textfile.
    :param data_input: Path
    :return: dict[str, int]
    """
    if Path(data_input).suffix:
        try:
            with open(data_input, "r") as text_file:
                text = text_file.read()
        except FileNotFoundError:
            print("Error! The file is not found or cannot be opened.")
        else:
            sentences = re.findall(r"\w+.*?[.?!]", text)
            character_frequency: collections.defaultdict = defaultdict(Counter)
            for sentence in sentences:
                frequent_characters_per_sentence = get_frequent_characters_per_sentence(sentence)
                character_frequency[sentence].update(Counter(frequent_characters_per_sentence))
            print(type(character_frequency))
            return character_frequency

    elif isinstance(data_input, str):
        return get_frequent_characters_per_sentence(data_input)
