# Script for execute workload A on Mongodb with various parameters.
import subprocess
# import plots
import sys

REPO_HOME="=REPO_DIR="
HOME_YCSB="=REPO_DIR=/ycsb-0.17.0"
BIN_YCSB=HOME_YCSB + "/bin"
SCRIPTS="=REPO_DIR=/scripts"
mongodb_connection_string = "mongodb://localhost:27017/ycsb?w=1"
output_dir="=REPO_DIR=/scripts/test-mongo-scenarioA"

def getOutputFilename(operation, dim, t, c) :
    filename = output_dir + "/output-" + operation
    if dim is not None:
        filename = filename + "-dim" + str(dim)

    if t is not None:
        filename = filename + "-throughput" + str(t)
    
    if c is not None:
        filename = filename + "-clients" + str(c)

    filename = filename + ".txt"
    return filename

def execute(command) :
    command = "sh -c \"" + command + "\""
    print("\n\n==> Execute: " + command)
    process = subprocess.call(command, shell=True)
    return process

def delete_db(usage) :
    print("\n\n==> Removing db")
    if usage=="local-docker":
        command = "docker exec -it mongo mongo ycsb --eval \\\"db.dropDatabase()\\\""
        execute(command)
    elif usage=="local":
            command = "mongo ycsb --eval \\\"db.dropDatabase()\\\""
            execute(command)
    else:
        print("Please, manually delete the db. This function is still not supported.")
        input()
    

def laod_data(dim) :
    # Execute workload a for every dim
    print("\n\n==> Loading data: " + str(dim) + " record")
    command = BIN_YCSB + "/ycsb.sh load mongodb-async -s -P " + HOME_YCSB + "/workloads/workloada -p recordcount=" + str(dim) + " -p mongodb.url=" + mongodb_connection_string + " > " + getOutputFilename("Load", dim, None, None)
    execute(command)

def run_workload(dim, t, c) :
    command = BIN_YCSB + "/ycsb.sh run mongodb-async -s -P " + HOME_YCSB + "/workloads/workloada -p recordcount=" + str(dim) + " -threads " + str(c) +" -target " + str(t) + " -p mongodb.url=" + mongodb_connection_string + " > " + getOutputFilename("Run", dim, t, c)
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

for num_clients in clients:  
    for dim in input_dim:
        laod_data(dim)
        for t in throughput:
            print("\n==> Wordload A. Input dim: " + str(dim) + "; Throughput: " + str(t) + "; Clients: " + str(num_clients))
            run_workload(dim, t, num_clients)
        
        delete_db(sys.argv[1])

# PROSSIMI PASSI: AGGIUNGERE ITERAZIONE SUI CLIENT.

# plots.generateAndShowInputLatencyPlots(input_dim, throughput, clients, "test-mongo-scenarioA")
# plots.generateAndShowThroughputLatencyPlots(input_dim, throughput, clients, "test-mongo-scenarioA")
