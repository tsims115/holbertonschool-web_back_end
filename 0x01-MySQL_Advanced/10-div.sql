-- Creates funstion SafeDiv that divides first by second number
CREATE FUNCTION SafeDiv (n1 int, n2 int)
IF n2 = 0 THEN
RETURNS 0;
END IF;
RETURNS n1 / n2;
