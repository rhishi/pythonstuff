import cmath
import math

print "Complex number basics:"
z = 2 + 3j
print "  z =", z
print "  z.real =", z.real
print "  z.imag =", z.imag
print "  abs(z) =", abs(z)
print "  cmath.phase(z) =", cmath.phase(z)
print "  cmath.polar(z) =", cmath.polar(z)
print "  cmath.conjugate(z) =", z.conjugate()
print "  cmath.rect(3.6, 0.98) =", cmath.rect(3.6, 0.98)
print ""

print "Printing complex numbers:"
z = 4 + 5j
# No in-built format specifier for complex numbers, but the following are good replacements.
print "  %5s %s" % ("z =", z)
print "  %-5s %f + %fi" % ("z =", z.real, z.imag)
print "  %5s %.2f + %.2fi" % ("z =", z.real, z.imag)
print "  %-5s %.0f + %.0fi" % ("z =", z.real, z.imag)
print "  {0:>5} {1.real:g} + {1.imag:g}i".format("z =", z)
print "  {0:5} {1.real:.2g} + {1.imag:.2g}i".format("z =", z)
print ""

print "4th roots of unity:"
for theta in [0, math.pi/2, math.pi, 3*math.pi/2, 2*math.pi]:
    z = cmath.rect(1, theta)
    print "  e^%fi = %15g + %15gi     its 4th power is %s" % (theta, z.real, z.imag, z**4)
print ""

print "4th roots of unity:"
for k in range(0, 5):
    theta = k * math.pi/2
    expr = "0"       if k == 0 else \
           "pi i/2"  if k == 1 else \
           "pi i"    if k == 2 else \
           "3pi i/2" if k == 3 else \
           "2pi i"   if k == 4 else \
           "%dpi i/2" % k
    expr = "e^{%s}" % expr
    z = cmath.rect(1, theta)
    print "  %-12s = %15g + %15gi     its 4th power is %s" % (expr, z.real, z.imag, z**4)
print ""

def roots_of_unity(n):
    """Returns an array of nth roots of unity."""
    for k in range(0, n):
        z1 = cmath.exp(2 * math.pi * k * 1j / n)
        z2 = cmath.rect(1, 2 * math.pi * k / n)
        print "{0},     {1.real:8.2g} + {1.imag:8.2g}i,     {1.real:8.2g} + {1.imag:8.2g}i".format(k, z1, z2)

roots_of_unity(4)
