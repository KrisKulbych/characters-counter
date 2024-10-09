# Characters Counter Application 

## Description
This Python application contains a function count_characters_occurrence(), that returns the number of characters in the string occuring only
    once.
It uses caching for performance optimization, meaning that if the same string is passed to the function multiple times, the result is fetched from memory instead of recalculating.

## Features 
- Caching with @cache Decorator that optimizes repeated calls with the same input.
- Uses Counter to quickly count character occurrences.
- The function uses a filter combined with a lambda function to select only those characters that occur exactly once.
- Has adjustable parameter for occurrence requirement.

## Requirements
- collections.Counter
- functools.cache
- pytest

## Solution 
<details>
  <summary>Click For Solution</summary>

```
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
    unique_occurrences = filter(
                            lambda occurrence: (
                                    occurrence == REQUIREMENT_OCCURRENCE
                                        ), characters_counts.values()
                            )
    unique_characters_number = sum(unique_occurrences)
    return unique_characters_number
```
</details>

## Explanation 
1. *import Counter from collections*: This is used to count the occurrences of each character in the string.
2. *import cache from functools*: This decorator caches the result of the function for a given input, making it faster for repeated calls with the same string.
3. Constant *REQUIREMENT_OCCURRENCE = 1* defines necessary condition.
4. The function takes one argument, string, which is expected to be of type str (string).
5. The variable *character_counters* is assigned a dictionary-like object where each key is a character in the input string, and each value is the number of times that character appears.
6. The *filter()* function is used to filter out only those character counts that are equal to *REQUIREMENT_OCCURRENCE*, which is 1
7. The *sum()* function adds up all the filtered values. Since we're filtering for characters that appear once, this gives us the total number of unique characters.
8. The function is decorated with *@cache*, meaning that if the same string is passed to this function again, it won’t recompute everything—it will simply return the result from memory, saving computation time.

## Test Cases 
<details>
  <summary>Test Case 1: checking correct behavior for several cases using pytest</summary>

```
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
```
</details>
<details>
  <summary>Test Case 2: checking fail behavior by raising expected error when unhashable input is provided</summary>

```
import pytest

from characters_counter import count_characters_occurrence


class TestCharactersCounter:
    def test_count_characters_occurrence_raises_expected_error_when_unhashable_input_is_provided(self) -> None:
        # Given
        cases = [123, 30.6, [], {}, set()]
        # When
        for input_text in cases:
            # Then
            with pytest.raises(TypeError):
                count_characters_occurrence(input_text)

```
</details>

## Helpful Links
- [collections — Container datatypes](https://docs.python.org/3/library/collections.html)
- [pytest: helps you write better programs](https://docs.pytest.org/en/stable/)
- [Welcome to pytest-cov’s documentation!](https://pytest-cov.readthedocs.io/en/latest/)
- [How to Create Requirements.txt File in Python](https://www.geeksforgeeks.org/how-to-create-requirements-txt-file-in-python/)
- [Ignoring files](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files)

tags: `python` `python3` `problem-solving` `programming` `learn-python`