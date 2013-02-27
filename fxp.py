


def fxp(number, fractionalBits):
  scaled = number * 2 ** fractionalBits
  rounded = int(round(scaled))
  binaryStr = bin(rounded)
  binary = binaryStr[2:]
  wordlength = len(binary)
  integerBits = wordlength - fractionalBits
  integer = binary[:integerBits]
  fraction = binary[integerBits:]
  return integer + "." + fraction


data = [ 9.2, 1.0, 0.5, 23.25 ]

for v in data:
  for f in [8, 10, 16, 24]:
    print "%30s " % fxp(v, f),
  print


