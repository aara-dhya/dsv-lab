# dsv-lab

# Data Science & Visualization Lab (DSVL) – Oral Exam Preparation Guide

During your practical exam, examiners typically test two things after you execute your assigned problem statement: **why you used specific functions/parameters** in your code and **what the output represents statistically**. 

---

## Core Python, NumPy, and Data Cleaning (Assignments 1–3)

### Assignment 1: Student Marks Dataset (Python Dictionaries & Functions)
* **Why did you wrap `students.values()` inside `list()`?**
  In Python 3, `students.values()` returns a `dict_values` view object rather than a standard list, so wrapping it in `list()` converts the extracted marks (`85, 92, 76, 88, 95`) into an indexable list structure.
* **What does `students.items()` do in the `for` loop?**
  The `.items()` method returns key-value pairs as `(name, mark)` tuples, allowing the loop to unpack and print both the student's name and their score simultaneously.
* **What happens if the dictionary is empty when `average_marks()` is called?**
  Because `average_marks()` calculates `sum(marks) / len(marks)`, an empty dictionary makes `len(marks)` equal to $0$, raising a `ZeroDivisionError`.
* **Can we calculate average, max, and min without converting `students.values()` to a list first?**
  Yes, built-in functions like `sum()`, `max()`, `min()`, and `len()` accept any iterable, including `dict_values` directly.

### Assignment 2: NumPy Array Operations and Pandas DataFrame
* **Why use a NumPy array (`np.array`) instead of a standard Python list for numerical operations?**
  NumPy arrays store elements of the same data type in contiguous memory blocks, enabling fast vectorized calculations (`np.sum`, `np.mean`, `np.std`) without writing explicit Python loops.
* **What does Standard Deviation (`np.std(data)`) tell us about the dataset?**
  In your output, the standard deviation is $27.5855$ around a mean of $59.2$, which measures how spread out the numbers are from the average. A low standard deviation means values cluster closely around the mean; a high value indicates wide dispersion.
* **What is the difference between a 1D NumPy array and a Pandas DataFrame?**
  A 1D NumPy array is a homogeneous grid of values accessed by positional index, whereas a Pandas DataFrame (`pd.DataFrame`) is a 2D labeled tabular structure with named columns (`columns=["Numbers"]`) and an explicit row index ($0$ to $9$).
* **How many rows does `df.head()` display by default, and how do you change it?**
  `df.head()` displays the first 5 records by default ($0$ through $4$). Passing an integer like `df.head(3)` displays that specific number of rows, while `df.tail()` shows the last 5 records.

### Assignment 3: Data Preprocessing using Pandas
* **Why do we chain `.isnull().sum()` instead of just calling `df.isnull()`?**
  Calling `df.isnull()` returns a full DataFrame of boolean (`True`/`False`) values, whereas chaining `.sum()` counts the `True` ($1$) values to show the total number of missing entries per column.
* **Why is `numeric_only=True` passed inside `df.mean(numeric_only=True)`?**
  Datasets often contain text/categorical columns alongside numbers; `numeric_only=True` prevents Pandas from throwing a `TypeError` by restricting the mean calculation strictly to numerical columns.
* **When should you replace missing values with the median instead of the mean?**
  The assignment prompt allows replacing missing values using either mean or median. Use the **mean** when numerical data is symmetrically distributed, and use the **median** (`df.median(numeric_only=True)`) when the column contains extreme outliers or skewed data, since outliers heavily distort the mean.
* **What is the purpose of `inplace=True` in `fillna()` and `drop_duplicates()`?**
  `inplace=True` modifies the existing DataFrame `df` directly in memory instead of returning a new copy that you would have to reassign with `df = ...`.
* **Why do we set `index=False` in `df.to_csv("cleaned_data.csv", index=False)`?**
  Without `index=False`, Pandas writes the DataFrame's row numbers ($0, 1, 2...$) as an extra unnamed first column in the saved CSV file.

---

## Exploratory Data Analysis and Visualization (Assignments 4–5)

