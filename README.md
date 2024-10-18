[![characters-counter-build](https://github.com/KrisKulbych/characters-counter/actions/workflows/build.yaml/badge.svg)](https://github.com/KrisKulbych/characters-counter/actions/workflows/build.yaml)

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

## Explanation 
1. *import Counter from collections*: This is used to count the occurrences of each character in the string.
2. *import cache from functools*: This decorator caches the result of the function for a given input, making it faster for repeated calls with the same string.
3. Constant *REQUIREMENT_OCCURRENCE = 1* defines necessary condition.
4. The function takes one argument, string, which is expected to be of type str (string).
5. The variable *character_counters* is assigned a dictionary-like object where each key is a character in the input string, and each value is the number of times that character appears.
6. The *filter()* function is used to filter out only those character counts that are equal to *REQUIREMENT_OCCURRENCE*, which is 1
7. The *sum()* function adds up all the filtered values. Since we're filtering for characters that appear once, this gives us the total number of unique characters.
8. The function is decorated with *@cache*, meaning that if the same string is passed to this function again, it won’t recompute everything—it will simply return the result from memory, saving computation time.

## Helpful Links
- [collections — Container datatypes](https://docs.python.org/3/library/collections.html)
- [pytest: helps you write better programs](https://docs.pytest.org/en/stable/)
- [Welcome to pytest-cov’s documentation!](https://pytest-cov.readthedocs.io/en/latest/)
- [How to Create Requirements.txt File in Python](https://www.geeksforgeeks.org/how-to-create-requirements-txt-file-in-python/)
- [Ignoring files](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files)
- [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/#:~:text=PEP%208%20suggests%20lines%20should,to%20run%20over%20several%20lines)

tags: `python` `python3` `problem-solving` `programming` `learn-python` `caracters-counter`
