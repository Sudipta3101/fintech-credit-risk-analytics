
SELECT
    COUNT(*) AS total_applications,
    SUM(CASE WHEN TARGET = 1 THEN 1 ELSE 0 END)
        AS applications_with_difficulties,
    SUM(CASE WHEN TARGET = 0 THEN 1 ELSE 0 END)
        AS applications_without_recorded_difficulties,
    ROUND(
        100.0 * SUM(CASE WHEN TARGET = 1 THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS difficulty_rate_pct
FROM loan_applications;
