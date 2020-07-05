import plots
import sys

input_dim = [100000, 500000, 1000000, 3000000, 5000000]
throughput = [1000, 100000, 1000000]
clients=[10]

if len(sys.argv)<2 :
    print("Error, required parameter: ")
    print("- source-dir: name of the directory contained in scripts dir where the output reports are.")
    print("Usage: py generate-singledb-plots.py <source-dir>")
    exit(1)

plots.generateAndShowInputLatencyPlots(input_dim, throughput, clients, sys.argv[1])
plots.generateAndShowThroughputLatencyPlots(input_dim, throughput, clients, sys.argv[1])