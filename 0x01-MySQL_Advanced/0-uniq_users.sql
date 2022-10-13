--- creates table of user with id, email, name
CREATE TABLE users (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email varchar(250),
    name varchar(250)
) IF NOT EXISTS;
