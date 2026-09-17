import pandas as pd


DATA_URL = (
    "https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/"
    "book/data/bellevue_almshouse_modified.csv"
)

df_bellevue = pd.read_csv(DATA_URL)


def fibonacci(n):
    """Return the nth number in the Fibonacci sequence."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def to_binary(n):
    """Return a nonnegative integer's binary representation as a string."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


def _clean_gender(data):
    cleaned = data.copy()
    invalid_gender = cleaned["gender"].notna() & ~cleaned["gender"].isin(["m", "w"])
    cleaned.loc[invalid_gender, "gender"] = pd.NA
    return cleaned


def task_1():
    """Return column names ordered from least to most missing values."""
    print("The gender values '?', 'g', and 'h' are invalid and are treated as missing.")
    cleaned = _clean_gender(df_bellevue)
    return cleaned.isna().sum().sort_values().index.tolist()


def task_2():
    """Return the total number of admissions in each year."""
    years = pd.to_datetime(df_bellevue["date_in"]).dt.year.rename("year")
    return years.groupby(years).size().reset_index(name="total_admissions")


def task_3():
    """Return the average age for each valid gender."""
    print("The gender values '?', 'g', and 'h' are invalid and are excluded.")
    cleaned = _clean_gender(df_bellevue)
    return cleaned.groupby("gender")["age"].mean()


def task_4():
    """Return the five most common professions in prevalence order."""
    return df_bellevue["profession"].value_counts().head(5).index.tolist()
