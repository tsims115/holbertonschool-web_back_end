-- creates a trigger that resets email attribute
DELIMITER $$
CREATE TRIGGER v_email AFTER UPDATE ON users
FOR EACH ROW
BEGIN
IF !(NEW.email <=> OLD.email) THEN
    update users
    SET valid_email = 0
    WHERE email = NEW.email;
END IF;
END $$;
