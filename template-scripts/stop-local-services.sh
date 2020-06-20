#!/bin/bash
# Script for start services on local machine. 
# This configuration is useful for first tests and benchmarks.
source =REPO_DIR=/scripts/common.sh

docker-compose -f $REPO_HOME/services.yml down -v