#!/bin/bash
echo "==> Downlaod YCSB v. 0.17.0"
curl -O --location https://github.com/brianfrankcooper/YCSB/releases/download/0.17.0/ycsb-0.17.0.tar.gz
echo "==> Extracting..."
tar xfvz ycsb-0.17.0.tar.gz