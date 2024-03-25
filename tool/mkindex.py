#!/usr/bin/python3
#cSpell:locale en
#cSpell:words leckere rezepte onkeyup

import os
import datetime as dt
from utils import get_files,get_tags

IGNOREFILES = ["index.xml"]

def make_index():
    print("Scanning files...")

    path = os.path.join("src", "rezepte.html")
    outfile = open(path, "w", encoding="cp1252")
    last_update = dt.datetime.now()
    outfile.write("""<html>
<head>
    <title>Leckere Rezepte</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"></link>
    <link rel="stylesheet" href="style.css"></link>
</head>
<body bgcolor="white">
    <script type="text/javascript" src="rezepte.js"></script>
    <div class="menubar">
        <a href="rezepte.html"><i class="fa fa-fw fa-home"></i></a>
        <div>
        <i onclick="onSearch()" class="fa fa-fw fa-search"></i>
        <input id="searchBox" onkeyup="filterList()" style="display:none" type="text" placeholder="Search..">
        </div>
        <div>
        <i onclick="onSearchHashtag()" class="fa fa-fw fa-hashtag"></i>
        <input id="searchHashtagBox" onkeyup="filterHashtagList()" style="display:none" type="text" placeholder="Search..">
        </div>
    </div>
    <div class="main">
""")

    count = 0
    for filename in get_files("src"):
        count+=1
        tags = get_tags(os.path.join("src", filename))
        tag_string = ";".join(tags)
        outfile.write(f"<div class=\"recipe\" tags=\"{tag_string}\">")
        outfile.write(f"""<a href="{filename}">{filename.replace(".xml", "")}</a>""")
        outfile.write("</div>\n")
    outfile.write("""
    </div>""")

    outfile.write(F"""
    <div>
    Last Update: {last_update}
    </div>""")
    outfile.write("""
</body>
</html>""")

    outfile.close()

    print("Found " + str(count) + " files")

if __name__ == '__main__':
    make_index()
