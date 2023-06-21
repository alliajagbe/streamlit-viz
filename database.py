from deta import Deta
import os

from dotenv import load_dotenv
load_dotenv(".env")

deta_key = os.getenv("DETA_KEY")

deta = Deta(deta_key)

# creating a new database

db = deta.Base("monthly_reports")

# inserting data
def insert_period(period, incomes, expenses, comment):
    return db.put({
        "key": period, 
        "incomes": incomes,
        "expenses": expenses,
        "comment": comment
    })

# fetching data
def fetch_all_periods():
    res = db.fetch()
    return res.items

def get_period(period):
    return db.get(period)