# Script for execute workload A on Mongodb with various parameters.
import subprocess
import plots

REPO_HOME="=REPO_DIR="
HOME_YCSB="=REPO_DIR=/ycsb-0.17.0"
BIN_YCSB=HOME_YCSB + "/bin"
SCRIPTS="=REPO_DIR=/scripts"
mongodb_connection_string = "mongodb://localhost:27017/ycsb?w=1"
output_dir="=REPO_DIR=/scripts/test-mongo-scenarioA"

def getOutputFilename(operation, dim, t) :
    filename = output_dir + "/output-" + operation
    if dim is not None:
        filename = filename + "-dim" + str(dim)

    if t is not None:
        filename = filename + "-throughput" + str(t)

    filename = filename + ".txt"
    return filename

def execute(command) :
    command = "sh -c \"" + command + "\""
    print("\n\n==> Execute: " + command)
    process = subprocess.call(command, shell=True)
    return process

def delete_db() :
    print("\n\n==> Removing db")
    command = "docker exec -it mongo mongo ycsb --eval \\\"db.dropDatabase()\\\""
    execute(command)

def laod_data(dim) :
    # Execute workload a for every dim
    print("\n\n==> Loading data: " + str(dim) + " record")
    command = BIN_YCSB + "/ycsb.sh load mongodb-async -s -P " + HOME_YCSB + "/workloads/workloada -p recordcount=" + str(dim) + " -p mongodb.url=" + mongodb_connection_string + " > " + getOutputFilename("Load", dim, None)
    execute(command)

def run_workload(dim, t) :
    command = BIN_YCSB + "/ycsb.sh run mongodb-async -s -P " + HOME_YCSB + "/workloads/workloada -p recordcount=" + str(dim) + " -target " + str(t) + " -p mongodb.url=" + mongodb_connection_string + " > " + getOutputFilename("Run", dim, t)
    execute(command)

# Every record is 1KB (10 fields of 100B)
input_dim = [1000, 10000, 100000, 500000, 1000000]
throughput = [100, 1000, 100000]
#clients=[]

for dim in input_dim:
    laod_data(dim)
    for t in throughput:
        print("\n==> Wordload A. Input dim: " + str(dim) + "; Throughput: " + str(t))
        laod_data(dim)
        run_workload(dim, t)
    
    delete_db()

plots.generateAndShowInputLatencyPlots(input_dim, throughput, "test-mongo-scenarioA")
plots.generateAndShowThroughputLatencyPlots(input_dim, throughput, "test-mongo-scenarioA")
