--- creates table of user with id, email, name
CREATE TABLE users (
    PRIMARY KEY (id),
    id int NOT NULL AUTO_INCREMENT,
    email varchar(250) unique NOT NULL,
    name varchar(250)
) IF NOT EXISTS;
