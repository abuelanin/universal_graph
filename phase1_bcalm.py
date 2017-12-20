import os,sys
import subprocess
from tqdm import tqdm

# x = os.path.dirname(os.path.abspath(__file__))

# ! $1: kmerSize | $2: abundance | $3: runNo | $4: seqFileName | $5: SeqType (fa,fq,fastaq)


if(len(sys.argv) < 2):
    sys.exit('Please pass the file name in the data directory and ensure that it has no underscore character!\nEx: python generateGFAs.py read.fa')
elif(len(sys.argv) >= 2):
    seqFileName = str(sys.argv[1]).split(".")[0]
    seqType = str(sys.argv[1]).split(".")[1]


kmer_size = str(21)
min_abundance = str(1)
run_no = str(1)

# subprocess.call(" ".join(["./run.sh", kmer_size, min_abundance, run_no, seqFileName, seqType]), shell=True)

runNo = 1
for i in tqdm(range(17, 76, 2)):
    if i % 4 == 0:
        continue
    kmer_size = str(i)
    run_no = str(runNo)
    # print "\n" + ("--" * 15) + str("#" + str(runNo)) + "| kmer = " + str(kmer_size) + (" --" * 15) + "\n"
    # Hide results
    FNULL = open(os.devnull, 'w')
    subprocess.call(" ".join(["./bcalm.sh", kmer_size, min_abundance, run_no, seqFileName, seqType]), shell=True,
                    stdout=FNULL, stderr=subprocess.STDOUT)
    runNo += 1