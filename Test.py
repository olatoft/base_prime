import unittest
import Main

class TestConvert(unittest.TestCase):

	def setUp(self):
		self.converter = Main.Converter()

	def test_convert(self):
		self.assertEqual(self.converter.convert(7), 1000)

if __name__ == '__main__':
	unittest.main()
