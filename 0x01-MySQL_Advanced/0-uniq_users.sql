-- creates table of user with id, email, name
CREATE TABLE users (
    id int NOT NULL AUTO_INCREMENT,
    email varchar(250) UNIQUE NOT NULL,
    name varchar(250),
    PRIMARY KEY (id)
) IF NOT EXISTS;