### Assignment 4: Load Kaggle Dataset, Clean Data, and Plot Graph
* **Why did we fill missing values with `"Unknown"` here instead of `df.mean()` like in Assignment 3?**
  The Netflix dataset (`netflix_titles.csv`) contains primarily categorical/text columns (such as director, cast, and country), so string imputation (`"Unknown"`) is required instead of a numerical mean.
* **Explain how `df["type"].value_counts().plot(kind="bar")` works step by step.**
  First, `df["type"]` selects the column indicating whether a title is a Movie or TV Show. Next, `.value_counts()` counts the frequency of each unique category in descending order. Finally, `.plot(kind="bar")` uses Matplotlib under the hood to render those counts as vertical bars.
* **Why is `plt.show()` called at the end of the script?**
  `plt.show()` flushes and renders the active Matplotlib figure window on screen and clears the current figure state so subsequent plots do not overlap on the same canvas.

### Assignment 5: Data Preprocessing and Exploratory Data Analysis (EDA)
* **What is the difference between `df.info()` and `df.describe()`?**
  * `df.info()` prints structural metadata: total entries, column names, non-null counts, data types (`int64`, `object`), and memory usage.
  * `df.describe()` computes summary statistics (count, mean, standard deviation, min, $25\%$/$50\%$/$75\%$ quartiles, and max) for numerical columns like `release_year`.
* **How does `sns.countplot(x="type", data=df)` differ from Matplotlib's bar plot in Assignment 4?**
  Seaborn's `countplot` automatically calculates the frequency of categories in the `"type"` column directly from the raw DataFrame `df`, eliminating the need to manually call `.value_counts()` first.
* **What is the difference between a Bar Chart (`countplot`) and a Histogram (`df["release_year"].hist()`)?**
  * A **bar chart / count plot** compares frequencies of discrete **categorical** variables (e.g., `"Movie"` vs. `"TV Show"`) with gaps between bars.
  * A **histogram** groups continuous or numerical data (`release_year`) into contiguous ranges called **bins** to show the underlying frequency distribution across time.

---

## Regression, Correlation, and BI Dashboards (Assignments 6–8)

### Assignment 6: Simple Linear Regression
* **Why does `X = df[["YearsExperience"]]` use double square brackets while `y = df["Salary"]` uses single square brackets?**
  Scikit-learn's `model.fit(X, y)` requires the feature matrix `X` to be a **2D structure** `(n_samples, n_features)` (a DataFrame created via `[[ ]]`), whereas the target vector `y` can be a **1D Series** `(n_samples,)` created via `[ ]`.
* **What is the mathematical equation of Simple Linear Regression, and how do `model.coef_[0]` and `model.intercept_` map to it?**
  The equation is:
  $$y = mx + c \quad \text{(or } y = \beta_1 x + \beta_0\text{)}$$
  * `model.coef_[0]` ($m$ or $\beta_1$) is the **slope**: the predicted increase in `Salary` for every $1$ additional year of experience.
  * `model.intercept_` ($c$ or $\beta_0$) is the **y-intercept**: the baseline predicted `Salary` when `YearsExperience` is $0$.
* **What does `model.fit(X, y)` actually compute?**
  It trains the linear model using Ordinary Least Squares (OLS), finding the line that minimizes the sum of squared residuals (vertical distances) between the actual data points (`plt.scatter(X, y)`) and the predicted line (`plt.plot(X, prediction)`).

### Assignment 7: Correlation and Regression Analysis
* **What is the range of values in `df.corr()`, and how do you interpret them?**
  `df.corr()` calculates the Pearson correlation coefficient ($r$) between numerical columns, which ranges from **$-1$ to $+1$**:
  * **$+1$**: Perfect positive linear relationship (as `YearsExperience` increases, `Salary` increases).
  * **$0$**: No linear relationship.
  * **$-1$**: Perfect negative linear relationship.
* **What do the parameters `annot=True` and `cmap="coolwarm"` do in `sns.heatmap()`?**
  * `annot=True` prints the numerical correlation value directly inside each colored cell of the heatmap.
  * `cmap="coolwarm"` sets the color palette from cool blue (low/negative correlation) to warm red (high positive correlation).
