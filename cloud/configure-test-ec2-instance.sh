#!/bin/sh
sudo yum install -y java-1.8.0-openjdk python34 python34-pip
sudo yum remove -y java-1.7.0-openjdk
export JAVA_HOME=/usr/lib/jvm/jre-1.8.0/