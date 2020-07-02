REPO_HOME="=REPO_DIR="
HOME_YCSB="=REPO_DIR=/ycsb-0.17.0"
BIN_YCSB=HOME_YCSB + "/bin"
SCRIPTS="=REPO_DIR=/scripts"

def getOutputFilename(base_dir, operation, dim, t, c) :
    filename = base_dir + "/output-" + operation
    if dim is not None:
        filename = filename + "-dim" + str(dim)

    if t is not None:
        filename = filename + "-throughput" + str(t)
    
    if c is not None:
        filename = filename + "-clients" + str(c)

    filename = filename + ".txt"
    return filename