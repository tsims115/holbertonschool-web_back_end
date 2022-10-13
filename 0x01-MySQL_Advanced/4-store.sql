-- Creates a trigger that updates the table items
DELIMITER $$
CREATE TRIGGER ins_sum AFTER INSERT ON orders
FOR EACH ROW
BEGIN
UPDATE items
SET quantity = quantity - NEW.number
WHERE NEW.item_name = name;
END $$;