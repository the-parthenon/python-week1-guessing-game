"""A number-guessing game."""

from random import randint

player_name = input("Welcome!  What can I call you?\n")

target_number = randint(1, 100)

print(player_name + ", I'm thinking of a number between 1 and 100.\nTry to guess the number.")

# print("Target number: " + str(target_number))

player_guess = 0
guess_count = 1

while target_number != player_guess:
    player_guess = int(input("What's your guess\n"))
    if player_guess > target_number:
        guess_count += 1
        print("Too high!  Try again.\n")
    elif player_guess < target_number:
        guess_count += 1
        print("Too low!  Take another stab at it.\n")


print("You got it! The number was " + str(target_number) + " and you got it in " + str(guess_count) + " guesses!")