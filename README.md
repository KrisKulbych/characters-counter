[![python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=yellow)](https://www.python.org)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![characters-counter-build](https://github.com/KrisKulbych/characters-counter/actions/workflows/build.yaml/badge.svg)](https://github.com/KrisKulbych/characters-counter/actions/workflows/build.yaml)

# Characters Counter
Characters Counter is a Python library designed to count the frequency of characters in sentences, or text files. It focuses on identifying frequently used characters within sentences and counting unique characters in strings, with customizable settings.

## Installation 
Characters Counter is available on TestPyPI:
```console
python -m pip install --extra-index-url https://test.pypi.org/simple/ characters-counter
```
Characters Counter officially supports Python >= 3.12.

## Features 
***1. Count unique characters in a string.***
The count_characters_occurrence function counts the number of characters in the string occuring only once. It uses caching for performance optimization, meaning that if the same string is passed to the function multiple times, the result is fetched from memory instead of recalculating.

***2. Most frequent characters in sentences.***
The count_character_frequency function counts most used letters/symbols in each sentence from the given textfile (default: top 3).

***3. Command-line utility.***
The library provides a CLI tool to count the frequency of characters in text. It supports processing text input via the --paragraph option or by specifying a file path with --file.

## Usage

### 1. Import the library in your code

Count unique characters in a string
```console
from characters_counter import count_characters_occurrence

input_text = "!@#123abcdee"
result = count_characters_occurrence(input_text)
print(f"Number of unique characters: {result}")
```

Count the most frequent characters in sentences
```console
from characters_counter import get_frequent_characters_per_sentence

input_text = "Python is the best language in the world."
result = get_frequent_characters_per_sentence(input_text)
print("Most frequent characters per sentence:", result)
```

Process text from a file
```console
from characters_counter import count_character_frequency

file_path = "text_sample.txt"
result = count_character_frequency(file_path)
print("Most frequent characters per text file:", result)
```

### 2. Using the CLI
Run the utility through the command line.
After installing the library, you can import app() from characters_counter in your file for text analysis.

To analyze the frequency of characters in a text file, use the --file or -f option and provide the file path:
```console
python <your_script.py> --file path/to/your/file.txt
```

To analyze a paragraph provided directly, use the --paragraph or -p option:
```console
python <your_script.py> --paragraph "Your input text here."
```

If both --file and --paragraph are provided, the application will prioritize the file and log a warning:
```console
python <your_script.py> --file path/to/your/file.txt --paragraph "Your input text here."
```

## Logging
The library uses a built-in logger to provide insights during execution.
Example Logger Output:
```console
2024-11-14 15:30 - DEBUG - Calculating characters in paragraph...
2024-11-14 15:30 - INFO - {'Hello world': {'l': 3, 'o': 2, 'H': 1}}
```

## Configuration
Global Constants
* ***REQUIREMENT_OCCURRENCE***: Configures the number of unique occurrences to count. Default: 1.
* ***NUM_OF_MOST_COMMON_CHARACTERS***: Determines the number of characters to return in sentence analysis. Default: 3.

## Testing
Run tests
```console
pytest tests\
```

## For Contributors
This project is managed with poetry. All python dependencies have to be specified inside pyproject.toml file. 
1. Install poetry globally:
```console
curl -sSL https://install.python-poetry.org | python -
```

2. Follow the steps in the command's output to add poetry to PATH.

3. Install dependencies to virtualenv:
```console
poetry env use python
poetry shell
poetry install
```

tags: `python` `python3` `problem-solving` `programming` `learn-python` `caracters-counter` `poetry` `cli` `testpypi`
