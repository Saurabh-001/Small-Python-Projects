import random

name = input("Enter your name: ")

wins = 0
row_wins = 0

option = 'Y'
option_list = ['Y','N','y','n']

while option=='Y' or option=='y':
    number = random.randint(0,20)
    chance = 0
    won = 0
    print("Hello "+name+", you have 5 chances to guess the number")
    while chance<5:
        choice = int(input("Enter your number {}: ".format(chance + 1)))
        if choice == number:
            wins += 1
            row_wins += 1
            won += 1
            print("Hurray, You got that right.")
            print("You beat me ",wins," times and ",row_wins," times in a row.\n")
            break
        elif choice<number:
            print("Oops, Your number is too low.")
            chance += 1
        else:
            print("Oops, Your number is too high.")
            chance += 1
    if won==0:
        print("Oh no! You ran out of chances. The number was ",number,".\n")
        row_wins = 0
    option = input("Hey {}, Would you like to play again?(Y/N) ".format(name))
    while option not in option_list:
        option = input("Sorry, I didn't understand that.\n Would you like to play again?(Y/N) ")
print("Thank You ",name," for playing. Hope you enjoyed.")
exit("Now exiting...")
