from seasons import inspect_birthday
from seasons import get_minutes
import pytest

"""Test Birthday Formats"""

def test_notborn():
    assert inspect_birthday("2029-05-12") == "Invalid Date Format"

def test_other_formats():
    assert inspect_birthday("05-12-1994") == "Invalid Date Format"
    assert inspect_birthday("12-05-1994") == "Invalid Date Format"

def test_proper_format():
    assert inspect_birthday("1994-05-12") == "1994-05-12"
    assert inspect_birthday("1993-04-19") == "1993-04-19"

def test_no_input():
    assert inspect_birthday("") == "Invalid Date Format"

