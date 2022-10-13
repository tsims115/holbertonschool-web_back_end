CREATE TRIGGER ins_sum BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
UPDATE items
SET quantity = quantity - 1
WHERE NEW.item_name = name
;