import csv
import re
from os import listdir
from os.path import isfile, join
from subprocess import check_output
from tqdm import tqdm


# Extract the names of the features from the bandage output
def constructFeaturesNames(fileName):
    fileName = "GFAs/" + fileName
    out = check_output(["Bandage", "info", fileName]).decode("utf-8")
    splitted = out.split('\n')
    splitted.pop(19)
    features_names = ["Kmer"]
    for line in splitted:
        x = line.split(":")
        # x[0] = x[0].replace(" ", "-")
        features_names.append(x[0])
    return features_names


# Function to get all the info of a GFA file using Bandage
def getBandageInfo(fileName, Kmer):
    fileName = "GFAs/" + fileName
    out = check_output(["./Bandage/Bandage", "info", fileName]).decode("utf-8")
    splitted = out.split('\n')
    splitted.pop(19)
    values = [Kmer]
    for line in splitted:
        value = float(re.search(r'(\d+(\.\d+)?)', line).group(0))
        values.append(value)
    return values

def exportToCSV():
    global features_names, features
    f = open("result.csv", 'w')
    #features = sorted(features.items(), key=operator.itemgetter(0))
    try:
        writer = csv.writer(f)
        writer.writerow(features_names)
        for i in features:
            writer.writerow(features[i])
    finally:
        f.close()


# Get all GFA Files Names
gfa_files = [f for f in listdir("GFAs") if isfile(join("GFAs", f))]

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