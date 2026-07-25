import pandas as pd

df = pd.read_excel(
    "data/Dataset for Data Analytics.xlsx",
    engine="openpyxl"
)

print(df.head())
print(df.shape)