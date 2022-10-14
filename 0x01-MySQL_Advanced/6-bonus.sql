-- creates a stored procedure
DELIMITER $$
CREATE PROCEDURE AddBonus (
    in user_id INT,
    in project_name VARCHAR(250),
    in score FLOAT
    )
BEGIN
DECLARE pid INT;
IF NOT EXISTS (SELECT * FROM projects WHERE name = project_name) THEN
    INSERT INTO projects (name)
    VALUES (project_name);
END IF;
SELECT id INTO pid FROM projects WHERE name = project_name;
INSERT INTO corrections (user_id, project_id, score)
VALUES (user_id, pid, score);
END $$;
