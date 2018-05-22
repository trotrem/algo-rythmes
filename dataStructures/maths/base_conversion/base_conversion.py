
ASCII_A = 65

def convertBase(b1, number, b2):
    isNegative = number[0] == "-"
    total = 0
    for i in range(1 if isNegative else 0, len(number)):
        total += int(number[i]) * b1**(len(number) - i - 1)
    maxpart = b2
    while maxpart <= total:
        maxpart *= b2
    maxpart /= b2
    newNumber = ["-" if isNegative else ""]
    while maxpart >= 1:
        multiplier = int(total // maxpart)
        if multiplier >= 10:
            multiplier = chr(multiplier - 10 + ASCII_A)
        total = total % maxpart
        newNumber.append(str(multiplier))
        maxpart //= b2
    return "".join(newNumber)
