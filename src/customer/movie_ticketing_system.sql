CREATE DATABASE movie_ticketing_system;

CREATE TABLE customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email_address VARCHAR(255) NOT NULL UNIQUE,
    mobile_number VARCHAR(20) NOT NULL UNIQUE,
    age TINYINT UNSIGNED NOT NULL
);

INSERT INTO customer (customer_id, first_name, last_name, email_address, mobile_number, age) VALUES
    (1, 'Jess', 'Quinto', 'jquinto@gmail.com', '09335558364', 58),
    (2, 'Bettina', 'Castillo', 'bettcastillo012@gmail.com', '09285529459', 34),
    (3, 'Mikhaila', 'Yason', 'mikayason12@gmail.com', '09081224880', 20),
    (4, 'Phoebe', 'Pichay', 'pbAndJ@gmail.com', '09323231920', 19),
    (5, 'Ihriel', 'Lim', 'ihrielim@gmail.com', '09193323643', 17),
    (6, 'Theo', 'Gallego', 'gallego.theo@gmail.com', '09291234117', 26),
    (7, 'Thomas', 'Guevarra', 'guevarrathomas@gmail.com', '09085554880', 63),
    (8, 'Bettina', 'Nicolas', 'bnnicolas@gmail.com', '09289670915', 47),
    (9, 'Mariel', 'Santiago', 'marielll@gmail.com', '09337452445', 31),
    (10, 'Aaron', 'Santiago', 'santiago12345@gmail.com', '09334442445', 31);