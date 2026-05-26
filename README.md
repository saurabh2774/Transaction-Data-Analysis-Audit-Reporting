Transaction Data Analysis & Audit Reporting

A data analytics and audit reporting project built using Python, Pandas, SQL, and Microsoft Excel to analyze large-scale transaction datasets, identify high-value transactions, clean duplicate records, and generate audit reports for business insights.

Project Overview

This project simulates a real-world financial transaction analysis workflow used in audit, risk, and data analytics domains.

The project performs:

Data cleaning and preprocessing
Duplicate record detection
Missing value handling
High-value transaction analysis
SQL-based transaction querying
Excel audit report generation
Tech Stack
Python
Pandas
SQLite (SQL)
Microsoft Excel
VS Code
Dataset Features

The dataset contains transaction-related information such as:

Transaction ID
Transaction Date
Client ID
Card ID
Transaction Amount
Merchant Information
Transaction Errors
Project Structure
Transaction-Analysis/
│
├── data/
│   ├── transactions.csv
│   └── transactions.db
│
├── reports/
│   └── Audit_Report.xlsx
│
├── scripts/
│   └── analysis.py
│
└── README.md
Features Implemented
Data Cleaning
Removed duplicate transaction records
Handled missing/null values
Converted transaction amount column into numeric format
Transaction Analysis
Identified high-value transactions
Analyzed top customers based on transaction amount
Generated transaction summaries
SQL Integration
Stored cleaned data into SQLite database
Executed SQL queries for analytical reporting
Excel Reporting

Generated Excel-based audit reports containing:

Cleaned transaction data
High-value transactions
Top customers summary
SQL Query Example
SELECT client_id,
SUM(amount) as Total_Amount
FROM transactions
GROUP BY client_id
ORDER BY Total_Amount DESC
LIMIT 10;
How to Run the Project
1. Clone Repository
git clone <your-github-repo-link>
2. Install Required Libraries
pip install pandas openpyxl matplotlib
3. Run the Script
cd scripts
python analysis.py
Output

The project generates:

SQLite database file
Excel audit report
Analytical summaries

Generated report location:

reports/Audit_Report.xlsx
Resume Description
Performed transaction dataset analysis using Python, Pandas, SQL, and Excel to clean data, identify duplicate records, and analyze high-value transactions.
Generated analytical summaries and Excel-based audit reports to support transaction monitoring and business insights.
Future Enhancements
Fraud detection analysis
Interactive dashboards using Power BI/Tableau
Automated anomaly detection
Data visualization and trend analysis
Author
SAURABH CHIKTE
