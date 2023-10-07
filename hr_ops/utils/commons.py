# import numpy as np
import numpy as np
import pandas as pd


def create_df(input: any, options: object | None) -> pd.DataFrame:
    if options.data_type == 'csv':
        return pd.read_csv(options.csv_file_path)

    if options.data_type == 'csv' and options.url_extract == True:
        return pd.read_csv(options.csv_url_path)

    if options.data_type == 'excel':
        return pd.read_excel(options.excel_file_path)

    if input:
        return pd.DataFrame(input)

# json_data = df.to_json(orient='records', date_format='iso')


def check_missing(df):
    return df.isnull().sum()


def replace_missing(df, value):
    # replace missing values with a specified value
    return df.fillna(value)


def drop_missing_rows(df):
    # drop rows with missing values
    return df.dropna()


def drop_missing_columns(df):
    return df.dropna(axis=1)


def filter_data(df, condition):
    '''
    Filter data based on a condition
    '''
    return df[condition]


def summary_statistics(df):
    '''
    Calculate summary stas of a DataFrame
    '''
    return df.describe()


def sort_dataframe(df, column, ascending=True):
    '''
    Sort a DataFrame by a specified column
    '''
    return df.sort_values(by=column, ascending=ascending)


def group_and_aggregate(df, by_column, aggregations):
    '''
    Group data by a column and calculate aggregations
    '''
    return df.groupby(by_column).agg(aggregations)


def apply_function(df, new_column, function, columns_to_apply):
    '''
    Create a new column by applying a function to existing columns
    '''
    df[new_column] = df[columns_to_apply].apply(function, axis=1)
    return df


def pivot_dataframe(df, index, columns, values):
    '''
    Pivot a DataFrame
    '''
    return df.pivot_table(index=index, columns=columns, values=values)


def concat_dataframes(df1, df2, axis=0):
    '''
    Concatenate two DataFrames
    '''
    return pd.concat([df1, df2], axis=axis)


def merge_dataframes(df1, df2, on_column):
    '''
    Merge two DataFrames based on a common col
    '''
    return pd.merge(df1, df2, on=on_column)


def calculate_correlation(df, column1, column2):
    '''
    Calculate correlation between two cols
    '''
    return df[column1].corr(df[column2])


def calculate_new_column(df, new_column, calculation):
    '''
    Create new column with calculated values
    '''
    df[new_column] = calculation
    return df
