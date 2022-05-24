import sys  # command line arguments
import re  # regular expression tools
import os  # checking if file exists
# import subprocess  # executing program

# set input and output files
if len(sys.argv) != 3:
    print("Correct usage: wordCount.py <input text file> <output file> ")
    exit()


inputFname = sys.argv[1]
outputFname = sys.argv[2]

# make sure text files exist
if not os.path.exists(inputFname):
    print("text file input %s doesn't exist! Exiting" % inputFname)
    exit()

# make sure output file exists
if not os.path.exists(outputFname):
    print("Creating new file")
    outputFile = open(outputFname, 'w+')
    # print("wordCount output file %s doesn't exist! Exiting" % outputFname)
else:
    outputFile = open(outputFname, 'w+')

# word count
words = 0

# word list
master = {}




# open input file
# remove punctuation and new lines
with open(inputFname, 'r') as inputFile:
    for line in inputFile:
        # get rid of newline characters
        line = line.strip()
        # split line on whitespace and punctuation
        line = re.sub(r'[^\w\s]', '', line)
        word = re.split('[ \t]', line)
        for element in word:
            if master.get(element) is None:
                master[element] = 1
            else:
                master[element] = master[element]+1
sortedMaster = sorted(master, reverse=True)
for item in sortedMaster:
    print(item , master.get(item))

exit()