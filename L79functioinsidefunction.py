def greater(a,b):
    if a>b:
        return a
    return b
print(greater(4,5))

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    return c
print(greatest(4,5,9))

def new_greatest(a,b,c):
    bigger =greater(a,b)
    return greater(bigger,c)

print(new_greatest(10,20,30))
    