import random
winning_number=random.randint(1,100)
# print("The winning number is:",winning_number)
# winning_number=48
guess=1
game_over = False
number=input("guess a number between 1 to 100 : ")
number=int(number)
while not game_over:
    if number==winning_number:
        print (f"you guessed it right and yoy gussed this in {guess} times")
        game_over=True
    else:
        if number<winning_number:
            print("Too low !!")
        else:
            print("too high !!")
            
            # Dry Principle
        guess+=1
        number = int(input("guess again : "))



