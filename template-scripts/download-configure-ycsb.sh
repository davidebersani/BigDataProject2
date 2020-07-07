#!/bin/bash
source =REPO_DIR=/scripts/common.sh

echo "==> Downlaod YCSB v. 0.17.0"
curl -O --location https://github.com/brianfrankcooper/YCSB/releases/download/0.17.0/ycsb-0.17.0.tar.gz
echo "==> Extracting..."
tar xfvz ycsb-0.17.0.tar.gz --directory $REPO_HOME
rm -r ycsb-0.17.0.tar.gz
curl -O --location https://jdbc.postgresql.org/download/postgresql-42.2.14.jar
mv postgresql-42.2.14.jar $HOME_YCSB/jdbc-binding/lib/
rm $HOME_YCSB/workloads/*
mv =REPO_DIR=/workloads/* $HOME_YCSB/workloads/