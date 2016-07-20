#!/bin/bash
sudo mysql_install_db --user=mysql >/dev/null 2>&1
sudo sed 's/password = .*/password = /g' -i /etc/mysql/debian.cnf
sudo service mysql start
sudo mysql -uroot < /home/developer/geppetto/init.sql
/home/developer/workspace/geppetto/check_update.sh
cd /home/developer/workspace/org.geppetto.persistence
mvn install
mvn install
mvn exec:java -Dexec.mainClass="org.geppetto.persistence.util.DBTestData" -Dexec.classpathScope=runtime
cd /home/developer/workspace/org.geppetto/utilities/source_setup
python update_server.py
/home/developer/virgo/bin/startup.sh
