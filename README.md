# Project Big Data 
 Authors: [Andrea Apicella](https://github.com/andrea19081996) Andrea Apicella e [Davide Bersani](https://github.com/davidebersani)

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
./init-project.sh
```
Afther this, you can download YCSB using the script ```download-ycsb.sh``` . Then, you're ready to benchmark!

## Edit script and benchmarks
If you want to edit some benchmark or script we suggest to do this editing the files contained in **template-scripts**. In this way you can use some useful variables contained in ```commons.sh``` and ```commons.py``` scripts.

When you have finished, run ```init-project.sh``` again to generate the correct scripts.

## Usage
(In progress...)