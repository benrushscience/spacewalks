# test_code.py

import pytest
from eva_data_analysis import text_to_duration

# convention to use test_ prefix for test functions and then add the name of the function being tested.
def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10

def test_text_to_duration_float():
    assert text_to_duration("10:15") == 10.25

def test_text_to_duration_irrational():
    # print(1e-5)
    # print(text_to_duration("10:20"))
    # print(abs(text_to_duration("10:20") - 10.333333))
    # assert abs(text_to_duration("10:20") - 10.333333) < 1e-5 #adding some tolerance to account for floating point precision issues
    assert text_to_duration("10:20") == pytest.approx(10.333333, rel=1e-5)  # using pytest.approx for floating point comparison
