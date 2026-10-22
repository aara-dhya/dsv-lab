import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix_titles.csv")

print(df.info())

print(df.describe())

print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df.fillna("Unknown", inplace=True)

sns.countplot(x="type", data=df)
plt.show()

df["release_year"].hist()
plt.title("Release Year Distribution")
plt.show()