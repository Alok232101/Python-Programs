# function returning two values
def fun(int1,int2):
    add = int1 + int2
    multiply = int1 * int2
    return (add,multiply)
# calling the function and printing the returned values
print(fun(5,7))

add,multiply =fun(2,3)
print("The sum is: ",add,"\nThe product is :",multiply)