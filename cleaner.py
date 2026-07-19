import pandas as pd

class DataCleaner:
    def remove_duplicates(self,df):
        return df.drop_duplicates()
    
    def fill_missing_values(self,df):
        for column in df.columns:
            if df[column].dtype in ["float64","int64"]:
                df[column] = df[column].fillna(df[column].median())
            else:
                df[column] = df[column].fillna(df[column].mode()[0])
        return df
     