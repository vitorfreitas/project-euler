dividers = range(20, 0, -1)
number = dividers[0] + dividers[0]
minDivider = 1

while minDivider == 1:
    for counter in dividers:
        if number % counter != 0:
            number += 20
            break
        if counter == dividers[-1]:
            minDivider = number

print(minDivider)
