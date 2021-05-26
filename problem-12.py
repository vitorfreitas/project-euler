def triangularNumberGenerator(init):
    triangle = 1
    while True:
        init += 1
        triangle = triangle + init
        yield triangle

highestDivisorCount = 0
for number in triangularNumberGenerator(1):
    divisorsCount = 0
    for inner in range(1, number + 1):
        if number % inner == 0:
            divisorsCount += 1
    highestDivisorCount = max(highestDivisorCount, divisorsCount)
    if highestDivisorCount >= 500:
        print(number, highestDivisorCount)
        break

