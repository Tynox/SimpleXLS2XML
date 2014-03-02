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
import xls_reader as XR
import csv_creator as CC
import xml_creator as XC

# version
version = 0.1


def init(argv):
    """
    Init and get arguments.
    """
    
    # get options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ce:hn:vr:x", ["--csv", "--element", "--help", "--name=", "--version", "--root=", "--xml"])
    except getopt.GetoptError as err:
        print str(err)
        _get_help()
        sys.exit()
    else:
        parseOpts(opts, args)


def _show_version():
    print "Version:{0}".format(version)


def _get_help():
    """
    get tool help
    """

    # show version
    _show_version()

    print "SimpleXLSConverter"
    print "-"*10
    print "SXC: convert XLS to XML/CVS. [Convert to XML by default.]"
    print "useage: SimpleXLSConverter..py [-h|--help] [-v|--version]"
    print "     -c --csv        Convert to csv"
    print "     -e --element    Set xml element name(Only available in single line mode)"
    print "     -h --help       Show help"
    print "     -n --name       New file name"
    print "     -r --root       Set XML root name"
    print "     -v --version    Show version"
    print "     -x --xml        Convert to xml"

def parseOpts(opts, args):
    """
    parse opts and arguments
    """

    # help or show version: exit and convert nothing
    shouldExit = False

    # xml root name
    root_name = None

    # xml element name
    element_name = None

    # create csv?
    create_csv = False

    # 'x' or 'xml' in args?
    x_appeared = False

    # only 'c' or 'csv' in args? not create xml?
    only_csv = False
    
    # check options. If operation is None, exit.
    for o, a in opts:
        if o in ("-h", "--help"):       # get help
            _get_help()
            shouldExit = True
        elif o in ("-v", "--version"):  # show version
            _show_version()
            shouldExit = True
        elif o in ("-r", "--root"):     # set xml root name
            root_name = a
        elif o in ("-n", "--name"):     # new file name
            name = a
        elif o in ("-x", "--xml"):      # cerate xml
            x_appeared = True
            only_csv = False
        elif o in ("-c", "--csv"):      # create csv
            create_csv = True
            if not x_appeared:
                only_csv = True
        elif o in ("-e", "--element"):  # set element name
            element_name = a
        
        # help or version: exit.
        if shouldExit:
            sys.exit()

    # get file
    dir_source = args[0]
    p = dir_source.rfind(".")
    if p == -1:
        file_name = dir_source
    else:
        file_name = dir_source[:dir_source.rfind(".")]

    # parse xls
    data = XR.reader(dir_source)

    # create XML or CVS
    if create_csv:
        CC.createCSV(file_name, data)
    if not only_csv:
        XC.createXML(file_name, data)


if __name__ == "__main__":
    #xlsRead()
    #createXML()
    init(sys.argv)
