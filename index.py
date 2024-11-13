# Guessing game 
import random


while True:

    number_ = random.randint (1, 10)

    user_input = int(input("Guess a number between 1-10: "))

    if user_input == number_ :
        print ('You Won!!!')

    elif user_input < 1 or user_input > 10:
        print("Error") 
    else :
            print('You guessed wrong..... Try again')
            print(number_)
            ans = str(input("Try again? Yes or No"))

            if(ans == "No"):
                break
            else:
                 continue