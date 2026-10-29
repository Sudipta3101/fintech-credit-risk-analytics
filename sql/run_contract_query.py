
from pathlib import Path
import sqlite3

project_dir = Path(__file__).resolve().parent.parent
db_path = project_dir / "data" / "fintech_loan_analysis.db"
sql_path = project_dir / "sql" / "contract_type_analysis.sql"

with sqlite3.connect(db_path) as connection:
    query = sql_path.read_text(encoding="utf-8")
    cursor = connection.execute(query)

    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()

print("\nCONTRACT TYPE ANALYSIS")
print("-" * 75)
print(" | ".join(columns))
print("-" * 75)

for row in rows:
    print(" | ".join(str(value) for value in row))
