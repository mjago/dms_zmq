import sys
sys.path.append("/Users/martyn/.emacs.d/martyn/martyn/DMS/lib/")
import random
import unittest
import dms
 
reload (dms)

class TestSequenceFunctions(unittest.TestCase):
 
    def setUp(self):
        self.seq = range(10)

    def test_numbers_equality(self):
        self.assertEqual(2, 3 - 1)

    def test_numbers_inequality(self):
        self.assertNotEqual(2, 3 + 1)

    def test_string_equality(self):
        self.assertEqual("2", "2")
 
    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

    def test_fib_returns_correct_answer(self):
        self.assertEqual(dms.fib(1), [])
        self.assertEqual(dms.fib(2), [1, 1])
        self.assertEqual(dms.fib(3), [1, 1, 2])
        self.assertEqual(dms.fib(4), [1, 1, 2, 3])
        self.assertEqual(dms.fib(5), [1, 1, 2, 3])
        self.assertEqual(dms.fib(6), [1, 1, 2, 3, 5])
        self.assertEqual(dms.fib(7), [1, 1, 2, 3, 5])
        self.assertEqual(dms.fib(8), [1, 1, 2, 3, 5])
        self.assertEqual(dms.fib(9), [1, 1, 2, 3, 5, 8])
        self.assertEqual(dms.fib(0), [])
        self.assertEqual(dms.fib(-1), [])
    
    def test_return_twice(self):
        self.assertEqual(2, dms.return_double(1))
        self.assertEqual(4, dms.return_double(2))
        self.assertEqual(-40, dms.return_double(-20))
 
    def test_factorial(self):
        self.assertEqual(1, dms.factorial(0))
        self.assertEqual(1, dms.factorial(1))
        self.assertEqual(2, dms.factorial(2))
        self.assertEqual(6, dms.factorial(3))
        self.assertEqual(24, dms.factorial(4))
        self.assertEqual(120, dms.factorial(5))
        self.assertEqual(720, dms.factorial(6))
 
if __name__ == '__main__':
    unittest.main()
