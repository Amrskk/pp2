import csv
import psycopg2
from db import insert_data, query_data, delete_data, update_data, enter_data, upload_csv
from db import get_records_by_pattern, insert_or_update_user, insert_many_users, query_data_with_pagination, delete_data_by_username_or_phone


# Connect to your postgres DB
conn = psycopg2.connect("postgresql://neondb_owner:npg_Tow97uEgYpAQ@ep-old-star-a22l0fgh-pooler.eu-central-1.aws.neon.tech/neondb?sslmode=require")
# Open a cursor to perform database operations
cur = conn.cursor()



userlist = [
    ("No", "No", "7017017012"), 
    ("New", "User", "0987654721"),
    ("User", "Neww", "1431231234"),
    ("Hello", "World", "3213993214")
]

# insert_many_users(userlist)

# get_records_by_pattern("Te")
insert_or_update_user("")


# upload_csv("./numbers.csv")
query_data()