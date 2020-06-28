import os
import matplotlib.pyplot as plt 
import re

def generateAndShowInputLatencyPlots(input_dim, throughputs, source) :

    for t in throughputs:
        # Generate plot Input dim / latency for every throughput value
        x_read=[]
        y_read=[]
        x_update=[]
        y_update=[]
        for dim in input_dim:
            cur_path = os.path.dirname(__file__)
            cur_path = os.path.join(cur_path, source)
            # new_path = os.path.join(cur_path, source ,"output-Run-dim" + str(dim) +".txt")
            # new_path = os.path.relpath("\\output\\test-mongo-scenarioA\\outputRun-dim" + str(dim) +".txt", cur_path)
            for filename in os.listdir(cur_path):
                if re.search("^output-Run-dim" + str(dim) + "-throughput" + str(t)  + "\.txt$", filename) :
                    new_path = os.path.join(cur_path,filename)
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
        plt.title('Input dimention / latency with Throughput=' + str(t)) 
        plt.legend()
        
        # function to show the plot 
        plt.show()
        
        #function for save result plt.show in file
        #plt.savefig('result.png')
