from random import randint
print("Welcome to the Guess the Number game!")
secret_number = randint(1, 100)
print("I'm thinking of a number between 1 and 100. Can you guess it?")
guess = None
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    if guess > secret_number:
        print("Your guess is too high. Try again.")
    elif guess < secret_number:
        print("Your guess is too low. Try again.")
    else:
        print("Congratulations! You've guessed the correct number:", secret_number)