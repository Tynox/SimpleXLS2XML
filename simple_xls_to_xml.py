#!/usr/bin/env python
# encoding:utf-8

"""
A Simple XLS convertor.
It can convert XLS to XMl or CVS.

author:Tynox
website:http://tarkrul.info

This is a free and unencumbered software into the public domain.
For more information, please refer to <http://unlicense.org>
"""


import codecs
import getopt
import os
import re
import sys
import xlrd
import xml.dom.minidom

version = 0.1

filter_words = None


def init():
    """
    Init and get arguments.
    """
    
    # get options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hv", ["--help", "--version"])
    except getopt.GetoptError as err:
        print str(err)
        sys.exit()
    else:
        parseOpts(opts, args)


def parseOpts(opts, args):
    """
    parse opts and arguments
    """

    shouldExit = False
    
    # check options. If operation is None, exit.
    for o, a in opts:
        if o in ("-h", "--help)":       # get help
            getHelp()
            shouldExit = True
        else o in ("-v", "--version"):  # show version
            showVersion()
            shouldExit = True

        if shouldExit:
            sys.exit()


def xlsRead():
    # reade xls
    global filter_words
    
    data = xlrd.open_workbook("filter.xlsx")
    table = data.sheets()[0]        # 获取第一个sheet
    filter_words = table.col_values(0)
    
    
def createXML():
    # create xml
    if filter_words is None:
        return
        
    new_filter = list()
    
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, "filters", None)
    root = dom.documentElement
    
    for f in filter_words:
        if len(f) == 0:
            continue
        # remove whitespace
        whitespace = re.compile("\s")
        f = re.sub(whitespace, "", f)
        if f in new_filter:
            continue
        new_filter.append(f)
        # create element
        filter = dom.createElement("filter")
        filter.setAttribute("word", f)
        root.appendChild(filter)
        
    out = codecs.open("filters.xml", "w", "utf-8")
    dom.writexml(out, addindent=" ", newl="\n", encoding="utf-8")
    out.close()
    
    
def createCVS():
    # TODO:创建CVS
    pass
    
    
if __name__ == "__main__":
    xlsRead()
    createXML()
