name=input("Enter your name : ")
count=0
i=0
while i<len(name):
    print(f"{name[i]} : {name.count(name[i])}")
    i+=1
