import time
import keyboard
import os


vers1 = "Ik ben Kris ik eet soms vis."
vers2 = "Ik woon in Heerhugowaard en rij niet op een paard."
vers3 = "Ik speel minecraft en ik ben cracked."


print(vers1)
print(vers2)
print(vers3)
time.sleep(5)
Main = True
print("Press A to exit")
while Main:
    if keyboard.is_pressed("a"):
        os.system("cls")
        print("Goodbye!")
        time.sleep(2)
        exit()
