import random
def game():
    x = random.randint(1, 100)
    guessCount =0
    print("I the mainframe have chosen a number between 1-100.\nGuess it to win.")

    while True:
        #Special Thanks To GamerBruh for fixing my code
        try:
            guess = int(input())
        except:
            print("numbers buddy numbers")
            game()
         #Special Thanks To GamerBruh for fixing my code   
        #Debuging
        if guess == 999:
            print(x)
        #Debuging
        if guess == x:
            guessCount+= 1
            print("Congratulations you have guessed correctly. You guessed it in ",guessCount," tries")
            regame = input("do you want to play again")
            if regame == "yes":
                game()
            else:
                break
        else:
            guessCount+= 1
            if guess < x:
                print("Wrong! Try guessing higher.")
                continue
            if guess > x:
                print("Wrong! Try guessing lower.")
                continue   
game()
