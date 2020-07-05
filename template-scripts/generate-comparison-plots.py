import plots
import sys

input_dim = [100000, 500000, 1000000, 3000000, 5000000]
throughput = [1000, 100000, 1000000]
clients=[10]

if len(sys.argv)<3 :
    print("Error, required parameter: ")
    print("- sources: name of the directories contained in scripts dir where the output reports are.")
    print("- workload: name of the workload.")
    print("Usage: py generate-singledb-plots.py <source1> <source2> .... <source n> <workload>")
    exit(1)

sources = []
for i in range(1,len(sys.argv)-1):
    sources.append(sys.argv[i])

workload = sys.argv[len(sys.argv)-1]
plots.generateAndShowInputLatencyPlotsComparison(input_dim, throughput, clients, sources, workload)
plots.generateAndShowThroughputLatencyPlotsComparison(input_dim, throughput, clients, sources, workload)
