# INSERT TABLES HERE (ALL RECORD MANAGEMENT ROWS)
CREATE DATABASE movie_ticketing_system;
USE movie_ticketing_system;

CREATE TABLE customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email_address VARCHAR(255) NOT NULL UNIQUE,
    mobile_number VARCHAR(20) NOT NULL UNIQUE,
    age TINYINT UNSIGNED NOT NULL
);

CREATE TABLE payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL, 
    ticket_paid ENUM('Paid', 'Pending') NOT NULL,
    date_paid DATE NULL,
    time_paid TIME NULL,
    CONSTRAINT fk_payment_customer
        FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
);

