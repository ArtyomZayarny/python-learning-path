import random

def showAttemptsLeft(attempts):
    print(f"You have {attempts} attempts remaining to guess the number")

def setAttempts(difficulty):
    attempts_count = 0
    if difficulty == 'easy':
        attempts_count = 10
    elif difficulty == 'hard':
        attempts_count = 5
    return attempts_count

def setRandomNumber():
    return random.randint(1, 100)

def getUserGuess():
    return int(input("Make a guess: "))

def compare_guess(u_guess, target_number):
    if u_guess > target_number:
        return 1
    elif u_guess < target_number:
       return -1
    else:
        return 0

print("Welcome to the Number Guessing Game!")
# thinking the random number in range from 1 to 100
my_number = setRandomNumber()

print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

game_over = False
#Set attempts
attempts = setAttempts(difficulty)
showAttemptsLeft(attempts)
while not game_over:
    # Ask user to guess number
    user_guess = getUserGuess()

    # Compare
    result = compare_guess(user_guess, my_number)

    # Win emmidiatly
    if result == 0:
        print(f"You got it!🤘 The answer was {my_number} 🚀")
        game_over = True
    else:
        if result == 1:
            print("Too high.👍")
        if result == -1:
            print("Too low.👎")
        attempts = attempts - 1

        if attempts == 0:
            game_over = True
            print("You've run out of guesses, you lose. 😭")
        else:
            print("Guess again.🙈")
            # Render attempts message
            showAttemptsLeft(attempts)





