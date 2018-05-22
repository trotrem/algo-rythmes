def findSummingPair(array, total):
    if len(array) < 2:
        return False
    right = len(array) - 1
    left = 0
    while not right == left:
        numbers_sum =  array[right] + array[left]
        if numbers_sum == total:
            return True
        elif numbers_sum > total:
            right -= 1
        elif numbers_sum < total:
            left += 1
    return False

def findSummingPairWithSet(data, total):
    validCOmplements = set()
    for i in range(len(data)):
        if data[i] in validCOmplements:
            return True

        validCOmplements.add(total - data[i])
    return False
