class Converter():

	def __init__(self):
		pass

	def convert(self, base_ten_number):
		pass

class Primes():

	def __init__(self):
		self.primes = [2, 3]

	def generate_prime(self):
		number = self.primes[-1] + 2
		while True:
			if self.is_prime(number):
				self.primes.append(number)
				return number
			else:
				number += 2
			
	def is_prime(self, number):
		for divisor in self.primes:
			if divisor**2 > number:
				return True
			elif number % divisor == 0:
				return False

if __name__ == '__main__':
	converter = Converter()
	print (converter.convert(7))
