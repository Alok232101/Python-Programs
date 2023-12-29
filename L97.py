# generate list with range function
# index method
# pass list to a function

number=list(range(1,11))
print(number)
print(number.pop())
print(number.index(3))
print(number[5])

def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(number))
    