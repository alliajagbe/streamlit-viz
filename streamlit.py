import streamlit as st
import plotly.graph_objects as go


# page configurations
incomes = ["salary", "dividends", "lottery"]
expenses = ["rent", "food", "bills", "saving", "fun", "clothes"]
currency = "USD"
page_title = "Budget App"
page_icon = "💰"
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)