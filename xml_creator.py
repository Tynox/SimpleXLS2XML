#!/usr/bin/env python
# encoding:utf-8

"""
xml_creator.py

author: Tynox
website: http://tarkru.info

This is a free and unencumbered software into the public domain.
For more information, please refer to <http://unlicense.org>
"""

import codecs
import re
import xml.dom.minidom

def createXML(file_name, body, rootName="root", element="element", attrib="attrib"):
    """
    rootName: xml root, str
    """
    
    # no repeated
    no_repeated = list()

    # create xml object
    impl = xml.dom.minidom.getDOMImplementation()

    # create root
    dom = impl.createDocument(None, rootName, None)

    # enter root
    root = dom.documentElement

    # create body
    for f in body:
        if len(f) == 0:
            continue

        # remove whitespace
        whitespace = re.compile("\s")
        f = re.sub(whitespace, "", f)
        if f in no_repeated:
            continue
        no_repeated.append(f)

        # create element
        el = dom.createElement(element)
        el.setAttribute(attrib, f)
        root.appendChild(el)
    
    # create xml file
    out = codecs.open("{0}.xml".format(file_name), "w", "utf-8")

    # write into xml
    dom.writexml(out, addindent=" ", newl="\n", encoding="utf-8")

    # close file
    out.close()


if __name__ == "__main__":
    pass
