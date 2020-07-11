#!/bin/bash
line=$(head -n 1 id_voltdb.txt)
docker stop $line
rm -r id_voltdb.txt