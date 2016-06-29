#INITIAL HACKED UP SHELL SCRIPT

git clone https://github.com/openworm/org.geppetto.git
python org.geppetto/utilities/source_setup/setup.py .

mkdir -p ~/virgo/pickup
mkdir -p ~/virgo/usr

cd org.geppetto.model
sudo docker run -it --rm --name my-maven-project -v "$PWD":/usr/src/mymaven -v ~/.m2:/root/.m2 -w /usr/src/mymaven maven:3.2-jdk-7 mvn clean install
sudo cp target/classes/lib/* ~/virgo/usr ; sudo cp target/* ~/virgo/usr
cd ../org.geppetto.core
sudo docker run -it --rm --name my-maven-project -v "$PWD":/usr/src/mymaven -v ~/.m2:/root/.m2 -w /usr/src/mymaven maven:3.2-jdk-7 mvn clean install
sudo cp target/classes/lib/* ~/virgo/usr ; sudo cp target/* ~/virgo/usr
cd ../org.geppetto.model.neuroml
sudo docker run -it --rm --name my-maven-project -v "$PWD":/usr/src/mymaven -v ~/.m2:/root/.m2 -w /usr/src/mymaven maven:3.2-jdk-7 mvn clean install
sudo cp target/classes/lib/* ~/virgo/usr ; sudo cp target/* ~/virgo/usr
cd ../org.geppetto.model.swc
sudo docker run -it --rm --name my-maven-project -v "$PWD":/usr/src/mymaven -v ~/.m2:/root/.m2 -w /usr/src/mymaven maven:3.2-jdk-7 mvn clean install
sudo cp target/classes/lib/* ~/virgo/usr ; sudo cp target/* ~/virgo/usr
cd ../org.geppetto.simulation
sudo docker run -it --rm --name my-maven-project -v "$PWD":/usr/src/mymaven -v ~/.m2:/root/.m2 -w /usr/src/mymaven maven:3.2-jdk-7 mvn clean install
sudo cp target/classes/lib/* ~/virgo/usr ; sudo cp target/* ~/virgo/usr
cd ../org.geppetto.frontend
sudo docker run -it --rm --name my-maven-project -v "$PWD":/usr/src/mymaven -v ~/.m2:/root/.m2 -w /usr/src/mymaven maven:3.2-jdk-7 mvn clean install
sudo cp target/classes/lib/* ~/virgo/usr ; sudo cp target/* ~/virgo/usr
cd ../org.geppetto
sudo cp geppetto.plan ~/virgo/pickup

cd utilities/docker/virgo-tomcat-server-3.6.4-RELEASE-jre-7
sudo docker build -t slarson/virgo-tomcat-server:3.6.4-RELEASE-jre-7 .

sudo docker run --name="virgo-tomcat-server" --publish=8080:8080 -v ~/virgo/pickup:/home/virgo/pickup -v ~/virgo/usr:/home/virgo/repository/usr -t slarson/virgo-tomcat-server:3.6.4-RELEASE-jre-7
