#!/usr/bin/env python
# encoding:utf-8

"""
CVS creator.py

author:Tynox
website: http://tarkrul.info

 
This is a free and unencumbered software into the public domain.
For more information, please refer to <http://unlicense.org>
"""

import csv
import os


def createCSV(file_name, data):
    """
    """
    # write the csv file
    csvfile = open("{0}.csv".format(file_name), "wb")
    
    # create a csv writer
    writer = csv.writer(csvfile)

    # write data
    for r in data:
        writer.writerow([r])

    print "CSV created successfully!"


if __name__ == "__main__":
    pass
