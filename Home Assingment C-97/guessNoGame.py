import random
chances=0
number = random.randint(0,9)

playerName=input("Enter your name:")
print("Hello",playerName,"Welcome to number guessing game!")

 # we used random for generating random numbrs 
while chances < 5:
    guess = int(input("Enter a number: "))
    
    chances += 1

    if guess < number:
        print("Your guess is low! ")

    if guess > number:
        print("Your guess is high! ")    

    if number == guess:
        break

if number == guess:
    print("Congratulation! You guessed it correctly")
elif number!= guess:
    print("Oops! You lost")
    print("The right number is", number)