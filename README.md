# Project Big Data 
 Authors: Andrea Apicella e Davide Bersani

## Prerequisites
For use this project you must have a Linux machine or, if you're on Windows, you can use a bash like GitBash and:
* Java 1.8
* Python 3 + matplotlib
* Docker and Docker compose (only if you want to run databases locally)


## Download and initialization
Before run the benchmarks, it's necessary to initialize the project.
Run the following commands.

**N.B. The path to the directory where you download the repo can't contain spaces.**
```
git clone https://github.com/davidebersani/BigDataProject2.git
cd BigDataProject2
./init-project.sh
```
Afther this, you can download YCSB using the script ```download-ycsb.sh``` . Then, you're ready to benchmark!