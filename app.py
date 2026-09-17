import streamlit as st

from apputil import fibonacci, task_1, task_2, task_3, task_4, to_binary


st.title("Week 3: Basic Pandas")

st.header("Recursive Functions")
amount = st.number_input(
    "Enter a nonnegative integer",
    min_value=0,
    max_value=30,
    value=None,
    step=1,
    format="%d",
)

if amount is not None:
    st.write(f"Fibonacci number: `{fibonacci(amount)}`")
    st.write(f"Binary representation: `{to_binary(amount)}`")

st.header("Bellevue Almshouse Analysis")

st.subheader("1. Columns ordered by missing values")
st.write(task_1())

st.subheader("2. Admissions by year")
st.dataframe(task_2(), hide_index=True)

st.subheader("3. Average age by gender")
st.dataframe(task_3().rename("average_age"))

st.subheader("4. Five most common professions")
st.write(task_4())
