#!/bin/bash
mkdir -p ${MYSQL_DATA_DIR}
mkdir -p ${MYSQL_RUN_DIR}
mkdir -p ${MYSQL_LOG_DIR}
sed 's/password = .*/password = /g' -i /etc/mysql/debian.cnf
mysql_install_db --user=mysql >/dev/null 2>&1
service mysql start
mysql -uroot < /home/developer/geppetto/init.sql
