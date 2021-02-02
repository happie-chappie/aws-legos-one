import pandas as pd

from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype


def validate(df, string_column_names):
    """
    This method returns true if all the string_columns in the
    dataframe are of type string and rest of the columns are
    of type 

    Args:
        df (DataFrame): DataFrame to validate
        string_columns (list): List of string columns

    Returns:
        bool: True if there is no NPI data, False otherwise
    """
    # getting all column names
    all_column_names = list(df.columns)
    # subsetting the numeric coluumn names from string column names
    numeric_column_names = list(set(all_column_names) -  set(string_column_names))

    # we loop through all the numeric columns
    for column_name in numeric_column_names:
        # checking if the numeric colulmn is numeric dtype or not
        # if it not the data is invalid
        if not is_numeric_dtype(df[column_name].values):
            return False

    # we loop through all the string columns
    for column_name in string_column_names:
        # checking if the string colulmn is string dtype or not
        # if it not the data is invalid
        if not is_string_dtype(df[column_name].values):
            return False

    # if all the column types are as expected then the data is valid
    return True
