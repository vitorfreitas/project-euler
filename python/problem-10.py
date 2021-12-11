from math import sqrt
from itertools import count

def isPrime(num):
    if num <= 2:
        return True
    for number in range(2, int(sqrt(num) + 1)):
        if num % number == 0:
            return False

    return True

def primeGenerator():
    for number in count(1):
        if isPrime(number):
            yield number

def main(limit):
    summedNumbers = 0

    for prime in primeGenerator():
        if prime == 1:
            continue
        if prime >= limit:
            break
        print(summedNumbers, prime)
        summedNumbers += prime

    return summedNumbers

print(main(2000000))
