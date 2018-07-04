import re

var=input("string")


def isvalid(string):
    found=re.match("[_A-Za-z][_a-zA-Z0-9]*",string)
    return bool(found)
test=isvalid(var)
print(test)