drop database geppetto;
create database geppetto;
drop user 'user_name'@'localhost';
flush privileges;
create user 'user_name' identified by 'password';
grant all privileges on geppetto.* to 'user_name'@'%' identified by 'password';
flush privileges;
