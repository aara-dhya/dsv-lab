import pandas as pd

df = pd.read_csv("data.csv")

print("Missing Values:")
print(df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)

df.drop_duplicates(inplace=True)

df.to_csv("cleaned_data.csv", index=False)

print("Cleaned dataset saved successfully.")