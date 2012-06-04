import subprocess
import sys

class Command:
    exe = ''
    opt = ''
    def __init__(self, exe, opt):
        self.exe = exe
        self.opt = opt
    
    def run(self, *args):
        argstr = reduce(lambda x,y: x + ' ' + y, args)        
        cmdstr = "{0} {1} {2}".format(self.exe, self.opt, argstr)
        print cmdstr
        sys.stdout.flush()
        status = subprocess.call(cmdstr)
        return status

