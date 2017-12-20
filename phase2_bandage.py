import csv
import re
from os import listdir
from os.path import isfile, join
from subprocess import check_output
from tqdm import tqdm
import sys
import json


with open('config.json', 'r') as f:
		config = json.load(f)

gfa_dir = config["gfa_files_path"]
bandage_dir = config["bandage_path"]
report_dir = config["report_dir_path"]
csv_dir = config["csv_dir_path"]
csv_file_name = config["csv_file_name"]


# Extract the names of the features from the bandage output
def constructFeaturesNames(fileName):
    fileName = gfa_dir + "/" + fileName
    out = check_output(["./"+ bandage_dir + "/Bandage", "info", fileName]).decode("utf-8")
    splitted = out.split('\n')
    splitted.pop(19)
    features_names = ["Kmer"]
    for line in splitted:
        x = line.split(":")
        # x[0] = x[0].replace(" ", "-")
        features_names.append(x[0])
    print "Processing the GFA files...\n"
    return features_names


# Function to get all the info of a GFA file using Bandage
def getBandageInfo(fileName, Kmer):
    fileName = gfa_dir + "/" + fileName
    out = check_output(["./"+ bandage_dir + "/Bandage", "info", fileName]).decode("utf-8")
    splitted = out.split('\n')
    splitted.pop(19)
    values = [Kmer]
    for line in splitted:
        value = float(re.search(r'(\d+(\.\d+)?)', line).group(0))
        values.append(value)
    return values

def exportToCSV():
    global features_names, features
    f = open(report + "/" + csv_dir + csv_file_name, 'w')
    try:
        writer = csv.writer(f)
        writer.writerow(features_names)
        for i in features:
            writer.writerow(features[i])
    finally:
        f.close()


print "Initializing the process...\n"

# Get all GFA Files Names
gfa_files = [f for f in listdir(gfa_dir) if isfile(join(gfa_dir, f))]

# Creating Features Names Array
features = {}

# Construct_Features_names
features_names = constructFeaturesNames(gfa_files[0])

for i in tqdm(range(len(gfa_files))):
    gfa = gfa_files[i]
    kmer = gfa.split("_")[1]
    features[int(kmer)] = getBandageInfo(gfa, kmer)

# Export results to CSV
exportToCSV()