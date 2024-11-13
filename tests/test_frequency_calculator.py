import logging
from pathlib import Path

import pytest
from _pytest.logging import LogCaptureFixture
from typer.testing import CliRunner

from characters_counter.frequency_calculator import app


class TestFrequencyCalculator:

    EXPECTED_RESULT = {
        "Typer is a library for building CLI applications that users will love using and developers will "
        "love creating": {"i": 10, "l": 10, "e": 8},
        "Based on Python type hints": {"n": 3, "t": 3, "s": 2},
        "It's also a command line tool to run scripts, automatically converting them to CLI applications": {
            "t": 10,
            "o": 9,
            "a": 8,
        },
        "": {},
    }

    def test_calculate_with_both_arguments(
        self, runner: CliRunner, caplog: LogCaptureFixture, sample_textfile: Path
    ) -> None:
        caplog.set_level(logging.DEBUG)
        # Given
        result = runner.invoke(app, ["-f", str(sample_textfile), "-p", "python"])
        # When / Then
        assert result.exit_code == 0
        assert "Warning! Both arguments are provided. Application will prioritize file." in caplog.text
        assert str(self.EXPECTED_RESULT) in caplog.text

    def test_calculate_with_file_argument(
        self, runner: CliRunner, caplog: LogCaptureFixture, sample_textfile: Path
    ) -> None:
        caplog.set_level(logging.DEBUG)
        # Given
        result = runner.invoke(app, ["-f", str(sample_textfile)])
        # When / Then
        assert result.exit_code == 0
        assert "Calculating characters in file..." in caplog.text
        assert str(self.EXPECTED_RESULT) in caplog.text

    @pytest.mark.parametrize(
        "data_input, expected_result",
        [
            (
                "Python is the best language in the world",
                {"Python is the best language in the world": {"t": 4, "e": 4, "h": 3}},
            ),
            ("python", {"python": {"p": 1, "y": 1, "t": 1}}),
        ],
    )
    def test_calculate_with_paragraph_argument(
        self, runner: CliRunner, caplog: LogCaptureFixture, data_input: str, expected_result: str
    ) -> None:
        caplog.set_level(logging.DEBUG)
        # Given
        result = runner.invoke(app, ["-p", data_input])
        # When / Then
        assert result.exit_code == 0
        assert "Calculating characters in paragraph..." in caplog.text
        assert str(expected_result) in caplog.text

    def test_calculate_with_empty_input(self, runner: CliRunner, caplog: LogCaptureFixture) -> None:
        caplog.set_level(logging.ERROR)
        # Given
        result = runner.invoke(app)
        # When / Then
        assert result.exit_code == 1
        assert "Error! Please provide either --file or --paragraph for character counting." in caplog.text
