#!/usr/bin/python3

import os

IGNOREFILES = ["index.xml"]

print("Scanning files...")

outfile = open("src\\rezepte.html", "w", encoding="ascii")

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
        <i onclick="onSearch()" class="fa fa-fw fa-search"></i>
        <input id="searchBox" onkeyup="filterList()" style="display:none" type="text" placeholder="Search..">
    </div>
    <div class="main">
""")

count = 0
for subdir, dirs, files in os.walk('src'):
    for filename in files:
        if filename in IGNOREFILES:
            continue

        if filename.endswith(".xml"):
            count+=1
            outfile.write("<div class=\"recipe\"> <a href=\"" + filename + \
                "\">" + filename.replace(".xml", "") + "</a></div>\n")

outfile.write("""
    </div>
</body>
</html>""")

outfile.close()

print("Found " + str(count) + " files")