* **How is correlation different from regression?**
  **Correlation** (`df.corr()`) measures the strength and direction of a linear association between two variables symmetrically ($r(X,Y) = r(Y,X)$), whereas **regression** (`sns.regplot`) fits an asymmetric predictive equation to estimate dependent variable $y$ (`Salary`) from independent variable $x$ (`YearsExperience`).
* **What does the shaded band around the line in `sns.regplot()` represent?**
  By default, `sns.regplot()` renders a **$95\%$ confidence interval** around the regression line, showing where the true regression line is likely to fall.

### Assignment 8: Sales Dashboard and Data Storytelling (Tableau / Power BI)
* **What is a KPI Card, and why do we place KPIs at the top of a dashboard?**
  KPI stands for **Key Performance Indicator**. Cards for `Total Sales`, `Total Profit`, `Total Orders`, and `Average Sales` provide high-level executive metrics at a glance before the user drills into granular charts.
* **Why did you choose a Line Chart for Monthly Sales, a Bar Chart for Categories/Products, and a Pie Chart for Segments?**
  * **Line Chart (`Monthly Sales Trend`)**: Best for showing continuous trends over time.
  * **Bar Chart (`Sales by Category`, `Top 10 Products`)**: Best for comparing magnitudes across discrete categories and ranking top items.
  * **Pie Chart (`Sales by Segment`)**: Best for showing part-to-whole proportions when there are very few categories (e.g., Consumer, Corporate, Home Office).
* **What is the difference between Dimensions and Measures in Tableau / Power BI?**
  * **Dimensions** are qualitative, categorical, or temporal fields used to group or filter data (e.g., `Region`, `Category`, `Year`, `Segment`).
  * **Measures** are quantitative numerical fields that can be aggregated via sum or average (e.g., `Sales`, `Profit`, `Orders`).
* **What is "Data Storytelling," and what actionable anomaly did your dashboard reveal?**
  Data storytelling translates raw charts into business decisions. For example, while the `Technology` category and `West` region drive high revenue and profit, some products record **high sales but low/negative profit** (often due to heavy discounting or shipping costs), signaling where management needs to revise pricing.

---

## Practical Execution Fixes & Examiner Trap Questions

Several code snippets in your lab handout contain formatting typos from document conversion that will throw a `SyntaxError` or `AttributeError` if typed verbatim during the exam. Keep this checklist handy when writing your code:

| Assignment | Handout Typo in PDF | Corrected Executable Code | Error Avoided |
| :--- | :--- | :--- | :--- |
| **Ass 1** | `def maximum marks (marks):` and `def minimum marks (marks):` | `def maximum_marks(marks):` and `def minimum_marks(marks):` | `SyntaxError` (spaces are not allowed in function names) |
| **Ass 2** | `data np.array([...])` and `df pd.DataFrame(...)` | `data = np.array([...])` and `df = pd.DataFrame(...)` | `SyntaxError` (missing assignment operator `=`) |
| **Ass 3–7** | `df pd.read_csv(...)` | `df = pd.read_csv(...)` | `SyntaxError` (missing assignment operator `=`) |
| **Ass 4–5** | `"netflix titles.csv"` | `"netflix_titles.csv"` | `FileNotFoundError` (standard Kaggle file uses an underscore) |
| **Ass 5** | `df ["release year").hist()` | `df["release_year"].hist()` | `SyntaxError` (mismatched bracket `)` and missing underscore) |
| **Ass 6** | `from sklearn.linear_model import Linear Regression` | `from sklearn.linear_model import LinearRegression` | `SyntaxError` (no space in class name `LinearRegression`) |
| **Ass 6** | `print("Intercept:", model.intercept)` | `print("Intercept:", model.intercept_)` | `AttributeError` (Scikit-learn learned attributes end with a trailing underscore `_`) |

``` bash 
python -m venv .venv 
source .venv/bin/activate 
pip install matplotlib numpy pandas scikit-learn 
