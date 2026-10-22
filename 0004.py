import matplotlib # Optional
matplotlib.use('Qt5Agg') # Optional

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

print(df.head())

df.drop_duplicates(inplace=True)

df.fillna("Unknown", inplace=True)

df["type"].value_counts().plot(kind="bar", color=["blue", "red"])
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()