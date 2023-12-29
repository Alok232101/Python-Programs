x=5 #global_variable

def func():
    x=7 #local_variable
    return x

print(func())
print(x)