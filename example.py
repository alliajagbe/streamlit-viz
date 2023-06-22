import streamlit as st
import plotly.graph_objects as go
import calendar
from datetime import datetime
from streamlit_option_menu import option_menu
import database as db


# page configurations
incomes = ["salary", "dividends", "lottery"]
expenses = ["rent", "food", "bills", "fun", "clothes"]
currency = "Naira"
page_title = "Budget App"
page_icon = "💰"
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

years = [datetime.today().year, datetime.today().year + 1]
months = [calendar.month_name[i] for i in range(1, 13)]

# hiding streamlit style
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# navigation bar
selected = option_menu(
    menu_title = None,
    options = ["Data Entry", "Visualizations"],
    icons = ["pencil-fill", "bar-chart-fill"],
    orientation = "horizontal",
)

if selected == "Data Entry":
    st.header(f"Data Entry in {currency}")

    with st.form("entry_form", clear_on_submit=True):
        month_col, year_col = st.columns(2)
        month_col.selectbox("Select Month", months, key="month")
        year_col.selectbox("Select Year", years, key="year")

        "---"
        "Enter your incomes and expenses below:"

        with st.expander("Incomes"):
            for income in incomes: 
                st.number_input(income, key=income, step=0.01, format="%f")

        with st.expander("Expenses"):
            for expense in expenses:
                st.number_input(expense, key=expense, step=0.01, format="%f")

        "---"
        submitted = st.form_submit_button("Submit")

        if submitted:
            period = str(st.session_state.year) + " " + str(st.session_state.month)
            incomes = {income: st.session_state[income] for income in incomes}
            expenses = {expense: st.session_state[expense] for expense in expenses}
            st.success("Data successfully submitted!")
