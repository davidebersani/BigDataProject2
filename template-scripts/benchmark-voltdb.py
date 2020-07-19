# Script for execute workload A on VoltDb with various parameters.
import sys
import commons

#voltdb_connection_string = "voltdb://127.0.0.1:21212/ycsb"
output_dir="=REPO_DIR=scripts/test-voltdb-all-scenario"

# Every record is 1KB (10 fields of 100B)
input_dim = [100000, 500000, 1000000, 3000000, 5000000]
throughput = [1000, 100000, 1000000]
clients=[10]
operationcount=100000 # Number of operation per thread

def delete_db(usage) :
    print("\n\n==> Removing db")
    if usage=="local-docker":
        command = "docker exec -it node1 sqlcmd --query=\"truncate table store\""
        commons.executeBashCommand(command)
    elif usage=="local":
            command = "/home/ec2-user/voltdb/bin/sqlcmd --query='truncate table store'"
            commons.executeBashCommand(command)
    else:
        print("Please, manually delete the db. This function is still not supported. Afther done, press Enter")
        input()


def laod_data(dim, usage) :
    # Execute workload a for every dim
    print("\n\n==> Loading data: " + str(dim) + " record")
    if usage=="local-docker":
        command = commons.BIN_YCSB + "/ycsb.sh load voltdb -P " + commons.HOME_YCSB + "/workloads/workloada -P " + commons.SCRIPTS + "/voltdb-prop > " + commons.getOutputFilename(output_dir, "Load", None, dim, None, None)
    elif usage=="local":
        command = commons.BIN_YCSB + "/ycsb.sh run voltdb -P " + commons.HOME_YCSB + "/workloads/workloada > " + commons.getOutputFilename(output_dir, "Run", None, dim, None, None)
    commons.executeBashCommand(command)

def run_workload(workload, dim, t, c, op, usage) :
    if usage=="local-docker":
        command = commons.BIN_YCSB + "/ycsb.sh run voltdb -P " + commons.HOME_YCSB + "/workloads/" + workload + " -P " + commons.SCRIPTS + "/voltdb-prop > " + commons.getOutputFilename(output_dir, "Run", workload, dim, t, c)
    elif usage=="local":
        command = commons.BIN_YCSB + "/ycsb.sh run voltdb -P " + commons.HOME_YCSB + "/workloads/" + workload + " > " + commons.getOutputFilename(output_dir, "Run", workload, dim, t, c)
    commons.executeBashCommand(command)

if len(sys.argv)<2 :
    print("Error, required parameter: ")
    print("- Usage: local or local-docker")
    print("Usage: py benchmark-voltdb-a.py <usage>")
    exit(1)

commons.createDirIfNotExists(output_dir)

for num_clients in clients:  
    for dim in input_dim:
        laod_data(dim, sys.argv[1])
        for t in throughput:
            print("\n==> Wordload A. Input dim: " + str(dim) + "; Throughput: " + str(t) + "; Clients: " + str(num_clients))
            run_workload("workloada", dim, t, num_clients, operationcount, sys.argv[1])
            print("\n==> Wordload B. Input dim: " + str(dim) + "; Throughput: " + str(t) + "; Clients: " + str(num_clients))
            run_workload("workloadb", dim, t, num_clients, operationcount, sys.argv[1])
            print("\n==> Wordload C. Input dim: " + str(dim) + "; Throughput: " + str(t) + "; Clients: " + str(num_clients))
            run_workload("workloadc", dim, t, num_clients, operationcount, sys.argv[1])
            print("\n==> Wordload E. Input dim: " + str(dim) + "; Throughput: " + str(t) + "; Clients: " + str(num_clients))
            run_workload("workloade", dim, t, num_clients, operationcount, sys.argv[1])
            print("\n==> Wordload F. Input dim: " + str(dim) + "; Throughput: " + str(t) + "; Clients: " + str(num_clients))
            run_workload("workloadf", dim, t, num_clients, operationcount, sys.argv[1])
        
        delete_db(sys.argv[1])
