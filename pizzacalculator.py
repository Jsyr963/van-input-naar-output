#John Youssef Pizza Calculator

prijslarge = 12.49
prijsmedium = 10.49
prijssmall = 6

small = int(input(f"hoeveel small pizza's wilt u hebben ? (€{prijssmall}) : "))
medium = int(input(f"hoeveel medium pizza's wilt u hebben ? (€{prijsmedium}) : "))
large = int(input(f"hoeveel large pizza's wilt u hebben ? (€{prijslarge}) : "))

print (f"Je bestelling is in Totaal €{round((prijssmall * small) + (prijsmedium * medium) + (prijslarge * large), 2)}, kies een betaalmethode : ")