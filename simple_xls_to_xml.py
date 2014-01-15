# encoding:utf-8

import codecs
import re
import xlrd
import xml.dom.minidom

filter_words = None


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
    
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, "filters", None)
    root = dom.documentElement
    
    for f in filter_words:
        if len(f) == 0:
            continue
        # remove whitespace
        whitespace = re.compile("\s")
        f = re.sub(whitespace, "", f)
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