CREATE DATABASE solodkov_hw_13;
use solodkov_hw_13;

CREATE TABLE price_rate
(
    id    INT PRIMARY KEY,
    value INT,
    CHECK ( value <= 100 )
);

CREATE TABLE customer
(
    id         INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name  VARCHAR(50)
);

CREATE TABLE driver
(
    id         INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name  VARCHAR(50)
);

CREATE TABLE tariff
(
    id          INT PRIMARY KEY,
    description VARCHAR(250)
);

CREATE TABLE car
(
    id        INT PRIMARY KEY,
    tariff_id INT NOT NULL,
    FOREIGN KEY (tariff_id) REFERENCES tariff (id)

);

CREATE TABLE shift
(
    id        INT PRIMARY KEY,
    driver_id INT NOT NULL,
    car_id    INT NOT NULL,
    FOREIGN KEY (driver_id) REFERENCES driver (id),
    FOREIGN KEY (car_id) REFERENCES car (id)

);

CREATE TABLE review
(
    id   INT PRIMARY KEY,
    body VARCHAR(250)
);

CREATE TABLE review_reason
(
    id     INT PRIMARY KEY,
    reason VARCHAR(250)
);

CREATE TABLE review2reason
(
    review_id INT NOT NULL,
    reason_id INT NOT NULL,
    FOREIGN KEY (review_id) REFERENCES review (id),
    FOREIGN KEY (reason_id) REFERENCES review_reason (id),
    UNIQUE (review_id, reason_id)
);

CREATE TABLE taxi_order
(
    id          INT PRIMARY KEY,
    driver_id   INT NOT NULL,
    customer_id INT NOT NULL,
    price_rate_id int NOT NULL ,
    tariff_id int not null,
    review_id int NOT NULL ,
    FOREIGN KEY (driver_id) REFERENCES driver (id),
    FOREIGN KEY (customer_id) REFERENCES customer (id),
    FOREIGN KEY (price_rate_id) REFERENCES price_rate (id),
    FOREIGN KEY (tariff_id) REFERENCES tariff (id),
    FOREIGN KEY (review_id) REFERENCES review (id),
    UNIQUE (review_id)
);





