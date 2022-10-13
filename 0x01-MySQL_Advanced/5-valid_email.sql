-- creates a trigger that resets email attribute
DELIMITER $$
CREATE TRIGGER v_email AFTER UPDATE of email ON users
FOR EACH ROW
BEGIN
if users.email = OLD.email
then
    UPDATE users
    SET valid_email = 1
    WHERE email = NEW.email
END IF;
END $$;
