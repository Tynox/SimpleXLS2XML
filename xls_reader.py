#!/usr/bin/env pythhon
# encoding:utf-8

import xlrd


def reader(fName):
    """
    reader xls
    fName: xls file name
    """

    # open xls file
    data = xlrd.open_workbook(fName)

    # get sheet *
    table = data.sheets()[0]
    
    # get a col * data
    data = table.col_values(0)
    
    return


if __name__ == "__main__":
    pass
