
from pathlib import Path
import sqlite3

project_dir = Path(__file__).resolve().parent.parent
db_path = project_dir / "data" / "fintech_loan_analysis.db"
sql_path = project_dir / "sql" / "summary.sql"

with sqlite3.connect(db_path) as connection:
    query = sql_path.read_text(encoding="utf-8")
    cursor = connection.execute(query)

    columns = [item[0] for item in cursor.description]
    result = cursor.fetchone()

print("\nOVERALL LOAN APPLICATION SUMMARY")
print("-" * 65)

for name, value in zip(columns, result):
    print(f"{name}: {value}")
