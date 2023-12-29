age=int(input("Enter your age : "))
if age<=0:
    print("Invalid Age !!!!")
elif age>=1 and age<=3:
    print("Your Ticket is free !! ")
elif age>=4 and age<=10:
    print("Your Ticket price is 150 !! ")
elif age>=11 and age<=60:
    print("Your Ticket price is 250 !! ")
else:
    print("Your Ticket price is 200 !! ")