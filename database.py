from deta import Deta

deta_key = "a0qiawdh_mky8ZU9eRKDRcHYbrHZVeYZNSYVau4dD"

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