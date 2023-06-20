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

    with st.expander("Incomes"):
        for income in incomes: 
            st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)