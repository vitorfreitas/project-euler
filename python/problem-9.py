from math import sqrt
from itertools import count

for number1 in count(1):
    for number2 in count(2):
        number1square = number1 * number1
        number2square = number2 * number2
        number3square = number1square + number2square
        number3 = sqrt(number3square)

        if number1 > number2:
            continue

        if number1 + number2 + number3 > 1000:
            break

        if number1 + number2 + number3 == 1000:
            print(number1, number2, number3, number1 * number2 * number3)
