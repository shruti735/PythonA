from os.path import isdir,curdir,abspath
from os import listdir
class DirFound(Exception):
    pass
def detect_dirs():
    for item in listdir(curdir):
        if isdir(item):
            raise DirFound(abspath(item))
        else:
            print(item)