def play():
    name = input("Name : ").capitalize()
    character = input("Character : ").lower()
    gender = input("Gender : ")
    pronoun = input("Pronounce His / Her : ").capitalize()
    bodyPart = input("Bodypart : ")
    dayTime =input("Daytime : ")
    paragraph = f"{name} is a {character} {gender} . {pronoun} brain lies in  {bodyPart}. He study at {dayTime}"
    print(paragraph)

start = input ("Are you ready | 'y'=yes and 'n'=no :  ").lower()
if start == 'y':
    play()
    while True:
        again = input("Do you want to play again. 'y' or 'n' =").lower()
        if again == 'y':
            play()
else:
    print("Come back again")
    