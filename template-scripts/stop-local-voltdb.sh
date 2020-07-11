#!/bin/bash
line=$(head -n 1 id_voltdb.txt)
docker rm $line
rm -r id_voltdb.txt