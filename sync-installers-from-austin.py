

class Package:
    src = ''
    dest = ''
    versions = []
    def __init__(self, src, dest, versions=[]):
        self.src = src
        self.dest = dest
        self.versions = versions

    def __str__(self):
        s = ''
        s += 'src : ' + self.src + '\n'
        s += 'dest: ' + self.dest + '\n'
        if len(self.versions) > 0: s += 'versions: ' + str(self.versions) + '\n'
        return s
        

packages = [
            #Package(r'\\nirvana\lvpublic\licensing\GetLicense',
            #        r'\\us-ber-bears\Software\Nirvana\GetLicense'),
            Package(r'\\nirvana\NISoftwareReleased\Windows\Distributions\LabVIEW Add-ons\FPGA IP Builder', 
                    r'\\us-ber-bears\Software\Nirvana\FPGA IP Builder'),
            Package(r'\\nirvana\NISoftwareReleased\Windows\Suites\LabVIEW Platform DVD',
                    r'\\us-ber-bears\Software\Nirvana\LabVIEW Platform DVD',
                    #['2010', '2010 SP1', '2011', '2011 SP1'])
                    ['2011/English', '2011 SP1/English'])
           ]

import subprocess
import sys
import os
    
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

path = 'C:\\cygwin\\bin\\'
#path = '/usr/bin/'
suffix = '.exe'
#suffix = ''

rsync = Command(path + 'rsync' + suffix, '-rltgod --delete')
rsyncprogress = Command(path + 'rsync' + suffix, '-rltgod --delete --progress')
rsyncdry = Command(r'C:\cygwin\bin\rsync.exe', '-rltgod --delete --progress --dry-run')
echo = Command(r'C:\cygwin\bin\echo.exe', '')

class SyncError(Exception):
    pass

def sync(src, dest):
    cmd = rsyncdry
    cmd = rsyncprogress
    #cmd = echo  
    src2 = "'" + src.replace('\\', '/') + '/' + "'"
    dest2 = "'" + dest.replace('\\', '/') + '/' + "'"
    if not os.path.exists(dest2):
        os.makedirs(dest2)
    status = cmd.run(src2, dest2)
    if (status != 0):
        raise SyncError
        
    

def sync_all():
    for package in packages:
        print package
        src = package.src
        dest = package.dest
        versions = package.versions
        if len(versions) == 0:
            sync(src, dest)
        else:
            for v in versions:
                sync(src + '\\' + v, dest + '\\' + v)


try:
    sync_all()
except SyncError:
    print 'Error syncing'
                
    

