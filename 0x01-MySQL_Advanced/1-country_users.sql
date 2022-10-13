-- creates table user
CREATE TABLE IF NOT EXISTS users (
    PRIMARY KEY (id),
    id int AUTO_INCREMENT NOT NULL,
    email varchar(250) NOT NULL UNIQUE,
    name varchar(250),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
