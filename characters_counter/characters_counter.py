import re
from collections import Counter
from functools import cache
from pathlib import Path

REQUIREMENT_OCCURRENCE = 1
NUM_OF_MOST_COMMON_CHARACTERS = 3


class CustomFileNotFoundError(Exception):
    """
    Raised when the file is not found or cannot be opened.
    """

    def __init__(self, filepath: Path):
        super().__init__(f"Error! The file {filepath} is not found or cannot be opened.")
        self.filepath = filepath


@cache
def count_characters_occurrence(string: str) -> int:
    """
    The function returns the number of characters in the string occuring only once.
    """
    characters_counts = Counter(string)
    unique_occurrences = filter(lambda occurrence: (occurrence == REQUIREMENT_OCCURRENCE), characters_counts.values())
    unique_characters_number = sum(unique_occurrences)
    return unique_characters_number


def get_frequent_characters_per_sentence(text: str) -> dict[str, dict[str, int]]:
    """
    The helper function counts the frequency of each character in the input sentence, excluding spaces.
    Single word is considered as a sentence as well.
    The number of characters returned is controlled by the global constant "NUM_OF_MOST_COMMON_CHARACTERS".
    """
    sentences = re.split(r"[.?!]", text)
    character_frequency: dict[str, dict[str, int]] = dict()
    for sentence in sentences:
        sentence = sentence.lstrip()
        count_characters = Counter(sentence.replace(" ", ""))
        frequent_characters_per_sentence = dict(count_characters.most_common(NUM_OF_MOST_COMMON_CHARACTERS))
        character_frequency[sentence] = frequent_characters_per_sentence
    return character_frequency


def open_and_read_textfile(filepath: Path) -> str:
    """
    The helper function attempts to open a text file and reads its contents as a string.
    If the file is not found, a CustomFileNotFoundError is raised.
    """
    try:
        with open(filepath, "r") as text_file:
            return text_file.read()
    except FileNotFoundError as error:
        raise CustomFileNotFoundError(filepath) from error


def count_character_frequency(data_input: Path | str) -> dict[str, dict[str, int]]:
    """
    The function counts most used letters/symbols in each sentence from the given textfile.
    """
    if Path(data_input).suffix:
        text = open_and_read_textfile(Path(data_input))
    else:
        text = str(data_input)
    character_frequency = get_frequent_characters_per_sentence(text)
    return character_frequency
