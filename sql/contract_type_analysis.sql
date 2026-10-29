
SELECT
    NAME_CONTRACT_TYPE AS contract_type,
    COUNT(*) AS total_applications,
    SUM(CASE WHEN TARGET = 1 THEN 1 ELSE 0 END)
        AS applications_with_difficulties,
    ROUND(
        100.0 * SUM(CASE WHEN TARGET = 1 THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS difficulty_rate_pct
FROM loan_applications
GROUP BY NAME_CONTRACT_TYPE
ORDER BY difficulty_rate_pct DESC;
