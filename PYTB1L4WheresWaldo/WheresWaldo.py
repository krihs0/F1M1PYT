import random
import time
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)

Check = 0

while True:
    if people[Check] == "Waldo":
        print("Waldo is gevonden op stoel " + str(Check + 1))
        time.sleep(50)
    else:
        print("Waldo zit niet op stoel " + str(Check + 1))
        Check = Check + 1
