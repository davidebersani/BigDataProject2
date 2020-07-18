#!/bin/sh
sudo pip install pathlib
sudo tar -zxvf voltdb-developer-9.3.1.tar.gz -C /opt
cd /opt
sudo mv voltdb-developer-9.3.1 voltdb
cd /home/ec2-user
sudo mkdir /usr/lib/jdk
sudo cp jdk-11.0.8_linux-x64_bin.tar.gz /usr/lib/jdk/jdk-11.0.8_linux-x64_bin.tar.gz
cd /usr/lib/jdk
sudo tar -zxvf jdk-11.0.8_linux-x64_bin.tar.gz
sudo rm jdk-11.0.8_linux-x64_bin.tar.gz
sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jdk/jdk-11.0.8/bin/java" 1010
sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jdk/jdk-11.0.8/bin/javac" 1010
sudo update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/lib/jdk/jdk-11.0.8/bin/javaws" 1010
cd /home/ec2-user
sudo mv javajdk.sh /etc/profile.d
unzip BigDataProject2-master.zip