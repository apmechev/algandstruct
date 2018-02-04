from algorithms.karatsuba import karatsuba
from random import randrange
import unittest

class testKarabutsa(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_karatsuba(self):
        a=randrange(1,1000000000)
        b=randrange(1,1000000000)
        if a*b !=karatsuba(a,b):
            raise("karatsuba failed for numbers"+str(a)+ " "+str(b))
    
    def test_100_examples(self):
        for i in range(100):
            a=randrange(1,1000000000)
            b=randrange(1,1000000000)
            if a*b !=karatsuba(a,b):
                raise("karatsuba failed for numbers"+str(a)+ " "+str(b))






















