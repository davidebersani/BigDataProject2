import os
import matplotlib.pyplot as plt 
import re
import itertools
import commons

class Serie:

    def __init__(self, name):
        self.x = []
        self.y = []
        self.name = name

    def addPoint(self, x1, y1):
        self.x.append(x1)
        self.y.append(y1)

def generateAndShowInputLatencyPlots(input_dim, throughputs, clients, source, workload) :

    cur_path = os.path.dirname(__file__)
    cur_path = os.path.join(cur_path, source)
    for c in clients:
        for t in throughputs:
            # Generate plot Input dim / latency for every throughput value
            read = Serie("read")
            update = Serie("update")
            scan = Serie("scan")
            readModifyWrite = Serie("Read-Modify-Write")
        
            for dim in input_dim:
                # new_path = os.path.join(cur_path, source ,"output-Run-dim" + str(dim) +".txt")
                # new_path = os.path.relpath("\\output\\test-mongo-scenarioA\\outputRun-dim" + str(dim) +".txt", cur_path)
                filename = commons.getOutputFilename(cur_path, "Run", workload, dim, t, c)
                new_path = os.path.join(cur_path,filename)
                f = open(new_path, "r")
                for line in f:
                    if "[READ], AverageLatency(us)," in line:
                        parts = line.split("[READ], AverageLatency(us), ")
                        num = float(parts[1])
                        read.addPoint(dim, num)
                    elif "[UPDATE], AverageLatency(us)," in line:
                        parts = line.split("[UPDATE], AverageLatency(us),")
                        num = float(parts[1])
                        update.addPoint(dim, num)
                    elif "[SCAN], AverageLatency(us)," in line:
                        parts = line.split("[SCAN], AverageLatency(us),")
                        num = float(parts[1])
                        scan.addPoint(dim, num)
                    elif "[READ-MODIFY-WRITE], AverageLatency(us)," in line:
                        parts = line.split("[READ-MODIFY-WRITE], AverageLatency(us),")
                        num = float(parts[1])
                        readModifyWrite.addPoint(dim, num)
                f.close()

            if(len(read.x)>0):
                plt.plot(read.x, read.y, linewidth = 1, 
                        marker='o', markerfacecolor='blue', markersize=5, label="READ") 
            if(len(update.x)>0):
                plt.plot(update.x, update.y, linewidth = 1, 
                        marker='o', markerfacecolor='blue', markersize=5, label="UPDATE")  
            
            if(len(scan.x)>0):
                plt.plot(scan.x, scan.y, linewidth = 1, 
                    marker='o', markerfacecolor='blue', markersize=5, label="SCAN")  

            if(len(readModifyWrite.x)>0):
                plt.plot(readModifyWrite.x, readModifyWrite.y, linewidth = 1, 
                    marker='o', markerfacecolor='blue', markersize=5, label="READ-MODIFY-WRITE")  


            # naming the x axis 
            plt.xlabel('Input dimension') 
            plt.xscale('log')
            # naming the y axis 
            plt.ylabel('Average latency (us)') 
            
            # giving a title to my graph 
            plt.title(workload + ' Input dimension / latency with Throughput=' + str(t) + " and " + str(c) + " clients") 
            plt.legend()
            
            # function to show the plot 
            plt.show()
            
            #function for save result plt.show in file
            #plt.savefig('result.png')

