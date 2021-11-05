import datetime
import time
import os

#open file with python cmd thingy it doesnt work in the editor terminal

date = datetime.datetime.now()
name = "name"

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

while True:
    def intro():
        print("Hello you!, ik ben Kris.") 
        time.sleep(1)
        print("Wie ben jij?")
        time.sleep
        name = str(input("Naam: "))
        time.sleep(1)
        print("Hello " + name)
        time.sleep(1)
        print("De datum en tijd is: " + str(date.date) + "en " + str(date.time))
        time.sleep(3)
        os.system("cls")
    intro()
    
    def outro():
        print(name + " wil jij dit programma nog een keer doen?") 
        while True:
            answeroutro = input("Type Y/N: ")
            if answeroutro == "Y" or answeroutro == "y":
                print ("Restarting...")
                time.sleep(1)
                os.system("cls")
                intro()
            elif answeroutro == "N" or answeroutro == "n":
                print("stopping...")
                time.sleep(1)
                exit()
            else:
                print("Antwoord niet herkend")

    def leeftijd():
        print("Hoe oud ben ik?")
        print("A: 8")
        print("B: 67")
        print("C: 16")
        while True:
            answerleeftijd = input("Antwoord: ")
            if answerleeftijd == "C" or answerleeftijd == "c" or str(answerleeftijd) == "16":
                print("Klopt ik ben inderdaad 16.")
                time.sleep(3)
                os.system("cls")
                break
            else:
                print("Nee, ik ben 16.")
                time.sleep(3)
                os.system("cls")
                break
    leeftijd()

    def woonplaats():
        print("Waar woon ik?")
        print("A: Hoorn")
        print("B: Heerhugowaard")
        print("C: Castricum")
        while True:
            answerwoonplaats = input("Antwoord: ")
            if answerwoonplaats == "B" or answerwoonplaats == "b" or answerwoonplaats == "Heerhugowaard":
                print("Klopt ik woon inderdaad in Heerhugowaard.")
                time.sleep(3)
                os.system("cls")
                break

            else:
                print("Nee, ik woon in Heerhugowaard.")
                time.sleep(3)
                os.system("cls")
                break
    woonplaats()

    def skateboarden():     #aaaaa
        print(color.BOLD + "Skateboarden" + color.END)
        print("Ik Skateboard nu ongeveer 5 maanden. In die 5 maanden heb ik heel wat")
        print("dingen gedaan. Het eerste wat ik had gedaan was indroppen, vanuit daar ")
        print("ging ik trucjes op de rand van de ramp doen waar ik nu ook een")
        print("een paar van kan. Naast de ramp heb ik ook nog wat op de grond gedaan")
        print("waaronder olies en shuv-it’s.")
        time.sleep(5)
        print("tijd over: 15")
        time.sleep(5)
        print("tijd over: 10")
        time.sleep(5)
        print("tijd over: 5")
        time.sleep(4)
        print("Bedankt voor het lezen!")
        time.sleep(1)
        os.system("cls")
        outro()

    def Gamen():        #aaa
        print(color.BOLD + "Gamen" + color.END)
        print("Ik doe al een lange tijd aan gamen. Ik denk dat de eerste game die ik")
        print("speelde op de ipad gewees zal zijn. Ik weet niet welke de eerste was maar ik")
        print("speelde heel lang clash of clans, ik was daarbij altijd in competitie met")
        print("mijn vader die het ook speelde. Pas na 4 jaar had ik hem ingehaald. De eerste pc game")
        print("is waarschijnlijk lego Harry Potter wat ik vaak samen met mijn vader achter de laptop")
        print("speelde. In 2013 begon ik met Minecraft spelen wat ik nu nogsteeds")
        print("speel en waarschijnlijk nog heel lang zal blijven spelen.")
        time.sleep(5)
        print("tijd over: 20")
        time.sleep(5)
        print("tijd over: 15")
        time.sleep(5)
        print("tijd over: 10")
        time.sleep(5)
        print("tijd over 5")
        time.sleep(4)
        print("Bedankt voor het lezen!")
        time.sleep(1)
        os.system("cls")
        outro()

    def Slapen():       #aaaa
        print(color.BOLD + "Slapen" + color.END)
        print("Ik hou erg van slapen. Het rust je uit mentaal en fysiek. Ook ligt")
        print("een bed best comfortabel wat ik helemaal niet erg vindt.")
        print("Het jammere is, is dat school mij weghoudt van mn slaap.")
        time.sleep(5)
        print("tijd over: 10")
        time.sleep(5)
        print("tijd over 5")
        time.sleep(4)
        print("Bedankt voor het lezen!")
        time.sleep(1)
        os.system("cls")
        outro()

    def hobby():
        print("Over welke hobby wilde je iets weten")
        print("A: Skateboarden")
        print("B: Gamen")
        print("C: Slapen")
        while True:
            answerhobby = input("Antwoord: ")
            if answerhobby == "A" or answerhobby == "a" or answerhobby == "Skateboarden":
                print("Goede keuze!")
                time.sleep(1)
                os.system("cls")
                skateboarden()
            elif answerhobby == "B" or answerhobby == "b" or answerhobby == "Gamen":
                print("Goede keuze!")
                time.sleep(1)
                os.system("cls")
                Gamen()
            elif answerhobby == "C" or answerhobby == "c" or answerhobby == "Slapen":
                print("Goede keuze!")
                time.sleep(1)
                os.system("cls")
                Slapen()
            else:
                print("Antwoord niet herkend")
            

    def hobbys():
        print("Wilde je nog iets over mijn hobbies weten?")
        while True:
            answerhobbys = input("Type Y/N: ")
            if answerhobbys == "Y" or answerhobbys == "y":
                os.system("cls")
                hobby()
            elif answerhobbys == "N" or answerhobbys == "n":
                print("jammer")
                time.sleep(2)
                outro()
            else:
                print("Antwoord niet herkend")
    hobbys()