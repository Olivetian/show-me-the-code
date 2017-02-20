# -*- coding: utf-8 -*-

import xlrd
from collections import OrderedDict
from xml.etree.ElementTree import ElementTree,Element, SubElement, Comment
import json
import io

fromfile = 'student.xls'

def read_xls(fromfile):
    book = xlrd.open_workbook(fromfile)
    sheet = book.sheet_by_index(0)
    data = OrderedDict()
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(rows):
        kv = []
        for j in range(1, cols):
            if type(sheet.cell_value(i, j)) is float:
                kv.append(int(sheet.cell_value(i, j)))
            else:
                kv.append(sheet.cell_value(i, j))
        data[str(int(sheet.cell_value(i, 0)))] = kv
    return json.dumps(data, ensure_ascii = False)

def to_xml(data):
    #Create a document and elements
    root = Element('root')
    stu = SubElement(root, 'student')
    #Create a comment
    stu.append(Comment(u' Student Info\n\t"id" : [Name, Math, Chinese, English]'))

    #Create text
    stu.text = data

    #Save to file
    tree = ElementTree(root)
    tree.write('student.xml', encoding = 'utf-8',  \
                         xml_declaration = True)

if __name__ == '__main__':
    data = read_xls(fromfile)
    to_xml(data)


