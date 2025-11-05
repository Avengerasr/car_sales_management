
-- DATABASE: Car Sales Management System

CREATE DATABASE IF NOT EXISTS car_sales_db;
USE car_sales_db;


-- 1️ TABLE: Car_Brand (Stores car company details)

CREATE TABLE Car_Brand (
    brand_id INT AUTO_INCREMENT PRIMARY KEY,
    brand_name VARCHAR(50) UNIQUE NOT NULL,
    country VARCHAR(50)
);


-- 2️ TABLE: Car_Model (Stores car models and specifications)

CREATE TABLE Car_Model (
    model_id INT AUTO_INCREMENT PRIMARY KEY,
    brand_id INT,
    model_name VARCHAR(50) NOT NULL,
    fuel_type ENUM('Petrol', 'Diesel', 'Electric', 'Hybrid'),
    transmission ENUM('Manual', 'Automatic'),
    price DECIMAL(10,2),
    stock INT DEFAULT 0,
    FOREIGN KEY (brand_id) REFERENCES Car_Brand(brand_id)
);


-- 3️ TABLE: Customer

CREATE TABLE Customer (
    cust_id INT AUTO_INCREMENT PRIMARY KEY,
    cust_name VARCHAR(50) NOT NULL,
    contact VARCHAR(15) UNIQUE,
    address VARCHAR(100),
    email VARCHAR(50) UNIQUE
);

-- 4 TABLE: Sales

CREATE TABLE Sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    cust_id INT NOT NULL,
    model_id INT NOT NULL,
    sale_date DATE DEFAULT (CURRENT_DATE),
    quantity INT CHECK (quantity > 0),
    total_amount DECIMAL(12,2),
    FOREIGN KEY (cust_id) REFERENCES Customer(cust_id),
    FOREIGN KEY (model_id) REFERENCES Car_Model(model_id)
);


-- 5️ TABLE: Payment

CREATE TABLE Payment (
    pay_id INT AUTO_INCREMENT PRIMARY KEY,
    sale_id INT,
    payment_mode ENUM('Cash', 'Credit Card', 'Online Transfer'),
    payment_status ENUM('Pending', 'Completed') DEFAULT 'Pending',
    FOREIGN KEY (sale_id) REFERENCES Sales(sale_id)
);

-- SAMPLE DATA

INSERT INTO Car_Brand (brand_name, country)
VALUES ('Maruti Suzuki', 'India'),
       ('Hyundai', 'South Korea'),
       ('Honda', 'Japan');

INSERT INTO Car_Model (brand_id, model_name, fuel_type, transmission, price, stock)
VALUES (1, 'Swift', 'Petrol', 'Manual', 600000, 10),
       (2, 'i20', 'Petrol', 'Automatic', 850000, 8),
       (3, 'City', 'Diesel', 'Manual', 1200000, 5);

INSERT INTO Customer (cust_name, contact, address, email)
VALUES ('Anushri', '9876543210', 'Nagpur', 'anushri@example.com'),
       ('Riya', '9123456789', 'Pune', 'riya@example.com');

INSERT INTO Sales (cust_id, model_id, quantity, total_amount)
VALUES (1, 1, 1, 600000);

INSERT INTO Payment (sale_id, payment_mode, payment_status)
VALUES (1, 'Online Transfer', 'Completed');

-- QUERIES 

-- 1️ Display all available cars
SELECT model_name, price, stock FROM Car_Model;

-- 2️ List all customers
SELECT cust_name, contact, city FROM Customer;

-- 3️ Join (Customer + Sales + Car_Model)
SELECT c.cust_name, cm.model_name, s.total_amount, s.sale_date
FROM Sales s
JOIN Customer c ON s.cust_id = c.cust_id
JOIN Car_Model cm ON s.model_id = cm.model_id;

-- 4️ Update stock after sale
UPDATE Car_Model SET stock = stock - 1 WHERE model_id = 1;

-- 5️ Delete a customer (if no sale linked)
DELETE FROM Customer WHERE cust_id = 2;

-- 6 Aggregate: Total Sales per Brand
SELECT b.brand_name, SUM(s.total_amount) AS Total_Sales
FROM Sales s
JOIN Car_Model m ON s.model_id = m.model_id
JOIN Car_Brand b ON m.brand_id = b.brand_id
GROUP BY b.brand_name;

-- 7️ Create a View for All Sales Summary
CREATE OR REPLACE VIEW v_sales_summary AS
SELECT s.sale_id, c.cust_name, m.model_name, s.quantity, s.total_amount, p.payment_mode, p.payment_status
FROM Sales s
JOIN Customer c ON s.cust_id = c.cust_id
JOIN Car_Model m ON s.model_id = m.model_id
JOIN Payment p ON s.sale_id = p.sale_id;

-- 8️ Index on Model name for faster search
CREATE INDEX idx_model_name ON Car_Model(model_name);

-- 9️ Demonstrate Sequence-like Auto Increment
INSERT INTO Sales (cust_id, model_id, quantity, total_amount)
VALUES (1, 2, 1, 850000);

-- 10 Retrieve from View
SELECT * FROM v_sales_summary;
