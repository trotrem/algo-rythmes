
ASCII_A = 65

def convertBase(b1, number, b2):
    isNegative = number[0] == "-"
    total = 0
    for i, n in enumerate(number[:(0 if isNegative else None):-1]):
        total += int(n) * b1**i
    maxpart = b2
    while maxpart < total:
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
