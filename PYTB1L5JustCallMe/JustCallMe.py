import sys

Leeftijd = 0
Geslacht = "Geslacht"
Haarkleur = "Kleur"
Tijd = 0

Leeftijd = sys.argv[1]
Geslacht = sys.argv[2]
Haarkleur = sys.argv[3]
tijd = sys.argv[4]

print("Hallo ik ben " + str(Leeftijd) + " jaar oud.")
print("Ik ben een " + Geslacht + " met " + Haarkleur + " haar.")
print("Het is nu " + str(tijd) + " uur.")