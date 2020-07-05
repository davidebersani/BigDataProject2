import plots
import sys

input_dim = [100000, 500000, 1000000, 3000000, 5000000]
throughput = [1000, 100000, 1000000]
clients=[10]

if len(sys.argv)<2 :
    print("Error, required parameter: ")
    print("- sources: name of the directories contained in scripts dir where the output reports are.")
    print("Usage: py generate-singledb-plots.py <sources>")
    exit(1)

sources = []
for i in range(1,len(sys.argv)):
    sources.append(sys.argv[i])

plots.generateAndShowInputLatencyPlotsComparison(input_dim, throughput, clients, sources)
plots.generateAndShowThroughputLatencyPlotsComparison(input_dim, throughput, clients, sources)