def play():
    name = input("Name : ").capitalize()
    character = input("Character : ").lower()
    gender = input("Gender : ")
    pronoun = input("Pronounce His / Her : ").capitalize()
    pronounLower = pronoun.lower()
    bodyPart = input("Bodypart : ")
    dayTime =input("Daytime : ")
    weapon=input("Name a Weapon : ")
    genre=input("Genre you like : ")
    paragraph = f"{name} is a {character} {gender} . {pronoun} brain lies in {pronounLower} {bodyPart}. He studies at {dayTime}.\
        He murder everyone with {weapon} and then he watch {genre} show/movies. And after he finish watching movie/shows.\
        He buries the dead bodies in the ground.  "
    print(paragraph)

start = input ("Are you ready | 'y'=yes and 'n'=no :  ").lower()
if start == 'y':
    play()
    while True:
        again = input("Do you want to play again. 'y' or 'n' =").lower()
        if again == 'y':
            play()
        else:
            break    
else:
    print("Come back again")
    