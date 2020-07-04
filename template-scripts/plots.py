import os
import matplotlib.pyplot as plt 
import re
import itertools

def generateAndShowInputLatencyPlots(input_dim, throughputs, clients, source) :

    for c in clients:
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
                    if re.search("^output-Run-dim" + str(dim) + "-throughput" + str(t) +"-clients" + str(c) + "\.txt$", filename) :
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
            plt.title('Input dimension / latency with Throughput=' + str(t) + " and " + str(c) + " clients") 
            plt.legend()
            
            # function to show the plot 
            plt.show()
            
            #function for save result plt.show in file
            #plt.savefig('result.png')

def generateAndShowThroughputLatencyPlots(input_dim, throughputs, clients, source) :

    for c in clients:
        for dim in input_dim:
            # Generate plot Throughput / latency for every dim value
            x_read=[]
            y_read=[]
            x_update=[]
            y_update=[]
            for t in throughputs:
                cur_path = os.path.dirname(__file__)
                cur_path = os.path.join(cur_path, source)
                # new_path = os.path.join(cur_path, source ,"output-Run-dim" + str(dim) +".txt")
                # new_path = os.path.relpath("\\output\\test-mongo-scenarioA\\outputRun-dim" + str(dim) +".txt", cur_path)
                for filename in os.listdir(cur_path):
                    if re.search("^output-Run-dim" + str(dim) + "-throughput" + str(t) +"-clients.*" + "\.txt$", filename) :
                        new_path = os.path.join(cur_path,filename)
                        f = open(new_path, "r")
                        for line in f:
                            if "[READ], AverageLatency(us)," in line:
                                parts = line.split("[READ], AverageLatency(us), ")
                                num = float(parts[1])
                                x_read.append(t)
                                y_read.append(num)
                            else:
                                if "[UPDATE], AverageLatency(us)," in line:
                                    parts = line.split("[UPDATE], AverageLatency(us),")
                                    num = float(parts[1])
                                    x_update.append(t)
                                    y_update.append(num)
                        f.close()

            plt.plot(x_read, y_read, linewidth = 1, 
                    marker='o', markerfacecolor='blue', markersize=5, label="READ") 
            plt.plot(x_update, y_update, linewidth = 1, 
                    marker='o', markerfacecolor='blue', markersize=5, label="UPDATE")  
            # naming the x axis 
            plt.xlabel('Throughput') 
            plt.xscale('log')
            # naming the y axis 
            plt.ylabel('Average latency (us)') 
            
            # giving a title to my graph 
            plt.title('Throughput / latency curve with Input dimension=' + str(dim) + " and " + str(c) + " clients") 
            plt.legend()
            
            # function to show the plot 
            plt.show()
            
            #function for save result plt.show in file
            #plt.savefig('result.png')

class Serie:

    def __init__(self, name):
        self.x = []
        self.y = []
        self.name = name

    def addPoint(self, x1, y1):
        self.x.append(x1)
        self.y.append(y1)

