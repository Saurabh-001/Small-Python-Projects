import random
import math

name = input("Enter your name: ")

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

maximum_chance = int(math.log2(upper_bound-lower_bound+1)) + 1

wins = 0
row_wins = 0

option = 'Y'
option_list = ['Y','N','y','n']

while option=='Y' or option=='y':
    number = random.randint(lower_bound,upper_bound)
    chance = 1
    won = 0
    print(f'Hello {name}, you have {maximum_chance} chances to guess the number')
    while chance<=maximum_chance:
        choice = int(input(f'Enter your number {chance}: '))
        if choice == number:
            wins += 1
            row_wins += 1
            won += 1
            print(f'Hurray, You got that right in {chance} chance.')
            print(f'You beat me {wins} times and {row_wins} times in a row.\n')
            break
        elif choice<number:
            print(f"Oops, Your number is too low.")
            chance += 1
        else:
            print(f"Oops, Your number is too high.")
            chance += 1
    if won==0:
        print(f"Oh no! You ran out of chances. The number was {number}.\n")
        row_wins = 0
    option = input(f'Hey {name}, Would you like to play again?(Y/N) ')
    while option not in option_list:
        option = input(f"Sorry, I didn't understand that.\n Would you like to play again?(Y/N) ")
print(f"Thank You {name} for playing. Hope you enjoyed.")
exit("Now exiting...")
