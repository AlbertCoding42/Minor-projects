# Cows and bulls guessing game:

from random import randint


def cowChecker(cows):
    for cow_index in range(0, 4):
        if guess[cow_index] == number[cow_index]:
            cows += 1
            guess_array[cow_index] = True
            number_array[cow_index] = True
        cow_index += 1
    print("Cows: " + str(cows))
    return guess_array
    return number_array


def bullChecker(bulls):
    bull_index = 0
    while bull_index < 4:
        while guess_array[bull_index] == True:
            bull_index += 1
        if bull_index > 3:
            break
        for i in range(0, 4):
            if guess[bull_index] == number[i] and number_array[i] == False:
                bulls += 1
                number_array[i] = True
                break
        bull_index += 1
    print("Bulls: " + str(bulls))


print("Welcome to the cows and bulls game!\nEnter a number as your first guess (The number is 4 digits long): ")
guesses = 1
guess = []
number = []
guess1 = input(">>> ")

# Random 4 digit number:
number1 = randint(1000, 9999)
# Chosen 4 digit number for testing:
number1 = 3759

# Converting guess and answer to lists:

for digit in str(guess1):
    guess.append(digit)
for digit in str(number1):
    number.append(digit)

while int(guess1) != number1:
    guess_array = [False, False, False, False, False]
    number_array = [False, False, False, False]
    cowChecker(0)
    bullChecker(0)
    guess1 = input("Enter another guess: \n>>> ")
    guesses += 1
    guess = []
    for digit in str(guess1):
        guess.append(digit)


print("You win!\nThe number is: " + str(number1))
print("You guessed " + str(guesses) + " times")
