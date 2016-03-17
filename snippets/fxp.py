


def fxp(number, fractionalBits):
    """
    Returns a fixed point representation of a floating point number
    rounded to a given number of fractional bits.
    
    The returned value is a string of 1's and 0's and a dot.  The 
    substring on the left of the dot gives the binary representation
    of the integer part of the number.  The right substring gives
    the rounded fractional part.
    """
    scaled = number * 2 ** fractionalBits
    rounded = int(round(scaled))
    binaryStr = bin(rounded)
    binary = binaryStr[2:]   # remove "0b" prefix  
    wordlength = len(binary)
    integerBits = wordlength - fractionalBits
    if integerBits >= 0:
        return binary[:integerBits] + "." + binary[integerBits:]
    else:
        return "." + "0"*(-integerBits) + binary

data = [ 9.2, 1.0/3, 0.171875, 23.47 ]

# first print a row with our data.
print "  ",
for v in data:
    print "%-30f " % v,
print

# for each fractional bitwidth, print out the fxp strings for the data.
for f in [8, 9, 12, 15, 16, 24]:
    print "%2d" % f,
    for v in data:
        print "%-30s " % fxp(v, f),
    print


