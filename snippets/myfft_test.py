import unittest
import myfft
from ddt import ddt, data, dataproduct

def myprint(x):
    print ["{0.real:.3g} + {0.imag:.3g}i".format(elm) for elm in x]

@ddt
class myfft_test(unittest.TestCase):
        
    def areEqual(self, x, y):
        if (len(x) != len(y)): return False
        for (a, b) in zip(x, y):
            if round(abs(a - b), 7) != 0: return False
        return True

    def dft_equals_fft_r2(self, x):
        dft = myfft.dft(x)
        fft = myfft.fft_r2(x)
        if len(x) < 10:
            print "fft - dft = ",
            myprint([ x - y for (x, y) in zip(fft, dft)])
        self.assertTrue(self.areEqual(dft, fft), "dft does not match fft radix-2")

    def dft_equals_fft_r4(self, x):
        dft = myfft.dft(x)
        fft = myfft.fft_r4(x)
        if len(x) < 10:
            print "fft - dft = ",
            myprint([ x - y for (x, y) in zip(fft, dft)])
        self.assertTrue(self.areEqual(dft, fft), "dft does not match fft radix-4")

    def dft_equals_fft_variant(self, x, variant):
        print "Checking %s on array of length %d" % (variant.__name__, len(x))
        dft = myfft.dft(x)
        fft = variant(x)
        self.assertTrue(self.areEqual(dft, fft), "dft does not match fft %s" % variant)

    @data ([ 1, -1, -1, 1 ], [ 0, 1, 0, 0 ])
    def test_vector1(self, x):
        self.dft_equals_fft_r2(x)

    vectors = [[ 1, 0, 0, 0 ],
               [ 0, 1, 0, 0 ],
               [ 0, 0, 1, 0 ],
               [ 0, 0, 0, 1 ],
               [ 1, 1, 1, 1 ],
               [ 0, 0, 0, 0 ],
               [ 1, 2, 3, 4 ],
               [ 0, 0, 1, 1, 1, 1, 0, 0 ],
               range(0, 128),
               [-1, 1] * 256
               ]

    variants = [ myfft.fft_r2_cryptic, myfft.fft_r2_simple, myfft.fft_r4_cryptic, myfft.fft_r4_simple, myfft.realfft ]
    
    @data (*vectors)
    def test_dft_equals_fft_r2(self, x):
        self.dft_equals_fft_r2(x)

    @data (*vectors)
    def test_dft_equals_fft_r4(self, x):
        self.dft_equals_fft_r4(x)

    @dataproduct (vectors, variants)
    def test_dft_equals_fft_variant(self, tupl):
        self.dft_equals_fft_variant(*tupl)

    def test_simple(self):
        self.dft_equals_fft_r2([1, -1, 1, -1])

