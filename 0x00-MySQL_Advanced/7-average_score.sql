--script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student 
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER // 
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
  DECLARE new_average FLOAT;
  SELECT AVG(score) INTO new_average FROM corrections WHERE user_id = user_id;
  
  UPDATE  users SET average_score = new_average WHERE id = user_id;

END;
// DELIMITER;
