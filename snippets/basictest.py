# encoding: utf-8

a = [0, 1, 2, 3]
b = [7, 6, 5, 4]

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
myprint1((1, 2))
myprint1(*(1, 2))
myprint1([1, 2])
myprint1(*[1, 2])
print

#myprint2()
#myprint2(1)
#myprint2(1, 2)
myprint2((1, 2))
myprint2([1, 2])
print

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



def hello_english(): return "Hello"
def hello_hindi(): return "Namaskar"

hello = { 'english': hello_english, 'hindi': hello_hindi }

for language in ['english', 'hindi']:
    print "%s says %s" % (hello[language].__name__, hello[language]())
    print "%s also says %s" % (hello[language].func_name, hello[language]())

    




