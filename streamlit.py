import streamlit as st
import plotly.graph_objects as go
import calendar
from datetime import datetime


# page configurations
incomes = ["salary", "dividends", "lottery"]
expenses = ["rent", "food", "bills", "saving", "fun", "clothes"]
currency = "USD"
page_title = "Budget App"
page_icon = "💰"
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

years = [datetime.today().year, datetime.today().year + 1]
months = [calendar.month_name[i] for i in range(1, 13)]