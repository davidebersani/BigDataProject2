from pathlib import Path
import subprocess

REPO_HOME="=REPO_DIR="
HOME_YCSB="=REPO_DIR=/ycsb-0.17.0"
BIN_YCSB=HOME_YCSB + "/bin"
SCRIPTS="=REPO_DIR=/scripts"

def executeBashCommand(command) :
    command = "sh -c \"" + command + "\""
    print("\n\n==> Execute: " + command)
    process = subprocess.call(command, shell=True)
    return process


def getOutputFilename(base_dir, operation, workload, dim, t, c) :
    filename = base_dir + "/output-" + operation
    if workload is not None:
        filename = filename + "-" + str(workload)

    if dim is not None:
        filename = filename + "-dim" + str(dim)

    if t is not None:
        filename = filename + "-throughput" + str(t)
    
    if c is not None:
        filename = filename + "-clients" + str(c)

    filename = filename + ".txt"
    return filename

def createDirIfNotExists(path) :
    executeBashCommand("mkdir -p " + path)