def generateAndShowInputLatencyPlotsComparison(input_dim, throughputs, clients, sources) :

    for c in clients:
        for t in throughputs:
            reads=[]
            updates=[]
            # Generate plot Input dim / latency for every throughput value
            for source in sources:
                read = Serie(source)
                update = Serie(source)
                for dim in input_dim:
                    cur_path = os.path.dirname(__file__)
                    cur_path = os.path.join(cur_path, source)
                    # new_path = os.path.join(cur_path, source ,"output-Run-dim" + str(dim) +".txt")
                    # new_path = os.path.relpath("\\output\\test-mongo-scenarioA\\outputRun-dim" + str(dim) +".txt", cur_path)
                    for filename in os.listdir(cur_path):
                        if re.search("^output-Run-dim" + str(dim) + "-throughput" + str(t) +"-clients" + str(c) + "\.txt$", filename) :
                            new_path = os.path.join(cur_path,filename)
                            f = open(new_path, "r")
                            for line in f:
                                if "[READ], AverageLatency(us)," in line:
                                    parts = line.split("[READ], AverageLatency(us), ")
                                    num = float(parts[1])
                                    read.addPoint(dim, num)
                                else:
                                    if "[UPDATE], AverageLatency(us)," in line:
                                        parts = line.split("[UPDATE], AverageLatency(us),")
                                        num = float(parts[1])
                                        update.addPoint(dim, num)
                            f.close()
                reads.append(read)
                updates.append(update)

            marker = itertools.cycle((',', '+', '.', 'o', '*', 's', 'x')) 
            for serie in reads:
                plt.plot(serie.x, serie.y, linewidth = 1, 
                        marker=next(marker), markerfacecolor='blue', markersize=5, label="READ - " + serie.name) 
            
            for serie in updates:
                plt.plot(serie.x, serie.y, linewidth = 1, 
                        marker=next(marker), markerfacecolor='blue', markersize=5, label="UPDATE - " + serie.name)  
            # naming the x axis 
            plt.xlabel('Input dimension') 
            plt.xscale('log')
            # naming the y axis 
            plt.ylabel('Average latency (us)') 
            
            # giving a title to my graph 
            plt.title('Input dimension / latency with Throughput=' + str(t) + " and " + str(c) + " clients") 
            plt.legend()
            
            # function to show the plot 
            plt.show()
            
            #function for save result plt.show in file
            #plt.savefig('result.png')

def generateAndShowThroughputLatencyPlotsComparison(input_dim, throughputs, clients, sources) :

    for c in clients:
        for dim in input_dim:
            # Generate plot Throughput / latency for every dim value
            reads=[]
            updates=[]
            for source in sources:
                read = Serie(source)
                update = Serie(source)
                for t in throughputs:
                    cur_path = os.path.dirname(__file__)
                    cur_path = os.path.join(cur_path, source)
                    # new_path = os.path.join(cur_path, source ,"output-Run-dim" + str(dim) +".txt")
                    # new_path = os.path.relpath("\\output\\test-mongo-scenarioA\\outputRun-dim" + str(dim) +".txt", cur_path)
                    for filename in os.listdir(cur_path):
                        if re.search("^output-Run-dim" + str(dim) + "-throughput" + str(t) +"-clients.*" + "\.txt$", filename) :
                            new_path = os.path.join(cur_path,filename)
                            f = open(new_path, "r")
                            for line in f:
                                if "[READ], AverageLatency(us)," in line:
                                    parts = line.split("[READ], AverageLatency(us), ")
                                    num = float(parts[1])
                                    read.addPoint(t,num)
                                else:
                                    if "[UPDATE], AverageLatency(us)," in line:
                                        parts = line.split("[UPDATE], AverageLatency(us),")
                                        num = float(parts[1])
                                        update.addPoint(t,num)
                            f.close()
                reads.append(read)
                updates.append(update)

            marker = itertools.cycle((',', '+', '.', 'o', '*', 's', 'x')) 

            for serie in reads:
                plt.plot(serie.x, serie.y, linewidth = 1, 
                        marker=next(marker), markerfacecolor='blue', markersize=5, label="READ - " + serie.name) 
            
            for serie in updates:
                plt.plot(serie.x, serie.y, linewidth = 1, 
                        marker=next(marker), markerfacecolor='blue', markersize=5, label="UPDATE - " + serie.name)  
                        
            # naming the x axis 
            plt.xlabel('Throughput') 
            plt.xscale('log')
            # naming the y axis 
            plt.ylabel('Average latency (us)') 
            
            # giving a title to my graph 
            plt.title('Throughput / latency curve with Input dimension=' + str(dim) + " and " + str(c) + " clients") 
            plt.legend()
            
            # function to show the plot 
            plt.show()
            
            #function for save result plt.show in file
            #plt.savefig('result.png')
