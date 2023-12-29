import random
num = int(random.random())
print(num)
# winnig_number=5
num1=input("Guess a number between 1 too 100 : ")
num1=float(num1)
if num1==num:
    print("You won the game!")
else:
    if num1 < num :
     print("Sorry, too low")
    else:
        print("Sorry, too high")