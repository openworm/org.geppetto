create database geppetto;
create user 'user_name' identified by 'password';
grant all privileges on geppetto.* to 'user_name'@'%' identified by 'password';
flush privileges;
