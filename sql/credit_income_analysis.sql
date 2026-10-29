
WITH applicant_ratios AS (
    SELECT
        TARGET,
        1.0 * AMT_CREDIT / AMT_INCOME_TOTAL
            AS credit_income_ratio
    FROM loan_applications
    WHERE AMT_INCOME_TOTAL > 0
      AND AMT_CREDIT IS NOT NULL
),
banded_applicants AS (
    SELECT
        TARGET,
        CASE
            WHEN credit_income_ratio <= 2
                THEN 'Up to 2x'
            WHEN credit_income_ratio <= 4
                THEN 'Above 2x to 4x'
            WHEN credit_income_ratio <= 6
                THEN 'Above 4x to 6x'
            WHEN credit_income_ratio <= 10
                THEN 'Above 6x to 10x'
            ELSE 'Above 10x'
        END AS credit_income_band
    FROM applicant_ratios
)
SELECT
    credit_income_band,
    COUNT(*) AS total_applications,
    SUM(CASE WHEN TARGET = 1 THEN 1 ELSE 0 END)
        AS applications_with_difficulties,
    ROUND(
        100.0 * SUM(CASE WHEN TARGET = 1 THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS difficulty_rate_pct
FROM banded_applicants
GROUP BY credit_income_band
ORDER BY
    CASE credit_income_band
        WHEN 'Up to 2x' THEN 1
        WHEN 'Above 2x to 4x' THEN 2
        WHEN 'Above 4x to 6x' THEN 3
        WHEN 'Above 6x to 10x' THEN 4
        WHEN 'Above 10x' THEN 5
    END;
