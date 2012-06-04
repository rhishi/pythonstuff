import os
import sys
from command import Command

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
            Package(r'\\nirvana\lvpublic\licensing\GetLicense',
                    r'\\us-ber-bears\Software\Nirvana\GetLicense'),
            Package(r'\\nirvana\NISoftwareReleased\Windows\Distributions\LabVIEW Add-ons\Unit Test Framework',
                    r'\\us-ber-bears\Software\Nirvana\Unit Test Framework',
                    ['2011']),
            Package(r'\\nirvana\NISoftwareReleased\Windows\Distributions\LabVIEW Add-ons\FPGA IP Builder', 
                    r'\\us-ber-bears\Software\Nirvana\FPGA IP Builder'),
            Package(r'\\nirvana\NISoftwareReleased\Windows\Distributions\Device Drivers', 
                    r'\\us-ber-bears\Software\Nirvana\Device Drivers',
                    ['2012']),
            Package(r'\\nirvana\NISoftwareReleased\Windows\Suites\LabVIEW Platform DVD',
                    r'\\us-ber-bears\Software\Nirvana\LabVIEW Platform DVD',
                    #['2010', '2010 SP1', '2011', '2011 SP1'])
                    ['2011/English', '2011 SP1/English'])
           ]

class SyncError(Exception):
    pass


def sync(src, dest, synccmd):
    src2 = "'" + src.replace('\\', '/') + '/' + "'"
    dest2 = "'" + dest.replace('\\', '/') + '/' + "'"
    if not os.path.exists(dest2):
        os.makedirs(dest2)
        if not os.path.exists(dest2): raise SyncError
    status = synccmd.run(src2, dest2)
    if (status != 0):
        raise SyncError
        

prefix = ''
suffix = ''
if 'cygwin' in sys.platform:
    prefix = '/usr/bin/'
    suffix = ''
else:
    prefix = 'C:\\cygwin\\bin\\'
    suffix = '.exe'

rsyncpath = prefix + 'rsync' + suffix
echopath = prefix + 'echo' + suffix

rsync = Command(rsyncpath, '-rlt --delete')
rsyncprogress = Command(rsyncpath, '-rlt --delete --progress')
rsyncdry = Command(rsyncpath, '-rlt --delete --progress --dry-run')
echo = Command(echopath, '')


def sync_all():
    synccmd = rsyncprogress
    for package in packages:
        print package
        src = package.src
        dest = package.dest
        versions = package.versions
        if len(versions) == 0:
            sync(src, dest, synccmd)
        else:
            for v in versions:
                sync(src + '\\' + v, dest + '\\' + v, synccmd)


try:
    sync_all()
except SyncError:
    print 'Error syncing'
                
    

