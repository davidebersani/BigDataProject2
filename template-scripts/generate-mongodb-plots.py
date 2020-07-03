import plots

input_dim = [100000, 500000, 1000000, 3000000, 5000000]
throughput = [1000, 100000, 1000000]
clients=[10]

plots.generateAndShowInputLatencyPlots(input_dim, throughput, clients, "test-mongo-scenarioA")
plots.generateAndShowThroughputLatencyPlots(input_dim, throughput, clients, "test-mongo-scenarioA")