#!/usr/bin/env python3
cround = 0
while True:
    cround = cround + 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")
    if answer == 'Brian':
        print("correct")
        break
    elif cround==3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")

