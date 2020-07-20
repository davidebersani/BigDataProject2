#!/bin/sh
sudo pip install pathlib
sudo tar -zxvf /home/ec2-user/voltdb-developer-9.3.1.tar.gz
sudo rm -r /home/ec2-user/voltdb-developer-9.3.1.tar.gz
sudo mv voltdb-developer-9.3.1 /home/ec2-user/voltdb
sudo yum install -y java-1.8.0
sudo yum remove -y java-1.7.0-openjdk