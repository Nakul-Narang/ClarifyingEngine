-- Customers Table
CREATE TABLE IF NOT EXISTS customers(
   customer_id SERIAL PRIMARY KEY, 
   full_name VARCHAR(100) NOT NULL,
   email VARCHAR(100) UNIQUE NOT NULL,
   status VARCHAR(20) DEFAULT 'active',-- 'active','dormant','banned'
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
--Product Table
CREATE TABLE IF NOT EXISTS products(
   product_id SERIAL PRIMARY KEY,
   name VARCHAR(100) NOT NULL,
   category VARCHAR (50) NOT NULL,
   price DECIMAL(10,2) NOT NULL,
   stock_quantity INT DEFAULT 0);
