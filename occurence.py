import re


def getnoofoccurence(substring,string):
    findings=list(re.finditer(substring,string))
    return len(findings)


g=getnoofoccurence("s","ssaa")
print(g)

