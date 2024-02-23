import random

def number_guessing_game():
    rand_number = random.randint(1, 20)

    print("Try to guess the number that is between 1 and 20")

    while True:
        guess = int(input("Enter your guess: "))
        
        if guess == rand_number:
            print("Good job! You guessed the number correctly!")
            break
        elif guess < rand_number:
            print("Too low. Guess again.")
        else:
            print("Too high. Guess again.")

number_guessing_game()
# comment