def generateAndShowThroughputLatencyPlots(input_dim, throughputs, clients, source, workload) :
    cur_path = os.path.dirname(__file__)
    cur_path = os.path.join(cur_path, source)
    for c in clients:
        for dim in input_dim:
            # Generate plot Throughput / latency for every dim value
            read = Serie("read")
            update = Serie("update")
            scan = Serie("scan")
            readModifyWrite = Serie("Read-Modify-Write")

            for t in throughputs:
                # new_path = os.path.join(cur_path, source ,"output-Run-dim" + str(dim) +".txt")
                # new_path = os.path.relpath("\\output\\test-mongo-scenarioA\\outputRun-dim" + str(dim) +".txt", cur_path)
                filename = commons.getOutputFilename(cur_path, "Run", workload, dim, t, c)
                new_path = os.path.join(cur_path,filename)
               
                f = open(new_path, "r")
                for line in f:
                    if "[READ], AverageLatency(us)," in line:
                        parts = line.split("[READ], AverageLatency(us), ")
                        num = float(parts[1])
                        read.addPoint(t, num)
                    elif "[UPDATE], AverageLatency(us)," in line:
                        parts = line.split("[UPDATE], AverageLatency(us),")
                        num = float(parts[1])
                        update.addPoint(t, num)
                    elif "[SCAN], AverageLatency(us)," in line:
                        parts = line.split("[SCAN], AverageLatency(us),")
                        num = float(parts[1])
                        scan.addPoint(t, num)
                    elif "[READ-MODIFY-WRITE], AverageLatency(us)," in line:
                        parts = line.split("[READ-MODIFY-WRITE], AverageLatency(us),")
                        num = float(parts[1])
                        readModifyWrite.addPoint(t, num)
                f.close()

            if(len(read.x)>0):
                plt.plot(read.x, read.y, linewidth = 1, 
                        marker='o', markerfacecolor='blue', markersize=5, label="READ") 
            if(len(update.x)>0):
                plt.plot(update.x, update.y, linewidth = 1, 
                        marker='o', markerfacecolor='blue', markersize=5, label="UPDATE")  
            
            if(len(scan.x)>0):
                plt.plot(scan.x, scan.y, linewidth = 1, 
                    marker='o', markerfacecolor='blue', markersize=5, label="SCAN")  

            if(len(readModifyWrite.x)>0):
                plt.plot(readModifyWrite.x, readModifyWrite.y, linewidth = 1, 
                    marker='o', markerfacecolor='blue', markersize=5, label="READ-MODIFY-WRITE")  

            # naming the x axis 
            plt.xlabel('Throughput') 
            plt.xscale('log')
            # naming the y axis 
            plt.ylabel('Average latency (us)') 
            
            # giving a title to my graph 
            plt.title(workload + ' Throughput / latency curve with Input dimension=' + str(dim) + " and " + str(c) + " clients") 
            plt.legend()
            
            # function to show the plot 
            plt.show()
            
            #function for save result plt.show in file
            #plt.savefig('result.png')

def generateAndShowInputLatencyPlotsComparison(input_dim, throughputs, clients, sources, workload) :
    for c in clients:
        for t in throughputs:
            reads=[]
            updates=[]
            scans=[]
            rmw=[]
            # Generate plot Input dim / latency for every throughput value
            for source in sources:
                read = Serie(source)
                update = Serie(source)
                scan = Serie(source)
                readModifyWrite = Serie(source)
                cur_path = os.path.dirname(__file__)
                cur_path = os.path.join(cur_path, source)
                for dim in input_dim:
                    # new_path = os.path.join(cur_path, source ,"output-Run-dim" + str(dim) +".txt")
                    # new_path = os.path.relpath("\\output\\test-mongo-scenarioA\\outputRun-dim" + str(dim) +".txt", cur_path)
                    filename = commons.getOutputFilename(cur_path, "Run", workload, dim, t, c)
                    new_path = os.path.join(cur_path,filename)
                    
                    f = open(new_path, "r")
                    for line in f:
                        if "[READ], AverageLatency(us)," in line:
                            parts = line.split("[READ], AverageLatency(us), ")
                            num = float(parts[1])
                            read.addPoint(dim, num)
                        elif "[UPDATE], AverageLatency(us)," in line:
                            parts = line.split("[UPDATE], AverageLatency(us),")
                            num = float(parts[1])
                            update.addPoint(dim, num)
                        elif "[SCAN], AverageLatency(us)," in line:
                            parts = line.split("[SCAN], AverageLatency(us),")
                            num = float(parts[1])
                            scan.addPoint(dim, num)
                        elif "[READ-MODIFY-WRITE], AverageLatency(us)," in line:
                            parts = line.split("[READ-MODIFY-WRITE], AverageLatency(us),")
                            num = float(parts[1])
                            readModifyWrite.addPoint(dim, num)
                    f.close()
                reads.append(read)
                updates.append(update)
                scans.append(scan)
                rmw.append(readModifyWrite)

            marker = itertools.cycle((',', '+', '.', 'o', '*', 's', 'x')) 
            for serie in reads:
                if(len(serie.x)>0):
                    plt.plot(serie.x, serie.y, linewidth = 1, 
                            marker=next(marker), markerfacecolor='blue', markersize=5, label="READ - " + serie.name) 
            
            for serie in updates:
                if(len(serie.x)>0):
                    plt.plot(serie.x, serie.y, linewidth = 1, 
                            marker=next(marker), markerfacecolor='blue', markersize=5, label="UPDATE - " + serie.name)  
                
            for serie in scans:
                if(len(serie.x)>0):
                    plt.plot(serie.x, serie.y, linewidth = 1, 
                            marker=next(marker), markerfacecolor='blue', markersize=5, label="SCAN - " + serie.name)  
            for serie in rmw:
                if(len(serie.x)>0):
                    plt.plot(serie.x, serie.y, linewidth = 1, 
                            marker=next(marker), markerfacecolor='blue', markersize=5, label="READ-MODIFY-WRITE - " + serie.name)  
            
            # naming the x axis 
            plt.xlabel('Input dimension') 
            plt.xscale('log')
            # naming the y axis 
            plt.ylabel('Average latency (us)') 
            
            # giving a title to my graph 
            plt.title(workload + ' Input dimension / latency with Throughput=' + str(t) + " and " + str(c) + " clients") 
            plt.legend()
            
            # function to show the plot 
            plt.show()
            
            #function for save result plt.show in file
            #plt.savefig('result.png')

