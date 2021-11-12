def bereken_maandkosten():
    verzekering_per_maand = 23
    benzine_kosten_per_liter =  1.54
    liter_per_kilometer = 0.2 

    km_per_maand = input("Hoeveel KM rijd jij per maand?: ")

    maandkosten = (float(km_per_maand) * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand
    print ("Je maandkosten: " + str(maandkosten)[0:5])

while True:
    bereken_maandkosten()
    
