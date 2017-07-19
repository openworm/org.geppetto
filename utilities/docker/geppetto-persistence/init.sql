create database geppetto;
create user 'user_name' identified by 'password';
grant all privileges on geppetto.* to 'geppetto_persistence_container'@'%' identified by 'password';
flush privileges;
