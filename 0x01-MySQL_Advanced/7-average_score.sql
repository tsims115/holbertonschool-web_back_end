-- Creates SP that computes and store the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (
    in user_id INT,
    )
BEGIN
    SET @avg_score :=
    SELECT AVG(score) FROM corrections WHERE user_id = user_id;
    UPDATE users
    SET average_score = @avg_score
    WHERE user_id = user_id;
END $$;
