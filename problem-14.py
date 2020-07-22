import time

def calcEven(num):
    return num / 2

def calcOdd(num):
    return 3 * num + 1

def calcCollatz(value):
    if value <= 1:
        return value
    if value % 2 == 0:
        return 1 + calcCollatz(calcEven(value))
    else:
        return 1 + calcCollatz(calcOdd(value))

def main():
    maxCallCount = 1
    highestNumber = 1
    for count in range(1000000, 1, -1):
        callCount = calcCollatz(count)
        if callCount > maxCallCount:
            highestNumber = count
            maxCallCount = callCount
    print(highestNumber, maxCallCount)

start = time.time()
main()
end = time.time()
print(end - start)
