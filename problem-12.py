from itertools import count

memo = {}

def sumNumberUntilZero(cur, num):
    if num == 0:
        return cur
    if memo.get(num):
        return cur + memo.get(num)
    return sumNumberUntilZero(cur + num, num - 1)

def triangularNumberGenerator():
    for number in count(1):
        num = sumNumberUntilZero(0, number)
        memo[number] = num
        yield num

highestDivisorCount = 0
for number in triangularNumberGenerator():
    divisorsCount = 0
    for inner in range(1, number + 1):
        if number % inner == 0:
            divisorsCount += 1
    highestDivisorCount = max(highestDivisorCount, divisorsCount)
    if highestDivisorCount >= 500:
        print(number, highestDivisorCount)
        break

