SELECT * FROM customers LIMIT 5;

SELECT * FROM loans LIMIT 5;

SELECT housing, AVG(default_status) AS default_rate
FROM customers c JOIN loans l ON c.customer_id = l.customer_id
GROUP BY housing; 

SELECT employment, AVG(credit_amount)
FROM loans GROUP BY employment;

SELECT purpose, AVG(default_status) AS risk_rate
FROM loans GROUP BY purpose ORDER BY risk_rate DESC;