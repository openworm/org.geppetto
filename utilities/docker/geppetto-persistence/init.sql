create database geppetto;
create user 'user_name' identified by 'password';
grant all privileges on geppetto.* to 'guest1'@'%' identified by 'password';
flush privileges;
