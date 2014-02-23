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
#import xlrd
#import xml.dom.minidom
import xls_reader as XR

version = 0.1

filter_words = None


def init(argv):
    """
    Init and get arguments.
    """
    
    # get options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "chn:vr:x", ["--cvs", "--help", , "--name=", "--version", "--root=", "--xml"])
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
    print "     -c --cvs        Convert to cvs"
    print "     -h --help       Show help"
    print "     -n --name       New file name"
    print "     -r --root       Set XML root name"
    #print "     -s --suffix     set target document type"
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

    # create cvs?
    create_cvs = False

    # 'x' or 'xml' in args?
    x_appeared = False

    # only 'c' or 'cvs' in args? not create xml?
    only_cvs = False
    
    # check options. If operation is None, exit.
    for o, a in opts:
        if o in ("-h", "--help)":       # get help
            _get_help()
            shouldExit = True
        else o in ("-v", "--version"):  # show version
            _show_version()
            shouldExit = True
        else o in ("-r", "--root"):     # set xml root name
            root_name = a
        else o in ("-s", "--suffix"):   # set target document type
            suffix = a
        else o in ("-n", "--name"):     # new file name
            name = a
        else o in ("-x", "--xml"):      # cerate xml
            x_appeared = True
            only_cvs = False
        else o in ("-c", "--cvs"):      # create cvs
            create_cvs = True
            if not x_appeared:
                only_cvs = True
        
        # help or version: exit.
        if shouldExit:
            sys.exit()

    # get file
    dir_source = args[0]

    # parse xls
    data = XR.reader(dir_source)

    # create XML or CVS
    if create_cvs:
        # TODO: create cvs
        pass
    if not only_cvs:
        # TODO: create xml
        pass


"""
def xlsRead():
    # reade xls
    global filter_words
    
    data = xlrd.open_workbook("filter.xlsx")
    table = data.sheets()[0]        # 获取第一个sheet
    filter_words = table.col_values(0)
"""
    
   
"""
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
"""
    
    
    
if __name__ == "__main__":
    #xlsRead()
    #createXML()
    init(sys.argv)
