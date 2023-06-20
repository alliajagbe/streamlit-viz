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

    if submitted:
        comment = "This is a comment"
        incomes = {"salary": 1000, "dividends": 2000, "lottery": 30000}
        expenses = {"rent": 1000, "food": 2000, "bills": 3000, "saving": 4000, "fun": 5000, "clothes": 6000}

        total_income = sum(incomes.values())
        total_expense = sum(expenses.values())
        remainder = total_income - total_expense
        inc_column, exp_column, rem_column = st.columns(3)
        inc_column.metric("Total Income", f"{total_income} {currency}")
        exp_column.metric("Total Expense", f"{total_expense} {currency}")
        rem_column.metric("Remainder", f"{remainder} {currency}")

        # income pie chart
        income_fig = go.Figure(data=[go.Pie(labels=list(incomes.keys()), values=list(incomes.values()))])
        income_fig.update_layout(title_text=f"Incomes for {period}")
        st.plotly_chart(income_fig, use_container_width=True)

