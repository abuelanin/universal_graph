#!/usr/bin/env bash
#! $1: kmerSize | $2: abundance | $3: runNo | $4: seqFileName | $5: SeqType (fa,fq,fastaq)
./bcalm/build/bcalm -in data/$4.$5 -kmer-size $1 -abundance-min $2
mkdir temp
mv $4.* temp
python bcalm/scripts/convertToGFA.py temp/$4.unitigs.fa $4_$1_$2.gfa $1
mv *.gfa GFAs
rm -r temp