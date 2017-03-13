#!/usr/bin/python

# http://stackoverflow.com/questions/2535255/fastest-way-convert-tab-delimited-file-to-csv-in-linux

# Usage: python script.py < input.tsv > output.csv

import sys
import csv

tabin = csv.reader(sys.stdin, dialect=csv.excel_tab)
commaout = csv.writer(sys.stdout, dialect=csv.excel, delimiter=';', lineterminator='\n', quoting=csv.QUOTE_ALL)
for row in tabin:
  commaout.writerow(row)

