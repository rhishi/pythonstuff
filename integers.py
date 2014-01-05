import sys

# In Python 2, there are two integer types: int, long.

# int is the underlying platform's signed integer type,
# either 32 or 64 bit, depending on the platform.

# sys.maxint gives the maximum value of int.  It is 2^31-1 or 2^63-1.

print "sys.maxint =  {0} =  {0:x}   {1}".format(sys.maxint, type(sys.maxint))

# There is no sys.minint, but it's simply -sys.maxint-1 as said in Python documentation
# http://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex

print "min int    = {0} = {0:x}   {1}".format(-sys.maxint-1, type(-sys.maxint-1))

print

# long is an integer type with unlimited range.  Python automatically
# switches over from int to long whenever there is overflow.

# That's why, there is no sys.maxlong.

# Python 3 even gets rid of sys.maxint, because it has just single
# integer type: int.  It actually behaves like 2's long i.e. has unlimited range.
# 3 has sys.maxsize, which loosely relates to 2's sys.maxint.
# http://docs.python.org/3.3/whatsnew/3.0.html#integers
# http://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

# Let's test the automatic switchover from int to long
# On 64-bit platform, the switchover point is between 2^63-1 and 2^63.

for i in range(1, 130):
    # make 2^i - 1, without spilling beyond i bits.
    n = (((1 << (i-1)) - 1) << 1) + 1
    print "2**{0:<3} - 1   is   {1:#35x}   {2}".format(i, n, type(n))
    print "2**{0:<3}       is   {1:#35x}   {2}".format(i, n+1, type(n+1))
print

print -1
print -1 & 0xFF
print -1 & 0xFFF


