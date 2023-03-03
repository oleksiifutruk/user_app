CREATE TABLE IF NOT EXISTS users(
 id BIGSERIAL NOT NULL PRIMARY KEY,
 first_name VARCHAR(50) NOT NULL,
 last_name VARCHAR(50),
 gender VARCHAR(12),
 age int,
 city VARCHAR(50),
 birth_day DATE,
 premium boolean,
 ip VARCHAR(50)
);



