
ASCII_A = ord('A')


def convertToBase10(b1, number, isNegative):
    total = 0
    for i in range(1 if isNegative else 0, len(number)):
        numPart = int(number[i]) if number[i].isdigit() else ord(number[i].upper()) - ASCII_A + 10
        total += numPart * b1**(len(number) - i - 1)
    return total

def findHighestSmallerPower(base10, b2):
    maxPower = b2
    while maxPower <= base10:
        maxPower *= b2
    return maxPower / b2

def convertFromBase10(base10, b2, isNegative):
    maxPower = findHighestSmallerPower(base10, b2)
    newNumber = ["-" if isNegative else ""]
    while maxPower >= 1:
        multiplier = int(base10 // maxPower)
        if multiplier >= 10:
            multiplier = chr(multiplier - 10 + ASCII_A)
        base10 = base10 % maxPower
        newNumber.append(str(multiplier))
        maxPower //= b2
    return "".join(newNumber)


def convertBase(b1, number, b2):
    isNegative = number[0] == "-"
    base10 = convertToBase10(b1, number, isNegative)
    return convertFromBase10(base10, b2, isNegative)
