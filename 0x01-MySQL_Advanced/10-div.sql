-- Creates funstion SafeDiv that divides first by second number
DELIMITER $$
CREATE FUNCTION SafeDiv (n1 int, n2 int)
RETURNS int;
    IF n2 = 0 THEN
    RETURN 0
    ELSE
    RETURN n1 / n2;
    END IF;
END $$;
