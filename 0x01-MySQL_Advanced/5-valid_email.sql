-- creates a trigger that resets email attribute
DELIMITER $$
CREATE TRIGGER v_email AFTER UPDATE of email ON users
FOR EACH ROW
BEGIN
IF NEW.email != OLD.email
THEN
    UPDATE users
    SET valid_email = 0
    WHERE email = NEW.email
END IF;
END $$;
