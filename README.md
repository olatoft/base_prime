# Base Prime

[![Build Status](https://travis-ci.org/olatoft/base_prime.svg?branch=master)](https://travis-ci.org/olatoft/base_prime)

Number system using prime numbers as its base.

## Explanation

All numbers can be constructed by multiplying prime numbers. Base Prime is a number system where this property is used by making each position in a number indicate wether a prime is present or not. The number then consists of primes that can be multiplied together to form that number.

For example, the number 42 can be broken down to 2 * 3 * 7, the first, the second and the fourth prime number. Thus, Base Prime would represent this number as 1011.

This has the potential to make multiplication and divison really fast. For instance, 6 * 7 could be broken down to 11 OR 1000 = 1011 = 42

## Dependencies
  * Python 3

## Installation
```
git clone https://github.com/olatoft/base_prime.git
```

## Run
```
python3 Main.py
```
