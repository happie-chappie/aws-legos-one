"""
data_set_one - all string columns - a, b, c
data_set_two - one string column - c, two numeric columns - a, b
data_set_three - all numeric columns - a, b, c
"""
import pandas as pd

from src.validate import validate

data_set_one = pd.read_csv('tests/data_set_one.csv')
data_set_two = pd.read_csv('tests/data_set_two.csv')
data_set_three = pd.read_csv('tests/data_set_three.csv')

def test_data_set_one_true_scenario():
    string_column_names = ["a", "b", "c"]
    assert validate(data_set_one, string_column_names)

def test_data_set_one_false_scenario():
    string_column_names = ["c"]
    assert not validate(data_set_one, string_column_names)

def test_data_set_two_true_scenario():
    string_column_names = ["c"]
    assert validate(data_set_two, string_column_names)

def test_data_set_two_false_scenario():
    string_column_names = ["a"]
    assert not validate(data_set_two, string_column_names)

def test_data_set_three_true_scenario():
    string_column_names = []
    assert validate(data_set_three, string_column_names)

def test_data_set_three_false_scenario():
    string_column_names = ["a"]
    assert not validate(data_set_three, string_column_names)
