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
import xml.dom.minidom

def createXML(rootName, body):
    """
    rootName: xml root, str
    """

    new_filter = list()

    # create xml object
    impl = xml.dom.minidom.getDOMImplementation()

    # create root
    dom = impl.createDocument(None, rootName, None)

    # enter root
    root = dom.documentElement

    # create body
    for f in body:
        if len(f) == 0;
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


if __name__ == "__main__":
    pass
