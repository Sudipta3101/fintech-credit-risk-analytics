# FinTech Credit Risk & Loan Application Analytics

## Project Overview
This project explores applicant characteristics and historical repayment-difficulty outcomes using Python. The goal is to identify patterns across financial indicators and applicant segments and communicate findings through clear, business-focused analysis.

## Business Objective
Analyze historical loan application data to understand how recorded repayment-difficulty rates vary by:
- Credit-to-income ratio bands
- Contract type
- Annual-income bands

## Dataset
- **Source:** Home Credit Default Risk dataset from Kaggle
- **File used:** `application_train.csv`
- **Records:** 307,511
- **Columns:** 122

The `TARGET` field indicates whether repayment difficulties were recorded under the dataset's definition. This project analyzes historical associations; it does not predict an individual's future repayment behavior.

## Tools
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Jupyter Notebook
- Excel and Power BI (planned project extensions)

## Work Completed
- Inspected dataset structure, data types, and missing values
- Summarized key financial variables
- Compared applicants by recorded repayment-difficulty outcome
- Created exploratory credit-to-income, contract-type, and income-band analyses
- Generated charts and exported a consolidated findings table

## Preliminary Findings
- The 2–4x credit-to-income band had the highest observed repayment-difficulty rate among the defined ratio bands (8.87%).
- Cash-loan applicants had a higher observed rate (8.35%) than revolving-loan applicants (5.48%).
- The above-3L income band had the lowest observed rate among the defined income bands (5.95%).

These are descriptive results from this dataset and do not establish causation.

## Limitations
- The analysis uses application-level data and should not be described as a live loan portfolio.
- The file alone does not establish current outstanding balances or month-by-month repayment trends.
- Missing values and extreme financial values require further investigation.
- Income-band monetary units must be verified against the dataset documentation before being labelled as a specific currency.
- The exploratory bands used in this project are not official lending thresholds.

## Project Status
**In progress.** Further work will include validation, improved reporting, and a Power BI dashboard.

## Responsible Use
This analysis is for learning and exploratory reporting. The findings should not be used alone to make lending decisions about individuals.