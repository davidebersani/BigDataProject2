import plots

input_dim = [100000, 500000, 1000000, 3000000, 5000000]
throughput = [1000, 100000, 1000000]
clients=[10]

plots.generateAndShowInputLatencyPlotsComparison(input_dim, throughput, clients, ["test-mongo-scenarioA", "test-postgres-scenarioA"])
plots.generateAndShowThroughputLatencyPlotsComparison(input_dim, throughput, clients, ["test-mongo-scenarioA", "test-postgres-scenarioA"])