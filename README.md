# Project Big Data 
 Authors: [Andrea Apicella](https://github.com/andrea19081996) e [Davide Bersani](https://github.com/davidebersani)

## Prerequisites
For use this project you must have a Linux machine or, if you're on Windows, you can use a bash like GitBash and:
* Java 1.8
* Python 3 + matplotlib installed
* Docker and Docker compose (only if you want to run databases locally)


## Download and initialization
Before run the benchmarks, it's necessary to initialize the project.
Run the following commands.

**N.B. The path to the directory where you download the repo can't contain spaces.**
```
git clone https://github.com/davidebersani/BigDataProject2.git
cd BigDataProject2
chmod +x init-project.sh
./init-project.sh
```
Afther this, you can download YCSB using the script ```scripts/download-ycsb.sh``` . Then, you're ready to benchmark!

## Edit scripts and benchmarks
If you want to edit some benchmark or script we suggest to do this editing the files contained in **template-scripts** directory. In this way you can use some useful variables contained in ```commons.sh``` and ```commons.py``` scripts.

When you have finished, run ```init-project.sh``` again to generate the correct scripts. Remeber, run always scripts that are in **scripts** directory.

## Usage
You can try benchmarks on local databases or you can test your cloud solution.
### Try with local databaes
First, start the databases you want to test. If you want, you can use the script ```start-local-services.sh``` contained in the script directory for start the databases and some useful services using Docker. 

After this, you can use "benchmark-*" Python scripts to start the benchmarks. First, we suggest to open these scripts from the template-scripts direcotry and modify them. You can edit parameters like operations/thread, input dimensions, throughputs, output directory and others variables. 

When you have finished, run ```init-project.sh``` again to generate the correct scripts. Remeber, run always scripts that are in **scripts** directory.

When the benchmarks is terminated, you will find some reports in the output directory specified in the script. They will be useful to understand how the db is perfoming. You can also generate some useful plots using the "generate-*" Python scripts.

### Try a cloud solution
You can also use these benchmarks to test db in cloud. If you have a good Internet connection you can edit the benchmarks setting the correct parameters to use remote db (default is local db) and run the benchmarks locally. But, if you have a bad connection, we suggest to use another machine to run the benchmarks (for example, an ec2 instance near the db). Doing this, test will not affected by latency problems.
