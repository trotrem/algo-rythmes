def array_left_rotation(a, n, k):
    result = [None] * n
    for i in range(n):
        nextRotated = a[(i - k)%n]
        result[(i - k)%n] = a[i]
    return result

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
