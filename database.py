from deta import Deta

deta_key = "a0qiawdh_mky8ZU9eRKDRcHYbrHZVeYZNSYVau4dD"

deta = Deta(deta_key)

# creating a new database

db = deta.Base("monthly_reports")