
from pathlib import Path
import sqlite3
import pandas as pd

# Find the project folders and source dataset
project_dir = Path(__file__).resolve().parent.parent
csv_path = project_dir / "data" / "application_train.csv"
db_path = project_dir / "data" / "fintech_loan_analysis.db"

# Select only the columns needed for our analysis
columns = [
    "SK_ID_CURR",
    "TARGET",
    "NAME_CONTRACT_TYPE",
    "CODE_GENDER",
    "FLAG_OWN_CAR",
    "FLAG_OWN_REALTY",
    "CNT_CHILDREN",
    "AMT_INCOME_TOTAL",
    "AMT_CREDIT",
    "AMT_ANNUITY",
    "AMT_GOODS_PRICE",
    "NAME_INCOME_TYPE",
    "NAME_EDUCATION_TYPE",
    "NAME_FAMILY_STATUS",
    "NAME_HOUSING_TYPE",
    "DAYS_BIRTH",
    "DAYS_EMPLOYED",
    "OCCUPATION_TYPE",
]

if not csv_path.exists():
    raise FileNotFoundError(
        f"Dataset not found: {csv_path}"
    )

print("Reading the selected columns...")
df = pd.read_csv(csv_path, usecols=columns)

print(f"Rows loaded: {len(df):,}")

# Create the SQLite database and table
with sqlite3.connect(db_path) as connection:
    df.to_sql(
        "loan_applications",
        connection,
        if_exists="replace",
        index=False,
        chunksize=10_000,
    )

    connection.execute(
        "CREATE INDEX IF NOT EXISTS idx_target "
        "ON loan_applications (TARGET)"
    )

    connection.execute(
        "CREATE INDEX IF NOT EXISTS idx_contract_type "
        "ON loan_applications (NAME_CONTRACT_TYPE)"
    )

    row_count = connection.execute(
        "SELECT COUNT(*) FROM loan_applications"
    ).fetchone()[0]

print(f"Database created: {db_path}")
print(f"Rows stored: {row_count:,}")
print("SQL database setup complete!")
