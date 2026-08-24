-- =====================================================
-- Retail Sales Analysis
-- PostgreSQL Portfolio Project
-- Dataset: Online Retail
-- =====================================================


-- 1. Preview the dataset
SELECT *
FROM online_retail
LIMIT 10;


-- 2. Total number of rows
SELECT COUNT(*) AS total_rows
FROM online_retail;


-- 3. Calculate sales for individual transactions
SELECT
    invoice_no,
    stock_code,
    description,
    quantity,
    unit_price,
    quantity * unit_price AS total_sales,
    invoice_date,
    customer_id,
    country
FROM online_retail
LIMIT 10;


-- 4. Total revenue
SELECT
    ROUND(SUM(quantity * unit_price), 2) AS total_revenue
FROM online_retail
WHERE quantity > 0
  AND unit_price > 0;


-- 5. Top 10 products by revenue
SELECT
    description,
    SUM(quantity) AS units_sold,
    ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM online_retail
WHERE quantity > 0
  AND unit_price > 0
  AND description IS NOT NULL
GROUP BY description
ORDER BY revenue DESC
LIMIT 10;


-- 6. Revenue by country
SELECT
    country,
    ROUND(SUM(quantity * unit_price), 2) AS total_revenue
FROM online_retail
WHERE quantity > 0
  AND unit_price > 0
GROUP BY country
ORDER BY total_revenue DESC;


-- 7. Monthly revenue trend
SELECT
    DATE_TRUNC('month', invoice_date) AS month,
    ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM online_retail
WHERE quantity > 0
  AND unit_price > 0
GROUP BY DATE_TRUNC('month', invoice_date)
ORDER BY month;


-- 8. Top 10 customers by spending
SELECT
    customer_id,
    ROUND(SUM(quantity * unit_price), 2) AS total_spent
FROM online_retail
WHERE quantity > 0
  AND unit_price > 0
  AND customer_id IS NOT NULL
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;


-- 9. Average order value
SELECT
    ROUND(AVG(order_total), 2) AS average_order_value
FROM (
    SELECT
        invoice_no,
        SUM(quantity * unit_price) AS order_total
    FROM online_retail
    WHERE quantity > 0
      AND unit_price > 0
    GROUP BY invoice_no
) AS orders;


-- 10. Top 10 countries by number of orders
SELECT
    country,
    COUNT(DISTINCT invoice_no) AS total_orders,
    ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM online_retail
WHERE quantity > 0
  AND unit_price > 0
GROUP BY country
ORDER BY total_orders DESC
LIMIT 10;