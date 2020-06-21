# Script for execute workload A on Mongodb with various parameters.
import subprocess
import os
import matplotlib.pyplot as plt 

REPO_HOME="=REPO_DIR="
HOME_YCSB="=REPO_DIR=/ycsb-0.17.0"
BIN_YCSB=HOME_YCSB + "/bin"
SCRIPTS="=REPO_DIR=/scripts"
host = "http://localhost:27017"
output_dir="=REPO_DIR=/scripts/test-mongo-scenarioA"

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
    print("\n\n==> Loading data")
    command = BIN_YCSB + "/ycsb.sh load mongodb-async -s -P " + HOME_YCSB + "/workloads/workloada -p recordcount=" + str(dim) + " > " + output_dir + "/outputLoad-dim" + str(dim) +".txt"
    execute(command)

def run_workload(dim) :
    print("\n\n==> Executing workload with input dim" + str(dim))
    command = BIN_YCSB + "/ycsb.sh run mongodb-async -s -P " + HOME_YCSB + "/workloads/workloada -p recordcount=" + str(dim) + " > " + output_dir + "/outputRun-dim" + str(dim) +".txt"
    execute(command)

# Every record is 1KB (10 fields of 100B)
input_dim = [1000, 10000, 100000, 500000, 1000000]
#throughput = []
#clients=[]

for dim in input_dim:
    print("\n==> Wordload A. Input dim: " + str(dim))
    laod_data(dim)
    run_workload(dim)
    delete_db()

x_read=[]
y_read=[]
x_update=[]
y_update=[]
# Generate plot Input dim / latency
for dim in input_dim:
    cur_path = os.path.dirname(__file__)
    new_path = os.path.join(cur_path, "test-mongo-scenarioA","outputRun-dim" + str(dim) +".txt")
    # new_path = os.path.relpath("\\output\\test-mongo-scenarioA\\outputRun-dim" + str(dim) +".txt", cur_path)
    f = open(new_path, "r")
    for line in f:
        if "[READ], AverageLatency(us)," in line:
            parts = line.split("[READ], AverageLatency(us), ")
            num = float(parts[1])
            x_read.append(dim)
            y_read.append(num)
        else:
            if "[UPDATE], AverageLatency(us)," in line:
                parts = line.split("[UPDATE], AverageLatency(us),")
                num = float(parts[1])
                x_update.append(dim)
                y_update.append(num)
    f.close()

plt.plot(x_read, y_read, linewidth = 1, 
         marker='o', markerfacecolor='blue', markersize=5, label="READ") 
plt.plot(x_update, y_update, linewidth = 1, 
         marker='o', markerfacecolor='blue', markersize=5, label="UPDATE")  
# naming the x axis 
plt.xlabel('Input dimension') 
plt.xscale('log')
# naming the y axis 
plt.ylabel('Average latency (us)') 
  
# giving a title to my graph 
plt.title('Input dimention / latency') 
plt.legend()
  
# function to show the plot 
plt.show() 

