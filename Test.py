import unittest
import Main

class TestConvert(unittest.TestCase):

    def setUp(self):
        self.converter = Main.Converter()

    def test_normal_convert(self):
        self.assertEqual(self.converter.convert(7), 1000)

    def test_faulty_convert(self):
        self.assertEqual(self.converter.convert(4), 'Error')

class TestPrimes(unittest.TestCase):

    def setUp(self):
        self.primes = Main.Primes()

    def test_is_prime(self):
        self.assertEqual(self.primes.is_prime(4), False)
        self.assertEqual(self.primes.is_prime(5), True)
        self.assertEqual(self.primes.is_prime(6), False)
        self.assertEqual(self.primes.is_prime(7), True)
        self.assertEqual(self.primes.is_prime(8), False)
        self.assertEqual(self.primes.is_prime(9), False)

    def test_generate_prime(self):
        self.assertEqual(self.primes.generate_prime(), 5)
        self.assertEqual(self.primes.generate_prime(), 7)
        self.assertNotEqual(self.primes.generate_prime(), 9)

if __name__ == '__main__':
    unittest.main()
