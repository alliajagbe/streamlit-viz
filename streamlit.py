import streamlit as st
import plotly.graph_objects as go
import calendar
from datetime import datetime


# page configurations
incomes = ["salary", "dividends", "lottery"]
expenses = ["rent", "food", "bills", "saving", "fun", "clothes"]
currency = "Naira"
page_title = "Budget App"
page_icon = "💰"
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

years = [datetime.today().year, datetime.today().year + 1]
months = [calendar.month_name[i] for i in range(1, 13)]

st.header(f"Data Entry in {currency}")

with st.form("entry_form", clear_on_submit=True):
    month_col, year_col = st.columns(2)
    month_col.selectbox("Select Month", months, key="month")
    year_col.selectbox("Select Year", years, key="year")

    "---"
    "Enter your incomes and expenses below:"

    with st.expander("Incomes"):
        for income in incomes: 
            st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)

    with st.expander("Expenses"):
        for expense in expenses:
            st.number_input(f"{expense}:", min_value=0, format="%i", step=10, key=expense)

    with st.expander("Comment"):
        comment = st.text_area("", placeholder="Enter comment here...", max_chars=100)

    "---"
    submitted = st.form_submit_button("Save Entry")

    if submitted: 
        period = str(st.session_state.year) + "-" + str(st.session_state.month)
        incomes = {income: st.session_state[income] for income in incomes}
        expenses = {expense: st.session_state[expense] for expense in expenses}

        st.write(f"Incomes: {incomes}")
        st.write(f"Expenses: {expenses}")
        st.success(f"Entry for {period} saved successfully!")


# visualizations
st.header(f"Visualizations")
with st.form("saved_periods"):
    period = st.selectbox("Select Period:", ["2023_January"])
    submitted = st.form_submit_button("Visualize")