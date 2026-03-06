CREATE TABLE IF NOT EXISTS ecommerce_transactions (
    transaction_id        VARCHAR PRIMARY KEY,
    customer_id           VARCHAR,
    product_id            VARCHAR,
    product_category      VARCHAR,
    payment_method        VARCHAR,
    order_timestamp       TIMESTAMP,
    quantity              INTEGER,
    price                 NUMERIC,
    total_amount          NUMERIC,
    city                  VARCHAR,
    country               VARCHAR
);

CREATE VIEW ecommerce_sales_summary AS
SELECT
    country,
    product_category,
    COUNT(*)          AS transaction_count,
    SUM(total_amount) AS total_revenue
FROM ecommerce_transactions
GROUP BY country, product_category;
