# Basic Guessing game

secret_number = "34"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_number and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess a number between 1 to 50: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")