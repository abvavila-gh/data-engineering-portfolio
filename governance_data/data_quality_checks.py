import pandas as pd

def check_nulls(df, column):
    null_count = df[column].isnull().sum()
    return f"Column {column} has {null_count} null values"

if __name__ == "__main__":
    df = pd.DataFrame({"id": [1, 2, None], "value": [10, None, 30]})
    print(check_nulls(df, "id"))
    print(check_nulls(df, "value"))