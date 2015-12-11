#!/usr/bin/env python

import re
import sys
import csv

i = int("0")
total_sum = int("0")
period = int("20")
total_period = int("0")
row_count = int("0")

with open('31.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        i = int(row[0])
        total_sum += int(i)
        row_count += int("1")
        print row
        print i

    total_period = period * row_count
    processor_utilization = int(total_sum/total_period)

    print "total sum       :- " '%d' %total_sum
    print "total period    :- " '%d' %total_period
    print "processor utilization :- " '%d' %processor_utilization
    print row_count
    
        
         

