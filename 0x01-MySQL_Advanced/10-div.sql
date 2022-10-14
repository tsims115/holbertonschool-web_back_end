-- Creates funstion SafeDiv that divides first by second number
DELIMITER $$
CREATE FUNCTION SafeDiv(n1 int, n2 int)
RETURNS FLOAT
BEGIN
    IF n2 = 0 THEN
    RETURN 0;
    END IF;
RETURN n1 / n2;
END $$;
