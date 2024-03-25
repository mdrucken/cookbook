import os

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
