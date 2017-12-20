# Universal Genome Graph Projects

The aim of the project is to identify genes that extracted from weak genomes.

# Features!

  - Convert FASTA files to Graphical Fragment Assembly format (GFA 1).
  - Extract the No. of the disconnected graphs with different k-mer values.

### Used programs:

| Program | README |
| ------ | ------ |
| Bcalm2 | https://github.com/GATB/bcalm/blob/master/README.md|
| Bandage | https://github.com/rrwick/Bandage/blob/master/README.md |

> We've used Bcalm to generate the unitigs for the sequence then convert the unitigs to GFA.
> Bandage is used to extract the connected graphs number.



### Installation (Linux) Tested on Ubuntu 


##### Clone the Universal Graph repository

```sh
git clone https://github.com/abuelanin/universal_graph.git
```


##### Install the dependencies
-- GCC >= 4.8 or a very recent C++11 capable compiler

```sh
sudo apt-get update
apt-get install build-essential
sudo apt-get install g++ gcc
sudo apt-get update
```
-- QT5
Install the dependencies and devDependencies and start the server.
```sh
sudo apt-get update
sudo apt-get install build-essential git qtbase5-dev libqt5svg5-dev
export QT_SELECT=5
```

Download and install Bcalm

```sh
git clone --recursive https://github.com/GATB/bcalm 
cd bcalm
mkdir build;  cd build;  cmake ..;  make -j 8
cd ../../
```

Download and install Bandage

```sh
sudo apt-get update
git clone https://github.com/rrwick/Bandage.git
cd Bandage
qmake
make
cd ..
```

> Optionally, copy the program into /usr/local/bin:```sudo make install```. The Bandage build directory can then be deleted.


----------

#### Python Dependices
| package | installation |
|--|--|
| tqdm | `sudo pip install tqdm` |
| numpy | `sudo pip install numpy`|
| pandas | `sudo pip install pandas`|
| plotly | `sudo pip install plotly` |


----------
***Project directory should be like this***

> Some directory and file names can be re-configured in the file **config.json**

```
├── Bandage
├── bcalm
├── data
├── GFAs
├── report
│   ├── csv
│   └── plots
├── bcalm.sh
├── phase1_bcalm.py
├── phase2_bandage.py
├── phase3_plot.py
├── run.sh
├── config.json
├── README.md
```


----------



## How to run
From the terminal, execute **./run.sh** file with passing the sequence file name that is located in the **data** directory.

Ex: passing fasta file called "seq.fa"  `./run.sh seq.fa`

