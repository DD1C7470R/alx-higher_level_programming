-- removes the databases hbtn_0c_0 on the server
USE mysql;
SELECT table_name FROM information_schema.tables WHERE table_schema = DATABASE();
