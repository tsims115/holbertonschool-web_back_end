-- creates a stored procedure
DELIMITER $$
CREATE PROCEDURE AddBonus (
    in user_id int,
    in project_name VARCHAR(250),
    in score float
    )
BEGIN
IF NOT EXISTS (SELECT id FROM projects WHERE name = project_name) THEN
    INSERT INTO projects (name)
    VALUES (project_name);
ENDIF;
INSERT INTO corrections (user_id, project_id, score)
VALUES (user_id, project_name, score);
END $$;
