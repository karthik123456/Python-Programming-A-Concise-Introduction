# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:28:22 2017

@author: Karthik Hegde
"""

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