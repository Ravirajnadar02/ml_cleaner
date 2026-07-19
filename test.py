import pandas as pd
from cleaner import DataCleaner

data={
    "Name": ["Alice","Bob","Alice","David","Charlie"],
    "Age": [25,30,25,40,None],
    "City":["New York","Los Angeles","New York","Chicago","Boston"  ]

}

df =pd.DataFrame(data)
print("Before cleaning data")
print(df)

cleaner =DataCleaner()

df =cleaner.remove_duplicates(df)
print("\n After cleaning data")
print(df)

print(df.dtypes)
print(df.isnull().sum())

print("\n Before filling missing values")
print(df)

df=cleaner.fill_missing_values(df)
print("\n after filling missing values")
print(df)
