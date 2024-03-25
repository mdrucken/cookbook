import os
from lxml import etree

IGNOREFILES = ["index.xml"]

def get_files(path):
    list = []
    for subdir, dirs, files in os.walk('src'):
        for filename in files:
            if filename in IGNOREFILES:
                continue

            if filename.endswith(".xml"):
                list.append(filename)
    return list

def get_tags(file_name):
    tag_list = []
    try:
        doc = etree.parse(file_name)
        res = doc.xpath("//tag")
        for tag in res:
            if tag.text == None:
                continue
            if tag.text in tags:
                tag_list.append(tag.text)
    except etree.ParseError as e:
        print(f"Parsing error in {file_name}:")
        print(f"{e}")
    return tag_list
    