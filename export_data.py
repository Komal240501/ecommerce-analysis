"""
Run this ONCE on your own PC (where SQL Server + the ODBC driver work).
It exports the six tables to CSV files in a ./data folder next to this
script. Copy that data folder into your Streamlit deployment repo so the
cloud app can load a snapshot instead of connecting to your local database.
"""
import os
import pandas as pd
import pyodbc

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=KOMAL\\SQLEXPRESS;'
    'Database=Ecommerce_Analytics_project;'
    'Trusted_connection=yes;'
)

os.makedirs("data", exist_ok=True)

tables = {
    "sessions": "SELECT * FROM website_sessions",
    "orders": "SELECT * FROM orders",
    "order_items": "SELECT * FROM orders_items",
    "products": "SELECT * FROM products",
    "refunds": "SELECT * FROM order_item_refunds",
    "website_pageviews": "SELECT * FROM website_pageviews",
}

for name, query in tables.items():
    df = pd.read_sql(query, conn)
    path = f"data/{name}.csv"
    df.to_csv(path, index=False)
    print(f"Saved {path}  ({len(df)} rows)")

print("\nDone. Copy the 'data' folder into your app's deployment folder/repo.")
