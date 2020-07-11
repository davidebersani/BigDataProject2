#!/bin/bash
line=$(head -n 1 id_voltdb.txt)
docker stop $line
docker rm $line
rm -r id_voltdb.txt