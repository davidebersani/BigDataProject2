#!/bin/bash
docker pull voltdb/voltdb-community:latest
if [ $# -eq 0 ] 
then
    echo 'Inserire numero di nodi nel cluster di voltdb che si vogliono creare'
else
    docker network create -d bridge voltLocalCluster
    host=""
    for (( c=1; c<=$1; c++ ))
    do
        if [ $c -ne $1 ]
        then
            host_ele+="node$c,"
        else
            host_ele+="node$c"
        fi
    done
    for (( c=1; c<=$1; c++ ))
    do
        docker run -d -P -e HOST_COUNT=$1 -e HOSTS=$host_ele --name=node$c --network=voltLocalCluster voltdb/voltdb-community:latest >> id_voltdb.txt
    done
fi