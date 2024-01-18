--script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student 

DELIMITER // 
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
  DECLARE new_average FLOAT;
  SELECT AVG(score) FROM corrections WHERE user_id = user_id INTO new_average;
  
  UPDATE  users SET average_score = new_average WHERE id = user_id;

END;
// DELIMITER;
