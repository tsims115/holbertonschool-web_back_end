-- creates a stored procedure
DELIMITER $$
CREATE PROCEDURE AddBonus (
    in user_id int,
    in project_name VARCHAR(250),
    in score float
    )
BEGIN
SET @pid = (SELECT projects.id WHERE projects.name = project_name);
IF NOT EXISTS @pid
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, @pid, score);
;
ENDIF;
IF EXISTS @pid
    UPDATE corrections
    SET corrections.score = score
    WHERE corrections.user_id = user_id
;
ENDIF;
END $$;