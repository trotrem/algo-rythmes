
opening = {
    "{": 0,
    "[": 1,
    "(": 2
}

closing = {
    "}": 0,
    "]": 1,
    ")": 2
}

def isBalanced(expr):
    par_stack = []
    for par in expr:
        if par in opening:
            par_stack.append(opening[par])
        elif par in closing:
            if not par_stack:
                return False
            elif closing[par] == par_stack[-1]:
                par_stack.pop()
            else:
                return False
    if not par_stack:
        return True
    return False

if __name__ == '__main__':
    n = int(input())

    for t_itr in range(n):
        expression = input()
        if isBalanced(expression):
            print("YES")
        else:
            print("NO")
