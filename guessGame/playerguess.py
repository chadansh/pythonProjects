import random

upperlimit = int(input("upper limit :"))
lowerLimit = 1
randChoice = random.randint(lowerLimit,upperlimit)
userChoice = ""
while upperlimit>1 and randChoice != userChoice:
    userChoice = int(input(f"choose random number from {lowerLimit} and {upperlimit} : "))
    if userChoice>randChoice:
        print("too high")
    elif userChoice<randChoice:
        print("too low")
    else :
        print(f"you win . number was {randChoice}")