def generateAndShowThroughputLatencyPlotsComparison(input_dim, throughputs, clients, sources, workload) :
    for c in clients:
        for dim in input_dim:
            # Generate plot Throughput / latency for every dim value
            reads=[]
            updates=[]
            scans=[]
            rmw=[]
            for source in sources:
                read = Serie(source)
                update = Serie(source)
                scan = Serie(source)
                readModifyWrite = Serie(source)
                cur_path = os.path.dirname(__file__)
                cur_path = os.path.join(cur_path, source)
                for t in throughputs:
                    # new_path = os.path.join(cur_path, source ,"output-Run-dim" + str(dim) +".txt")
                    # new_path = os.path.relpath("\\output\\test-mongo-scenarioA\\outputRun-dim" + str(dim) +".txt", cur_path)
                    filename = commons.getOutputFilename(cur_path, "Run", workload, dim, t, c)
                    new_path = os.path.join(cur_path,filename)

                    f = open(new_path, "r")
                    for line in f:
                        if "[READ], AverageLatency(us)," in line:
                            parts = line.split("[READ], AverageLatency(us), ")
                            num = float(parts[1])
                            read.addPoint(t,num)
                        elif "[UPDATE], AverageLatency(us)," in line:
                            parts = line.split("[UPDATE], AverageLatency(us),")
                            num = float(parts[1])
                            update.addPoint(t, num)
                        elif "[SCAN], AverageLatency(us)," in line:
                            parts = line.split("[SCAN], AverageLatency(us),")
                            num = float(parts[1])
                            scan.addPoint(t, num)
                        elif "[READ-MODIFY-WRITE], AverageLatency(us)," in line:
                            parts = line.split("[READ-MODIFY-WRITE], AverageLatency(us),")
                            num = float(parts[1])
                            readModifyWrite.addPoint(t, num)
                    f.close()
                reads.append(read)
                updates.append(update)
                scans.append(scan)
                rmw.append(readModifyWrite)

            marker = itertools.cycle((',', '+', '.', 'o', '*', 's', 'x')) 

            for serie in reads:
                if(len(serie.x)>0):
                    plt.plot(serie.x, serie.y, linewidth = 1, 
                            marker=next(marker), markerfacecolor='blue', markersize=5, label="READ - " + serie.name) 
            
            for serie in updates:
                if(len(serie.x)>0):
                    plt.plot(serie.x, serie.y, linewidth = 1, 
                            marker=next(marker), markerfacecolor='blue', markersize=5, label="UPDATE - " + serie.name)  
            
            for serie in scans:
                if(len(serie.x)>0):
                    plt.plot(serie.x, serie.y, linewidth = 1, 
                            marker=next(marker), markerfacecolor='blue', markersize=5, label="SCAN - " + serie.name)  

            for serie in rmw:
                if(len(serie.x)>0):
                    plt.plot(serie.x, serie.y, linewidth = 1, 
                            marker=next(marker), markerfacecolor='blue', markersize=5, label="READ-MODIFY-WRITE - " + serie.name)  
                            
            # naming the x axis 
            plt.xlabel('Throughput') 
            plt.xscale('log')
            # naming the y axis 
            plt.ylabel('Average latency (us)') 
            
            # giving a title to my graph 
            plt.title(workload + ' Throughput / latency curve with Input dimension=' + str(dim) + " and " + str(c) + " clients") 
            plt.legend()
            
            # function to show the plot 
            plt.show()
            
            #function for save result plt.show in file
            #plt.savefig('result.png')
