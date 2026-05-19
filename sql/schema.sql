DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS customers;


CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    age INTEGER,
    sex VARCHAR(20),
    housing VARCHAR(50),
    job INTEGER
);

CREATE TABLE loans (
    loan_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    credit_amount NUMERIC,
    duration INTEGER,
    purpose VARCHAR(100),
    checking_status VARCHAR(50),
    saving_status VARCHAR(50),
    default_status INTEGER
);

