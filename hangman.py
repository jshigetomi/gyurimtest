import os
import time
import random

#I did this thing different

#list = ["shift","soda","guitar","game","watch","water","teacher","student","bottle"]
list = ["hello"]
chance = ["(lives)> ","♥ ","♥ ","♥ ","♥ ","♥ "]
def line():
    blanklines = []
    blank = ()
    userInput = ""
    chance = ["(lives)> ","♥ ","♥ ","♥ ","♥ ","♥ "]
    run = random.randint(0,len(list) - 1)
    blank = len(list[run])
    for m in range(0,blank):
        blanklines.append('_ ')
    answer = list[run]
    while True:
        os.system('cls')

        for h in chance:
            print(h, end="")
        print("\n")
        for i in blanklines:
            print(i, end="")
        print("\n")

        userInput = input("(Guess a letter)>")
        if userInput == "exit":
            break
        if len(userInput) == 0 or len(userInput) >= 2:
            print("Please enter only one letter.")
            time.sleep(1)
        elif userInput not in answer:
            print("wrong! try again")
            time.sleep(1)
            chance.remove(chance[1])
        elif userInput in answer:
            index = 0
            while userInput in answer and index < len(answer):
                if answer[index] == userInput:
                    blanklines[index] = userInput + " "
                index += 1
            print("Good job!")
            time.sleep(2)
        if '_ ' not in blanklines:
            os.system('cls')
            print("GOOD JOB! YOU WON!")
            time.sleep(2)
            break
        elif "♥ " not in chance:
            os.system('cls')
            print("GAME OVER")
            time.sleep(2)
            break
userInput = ""
while userInput != 'exit':
    os.system('cls')
    userInput = input("(Would you start the game? Enter yes or no.)>")
    os.system('cls')
    if userInput == 'yes':
        os.system('cls')
        userInput = input("You need to guess five alphabets to fill in the blank. You have five chances.")
        line()
    elif userInput == 'no':
        print("Good Bye")
        break
    else:
        print("Error incorrect input. Please try again.")

