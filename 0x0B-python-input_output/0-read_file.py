#!/usr/bin/python3
"""read_file
"""


def read_file(filename=""):
    """Takes in str filename to read it and
    print to stdout
    """

    with open(filename, encoding="utf-8") as readFile:
        print(readFile.read(), end=''
    file.close())
