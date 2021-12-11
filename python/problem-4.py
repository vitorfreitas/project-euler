def isPalindromic(number):
    stringArray = list(str(number))
    if len(stringArray) % 2 != 0:
        return False
    halfString = len(stringArray) / 2
    firstSlice = stringArray[0:halfString]
    lastSlice = stringArray[halfString:len(stringArray)]
    firstString = "".join(firstSlice)
    lastString = "".join(lastSlice[::-1])

    return firstString == lastString

biggerPalindromicNumber = 1

for firstCounter in range(999, 1, -1):
    for secondCounter in range(999, 1, -1):
        product = firstCounter * secondCounter
        if (isPalindromic(product) and product > biggerPalindromicNumber):
            biggerPalindromicNumber = product

print(biggerPalindromicNumber)


