#!/bin/sh
sudo yum update -y
sudo echo "[mongodb-org-4.2]" | sudo tee -a /etc/yum.repos.d/mongodb-org-4.2.repo
sudo echo "name=MongoDB Repository" | sudo tee -a  /etc/yum.repos.d/mongodb-org-4.2.repo
sudo echo "baseurl=https://repo.mongodb.org/yum/amazon/2013.03/mongodb-org/4.2/x86_64/" | sudo tee -a  /etc/yum.repos.d/mongodb-org-4.2.repo
sudo echo "gpgcheck=1" | sudo tee -a  /etc/yum.repos.d/mongodb-org-4.2.repo
sudo echo "enabled=1" | sudo tee -a  /etc/yum.repos.d/mongodb-org-4.2.repo
sudo echo "gpgkey=https://www.mongodb.org/static/pgp/server-4.2.asc" | sudo tee -a  /etc/yum.repos.d/mongodb-org-4.2.repo
sudo yum install -y mongodb-org
sudo chkconfig mongod on
sudo service mongod start