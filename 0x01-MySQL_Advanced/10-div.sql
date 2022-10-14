-- Creates funstion SafeDiv that divides first by second number
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv (n1 int, n2 int)
RETURNS FLOAT DETERMINISTIC;
BEGIN
    IF n2 = 0 THEN
    RETURN 0;
    ELSE
    RETURN n1 / n2;
    END IF;
END $$;
