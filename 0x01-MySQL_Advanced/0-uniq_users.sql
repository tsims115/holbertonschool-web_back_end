--- creaetes table of user with id, email, name
CREATE TABLE users (
    id int NOT NULL AUTOINCREMENT PRIMARY KEY,
    email VARCHAR(250),
    name VARCHAR(250)
) IF NOT EXISTS;
