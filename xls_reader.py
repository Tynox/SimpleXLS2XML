#!/usr/bin/env pythhon
# encoding:utf-8

import xlrd


def reader(fName):
    """
    reader xls
    fName: xls file name
    """

    data = dict()

    # open xls file
    xls = xlrd.open_workbook(fName)

    # get sheet *
    table = xls.sheets()[0]
    
    # get a col * data
    col = table.col_values(0)

    # get a row data
    row = table.col_values(0)
    
    return col


if __name__ == "__main__":
   import sys
   f = sys.argv[1]
   data = reader(f)
   print data
