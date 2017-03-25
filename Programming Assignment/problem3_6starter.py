# -problem3_6.py *- coding: utf-8 -*-

import sys

infile = sys.argv[1]
outfile = sys.argv[2]
infile = open(infile)
outfile = open(outfile,'w')
for line in infile:
    line = line.strip("\n")
outfile.write(str(len(line))) + "\n"
infile.close()
outfile.close()