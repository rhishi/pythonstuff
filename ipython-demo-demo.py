"""A simple interactive demo to illustrate the use of IPython's Demo class.

To run it, start IPython and execute the following commands:

from IPython.lib.demo import Demo
demo = Demo('ipython-demo-demo.py')
while not demo.finished: demo()

Any python script can be run as a demo, but that does little more than showing
it on-screen, syntax-highlighted in one shot.  If you add a little simple
markup, you can stop at specified intervals and return to the ipython prompt,
resuming execution later.
"""

print 'Hello, welcome to an interactive IPython demo.'
print 'Executing this block should require confirmation before proceeding,'
print 'unless auto_all has been set to true in the demo object.'

# The mark below defines a block boundary, which is a point where IPython will
# stop execution and return to the interactive prompt.
# Note that in actual interactive execution,
# <demo> --- stop ---

x = 1
y = 2
print "x =", x, ", y =", y

# <demo> --- stop ---

# the mark below makes this block as silent
# <demo> silent

print 'This is a silent block, which gets executed but not printed.'

# <demo> --- stop ---
# <demo> auto
print 'This is an automatic block.'
print 'It is executed without asking for confirmation, but printed.'
z = x + y

print 'z =', z

# <demo> --- stop ---
# This is just another normal block.
z = z**2
print 'now z = ', z
print 'bye!'
