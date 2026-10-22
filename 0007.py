import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_Data.csv")

print(df.corr())

sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()

sns.regplot(x="YearsExperience", y="Salary", data=df)
plt.title("Regression Analysis")
plt.show()