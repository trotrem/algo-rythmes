ASCII_0 = ord('0')

def digitToChar(digit):
    return chr(ASCII_0 + digit)

def intToString(integer):
    sign = "" if integer >= 0 else "-"
    integer = abs(integer)
    string = []
    while integer > 0:
        string.append(digitToChar(integer%10))
        integer = integer // 10
    string.append(sign)
    if(len(string) == 1):
        string = ["0"]
    return "".join(reversed(string))

def charToDigit(char):
    return ord(char) - ASCII_0

def stringToInt(string):
    sign = -1 if string[0] == "-" else 1
    start = 0 if sign == 1 else 1
    integer = 0
    for i in range(start, len(string)):
        integer *= 10
        integer += charToDigit(string[i])
    return integer * sign
