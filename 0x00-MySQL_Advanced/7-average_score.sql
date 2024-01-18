-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student

DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE new_av FLOAT;

    SELECT AVG(score) INTO new_av FROM corrections WHERE user_id = user_id;
    UPDATE users SET average_score = new_av WHERE id = user_id;
END //
DELIMITER ;
