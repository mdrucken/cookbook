#!/usr/bin/python3
#cSpell:locale en

import os
from lxml import etree
from utils import get_files

def make_tags():
    tags = {}
    for file in get_files("src"):
        file_name = os.path.join("src", file)
        try:
            doc = etree.parse(file_name)
            res = doc.xpath("//tag")
            for tag in res:
                if tag.text == None:
                    continue
                if tag.text in tags:
                    tags[tag.text].append(file)
                else:
                    tags[tag.text] = [file]
        except etree.ParseError as e:
            print(f"Parsing error in {file}:")
            print(f"{e}")
    print(f"Found {len(tags.keys())} tags")
    print(f"{tags}")

if __name__ == '__main__':
    make_tags()

