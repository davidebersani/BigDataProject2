# Script for execute workload A on Mongodb with various parameters.
import subprocess
import plots
import sys
import commons

postgres_connection_string = "jdbc:postgresql://127.0.0.1:5432/ycsb"
output_dir="=REPO_DIR=/scripts/test-postgres-scenarioA"

def execute(command) :
    command = "sh -c \"" + command + "\""
    print("\n\n==> Execute: " + command)
    process = subprocess.call(command, shell=True)
    return process

def delete_db(usage) :
    print("\n\n==> Removing db")
    # if usage=="local":
    #     command = "mongo ycsb --eval \\\"db.dropDatabase()\\\""
    #     execute(command)
    # else:
    print("Please, manually delete the db. This function is still not supported.")
    input()
    

def laod_data(dim) :
    # Execute workload a for every dim
    print("\n\n==> Loading data: " + str(dim) + " record")
    command = commons.BIN_YCSB + "/ycsb.sh load jdbc -s -P " + commons.HOME_YCSB + "/workloads/workloada -P " + commons.SCRIPTS + "/prop -p recordcount=" + str(dim) + " -p db.url=" + postgres_connection_string + " > " + commons.getOutputFilename(output_dir, "Load", dim, None, None)
    execute(command)

def run_workload(dim, t, c, op) :
    command = commons.BIN_YCSB + "/ycsb.sh run jdbc -s -P " + commons.HOME_YCSB + "/workloads/workloada -P " + commons.SCRIPTS + "/prop -p recordcount=" + str(dim) + " -threads " + str(c) +" -target " + str(t) + " -p db.url=" + postgres_connection_string + " -p operationcount=" + str(op) + " > " + commons.getOutputFilename(output_dir, "Run", dim, t, c)
    execute(command)


if len(sys.argv)<2 :
    print("Error, required parameter: ")
    print("- Usage: local or remote or local-docker")
    print("Usage: py benchmark-mongodb-a.py <usage>")
    exit(1)


# Every record is 1KB (10 fields of 100B)
input_dim = [100000, 500000, 1000000, 3000000, 5000000]
throughput = [1000, 100000, 1000000]
clients=[10]
operationcount=100000 # Number of operation per thread


print("==> Before running create the table! See https://github.com/brianfrankcooper/YCSB/tree/master/jdbc")
for num_clients in clients:  
    for dim in input_dim:
        laod_data(dim)
        for t in throughput:
            print("\n==> Wordload A. Input dim: " + str(dim) + "; Throughput: " + str(t) + "; Clients: " + str(num_clients))
            run_workload(dim, t, num_clients, operationcount)
        
        delete_db(sys.argv[1])

# PROSSIMI PASSI: AGGIUNGERE ITERAZIONE SUI CLIENT.

# plots.generateAndShowInputLatencyPlots(input_dim, throughput, clients, "test-postgres-scenarioA")
# plots.generateAndShowThroughputLatencyPlots(input_dim, throughput, clients, "test-postgres-scenarioA")
