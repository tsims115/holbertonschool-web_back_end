--- creates table of user with id, email, name
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(250) UNIQUE NOT NULL,
    name VARCHAR(250),
    PRIMARY KEY (id)
);
