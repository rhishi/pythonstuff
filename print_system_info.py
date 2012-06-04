import sys
from types import *

def myprint(prefix, *args):
    print ("%-25s" % prefix),
    for a in args:
        if type(a) is list:
            print "\n  " + "\n  ".join(a)
        else:
            print a

myprint("sys.executable = ", sys.executable)

myprint("sys.version = ", sys.version)
myprint("sys.version_info = ", sys.version_info)

myprint("sys.platform = ", sys.platform)

myprint("sys.path = ", sys.path)




