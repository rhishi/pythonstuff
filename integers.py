import sys

print "{0} = {0:x}".format(sys.maxint)

# there is no sys.maxlong, because longs are of unlimited size!

for i in range(1, 130):
    n = (1 << i) - 1
    print "2**{0:<3} - 1   is   {1:#35x}   {2}".format(i, n, type(n))
    print "2**{0:<3}       is   {1:#35x}   {2}".format(i, n+1, type(n+1))

print -1
print -1 & 0xFF
print -1 & 0xFFF


