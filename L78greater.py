def greater(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    return c
print(greater(4,5,9))