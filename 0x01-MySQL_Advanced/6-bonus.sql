-- creates a stored procedure
DELIMITER $$
CREATE PROCEDURE AddBonus (
    in user_id INT,
    in project_name VARCHAR(250),
    in score FLOAT
    )
BEGIN
SET pid := (SELECT id FROM projects WHERE name = project_name);
IF pid IS NULL THEN
    INSERT INTO projects (name)
    VALUES (project_name);
    SET pid := (SELECT id FROM projects WHERE name = project_name);
END IF;
INSERT INTO corrections (user_id, project_id, score)
VALUES (user_id, pid, score);
END $$;
