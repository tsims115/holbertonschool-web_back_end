-- Creates a trigger that updates the table items
CREATE TRIGGER ins_sum BEFORE INSERT ON orders
BEGIN
UPDATE items
SET quantity = quantity - 1
WHERE NEW.item_name = name
;