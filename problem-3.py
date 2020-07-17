from math import sqrt


def isDivisable(num1, num2):
    result = num1 % num2 == 0
    return result

def isPrime(num):
    if num >= 1 and num <= 3:
        return True
    return sqrt(num) * sqrt(num) == num

def main():
    number = 600851475143
    factor = 1

    for count in range(3, int(sqrt(number))):
        if isDivisable(number, count) and isPrime(count):
            factor = count

    return factor

print(main())
