import pandas as pd

def rename_columns(df, names):  
    df2 = df.copy()
    df2.columns = names
    return df2