import unittest
import myfft
from ddt import ddt, data, datalist

def myprint(x):
    print ["{0.real:.3g} + {0.imag:.3g}i".format(elm) for elm in x]   

@ddt
class DFTEqualsFFTTest(unittest.TestCase):
        
    def areEqual(self, x, y):
        if (len(x) != len(y)): return False
        for (a, b) in zip(x, y):
            if round(abs(a - b), 7) != 0: return False
        return True

    def dft_equals_fft_test(self, x):
        dft = myfft.dft(x)
        fft = myfft.fft(x)
        if len(x) < 10: print "fft - dft = ",
        if len(x) < 10: myprint([ x - y for (x, y) in zip(fft, dft)])
        self.assertTrue(self.areEqual(dft, fft), "dft does not match fft")

    @data ([ 1, -1, -1, 1 ], [ 0, 1, 0, 0 ])
    def test_vector1(self, x):
        self.dft_equals_fft_test(x)

    vectors = [[ 1, 0, 0, 0 ],
               [ 0, 1, 0, 0 ],
               [ 0, 0, 1, 0 ],
               [ 0, 0, 0, 1 ],
               [ 1, 1, 1, 1 ],
               [ 0, 0, 0, 0 ],
               [ 1, 2, 3, 4 ],
               range(0, 128),
               [-1, 1] * 256
               ]

    @datalist (vectors)
    def test_vector2(self, x):
        self.dft_equals_fft_test(x)

    def test_simple(self):
        self.dft_equals_fft_test([1, -1, 1, -1])

