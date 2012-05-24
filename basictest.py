

a = [0, 1, 2, 3]
b = [7, 6, 5, 4]

print "%50s =" % "a", a
print "%50s =" % "b", b
print "%50s =" %                         "zip(a, b) ", zip(a, b)
print "%50s =" %                    "zip(*zip(a, b))",      zip(*zip(a, b))
print "%50s =" % "type of element of zip(*zip(a, b))", type(zip(*zip(a, b))[0])
print "%50s =" %                     "zip(zip(a, b))", zip(zip(a, b))
print "%50s =" %               "zip(*zip(zip(a, b)))", zip(*zip(zip(a, b)))

print "%50s =" % "[e for l in zip(*zip(a, b)) for e in l]", [e for l in zip(*zip(a, b)) for e in l]

x = [23, 24, 25, 26]
print "%50s =" % "[k for k in x for x in zip(*zip(a, b))]", [k for k in x for x in zip(*zip(a, b))]

print "%50s =" % "    [list(t) for t in zip(*zip(a, b))]     ", [list(t) for t in zip(*zip(a, b))]
print "%50s =" % "sum([list(t) for t in zip(*zip(a, b))], [])", sum([list(t) for t in zip(*zip(a, b))], [])

print "%50s =" % "reduce(lambda x,y: x+y, zip(*zip(a, b)))", reduce(lambda x,y: x+y, zip(*zip(a, b)))

print 'String with backslash \\ in it.'
print r'String with two backslashes \\ in it.'

def myprint1(*args):
    print "myprint1:",
    for a in args:
        print a, ';',
    print

def myprint2(args):
    print "myprint2:",
    for a in args:
        print a, ';',
    print

myprint1()
myprint1(1)
myprint1(1, 2)
myprint1([1, 2])

#myprint2()
#myprint2(1)
#myprint2(1, 2)
myprint2([1, 2])

import subprocess

print 'subprocess.call:'
subprocess.call(r'C:\cygwin\bin\bash.exe --version')
subprocess.call(r'C:\cygwin\bin\bash.exe --help')
subprocess.call(r'C:\cygwin\bin\bash.exe -c "echo Sa and An"')
subprocess.call(r'C:\cygwin\bin\echo.exe Sa and An and Fo')
subprocess.call(r"C:\cygwin\bin\ls.exe '/cygdrive/c/Program Files/'")
print

print 'subprocess.check_output:'
print subprocess.check_output(r'C:\cygwin\bin\bash.exe --version')

import os
print os.path.exists('C:/Users/')
print os.path.exists('//us-ber-bears/Software/')

if not os.path.exists('//us-ber-bears/Software/test'):
    os.makedirs('//us-ber-bears/Software/test')
