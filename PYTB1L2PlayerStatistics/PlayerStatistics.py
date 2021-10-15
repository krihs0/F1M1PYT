import random
import time
import keyboard
import os

power_list = ['Teleportation','Psychic Abilities','Superspeed','Superstrength','Flight','Superintelligence']

Age = random.randint(14,34)
Jumpforce = random.randint(0,20)
Power = random.choice(power_list)
Power2 = random.randint(1,3)
Speed = random.randint(50,150)
Strenght = random.randint(50,150)
Intelligence = random.randint(50,150)
CookingLevel = random.randint(1,5)
Charisma = random.randint(1,10)


if Power == "Superspeed":
    Speed = 500
elif Power == "Superstrength":
    Strenght = 500
elif Power == "Superintelligence":
        Intelligence = 500
if Power2 == 2:
    print("Wow! You're extremely lucky! You have been born with an additional power!")
    Power2 = random.choice(power_list)
time.sleep(2)
   
print("Hello, what is your name?")
Name = input("Name: ")
print("If you want to know your stats press A")
while True:
    if keyboard.is_pressed("a"):
        os.system("cls")
        print("Name: " + Name)
        print("Age: " + str(Age))
        print("Power: " + Power)
        for x in power_list:
            if x == Power2:
                print("Second power: " + Power2)
        print("Speed: " + str(Speed))
        print("Strength: " + str(Strenght))
        print("Intelligence: " + str(Intelligence))
        print("Jumpforce: " + str(Jumpforce))
        print("Cooking: " + str(CookingLevel) + " Stars")
        print("Charisma: " + str(Charisma))
        print("Press B to end the program!")
    if keyboard.is_pressed("b"):
        print("Goodbye!")
        time.sleep(1)
        exit()
