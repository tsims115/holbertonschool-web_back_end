-- Creates a view need_meeting lists all students with score under 80
DELIMITER $$
CREATE VIEW need_meeting AS SELECT name FROM students WHERE score < 80;
END $$;
