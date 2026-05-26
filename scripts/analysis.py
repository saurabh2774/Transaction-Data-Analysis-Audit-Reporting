import pandas as pd
import sqlite3

# Load dataset
df = pd.read_csv("../data/transactions.csv")

print("DATA LOADED SUCCESSFULLY")

# Show columns
print("\nCOLUMNS:")
print(df.columns)

# -----------------------------
# DATA CLEANING
# -----------------------------

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

print("\nDATA CLEANING COMPLETED")

# -----------------------------
# COLUMN NAMES
# -----------------------------

amount_column = "amount"
customer_column = "client_id"

# Convert amount column to numeric
df[amount_column] = pd.to_numeric(df[amount_column], errors="coerce")

# Remove rows with invalid amount
df = df.dropna(subset=[amount_column])

# -----------------------------
# HIGH VALUE TRANSACTIONS
# -----------------------------

high_value = df[df[amount_column] > 50000]

print("\nHIGH VALUE TRANSACTIONS FOUND:")
print(len(high_value))

# -----------------------------
# SAMPLE DATA FOR EXCEL
# -----------------------------

sample_data = df.head(10000)

# -----------------------------
# SQL DATABASE
# -----------------------------

conn = sqlite3.connect("../data/transactions.db")

# Store dataframe into SQL table
df.to_sql("transactions", conn, if_exists="replace", index=False)

print("\nSQL DATABASE CREATED")

# -----------------------------
# SQL QUERY
# -----------------------------

query = f"""
SELECT {customer_column},
SUM({amount_column}) as Total_Amount
FROM transactions
GROUP BY {customer_column}
ORDER BY Total_Amount DESC
LIMIT 10
"""

top_customers = pd.read_sql(query, conn)

print("\nTOP CUSTOMERS")
print(top_customers)

# -----------------------------
# EXCEL REPORT GENERATION
# -----------------------------

with pd.ExcelWriter("../reports/Audit_Report.xlsx") as writer:

    sample_data.to_excel(writer,
                         sheet_name="Sample_Cleaned_Data",
                         index=False)

    high_value.head(5000).to_excel(writer,
                                   sheet_name="High_Value_Transactions",
                                   index=False)

    top_customers.to_excel(writer,
                           sheet_name="Top_Customers",
                           index=False)

print("\nAUDIT REPORT GENERATED SUCCESSFULLY")