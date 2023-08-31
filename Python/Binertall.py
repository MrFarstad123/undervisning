# Tall til binærtall

# Få tall fra bruker
start_tall = int(input("Skriv inn et tall mellom 1 og 15: "))

# Idiotsikkre koden
if start_tall < 0 :    
    quit()

if start_tall > 15 :
    quit()

# Gjør om til binær
binær_tall = bin(start_tall)

# Print resultat
print ("Det binære tallet for", start_tall, " er ",  binær_tall)