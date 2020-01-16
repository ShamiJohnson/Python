#guess the number

import random
x = random.randint(1, 100)
#greeting
print("Hi, I'm thinking of a number between 1 and 100.")
print("Guess a number, and I will tell you")
print("if you are too high, too low, or got it right! Good luck!")

guessing = 0
while guessing<100: #while loop
    print('Take a guess!') #get input
    guess = input()
    guess = int(guess)
    guessing = guessing + 1
    
    #determining number
    if guess < x:
        print('Your guess is too low.')
    if guess > x:
        print('Your guess is too high.')
    if guess == x:
        print('Congratulations!')
        if guess == x:
            tries = str(guessing)  #finding number of tries
        print('You guessed my number and it only took you ' + tries + ' tries!') #final line
        break #loop end
