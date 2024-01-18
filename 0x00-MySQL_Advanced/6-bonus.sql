-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

DELIMITER // 
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
  DECLARE project_exist BOOLEAN;
  SELECT EXISTS(SELECT 1 FROM projects WHERE name = project_name) INTO project_exist;
  
  IF NOT project_exist THEN 
    INSERT INTO projects (name) VALUES (project_name);
  END IF;
  
  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);

END;
// DELIMITER;
