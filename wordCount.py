import sys  # command line arguments
import re  # regular expression tools
import os  # checking if file exists
import subprocess  # executing program

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
    exit()
