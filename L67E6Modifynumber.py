winning_number=48
guess=1
game_over =False
number=input("guess a number between 1 to 100 : ")
number=int(number)
while not game_over:
    if number==winning_number:
        print (f"you guessed it right and yoy gussed this in {guess} times")
        game_over=True
    else:
        if number<winning_number:
            print("Too low !!")
            guess+=1
            number = int(input("guess again : "))
        else:
            print("too high !!")
            guess+=1
            number = int(input("guess again : "))



