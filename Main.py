class Converter():

    def __init__(self):
        pass

    # Converts a number from base 10 to base prime
    # Input: int base_ten_number, the number in base 10 which should be
    # converted
    # Ouput: int base_prime_number, the converted number in base prime
    def convert(self, base_ten_number):
        base_prime_text = ''


class Primes():

    def __init__(self):
        self.prime_list = [2, 3]

    # Generates the next prime after those already in prime_list, and adds it
    # to prime_list
    # Ouput: int number, which is the next prime
    def generate_prime(self):
        number = self.prime_list[-1] + 2
        while True:
            if self.is_prime(number):
                self.prime_list.append(number)
                return number
            else:
                number += 2

    # Help method for generate_prime
    # Input: int number, which may or may not be prime
    # Output: boolean, true if the number is prime, false otherwise
    def is_prime(self, number):
        for divisor in self.prime_list:
            if divisor**2 > number:
                return True
            elif number % divisor == 0:
                return False


if __name__ == '__main__':
    converter = Converter()
    print(converter.convert(7))
