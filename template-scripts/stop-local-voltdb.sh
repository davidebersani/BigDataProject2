#!/bin/bash
input="id_voltdb.txt"
while IFS= read -r line
do
    docker stop $line
    docker rm $line
done < "$input"

rm -r id_voltdb.txt