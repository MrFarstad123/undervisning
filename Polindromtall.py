# Polindromtall // Kan leses begge veiene

# Få input fra bruker
tall = input("Skriv inn et tall mellom 100 og 999; ")

# Reverser input for å bruke i sammenligning
tall_reverse = tall[::-1]

# Sjekk om tallet er ploindrom eller ikke
if tall == tall_reverse :
    print ("Dette er et polindrom.")
else :
    print ("Dette er ikke et polindrom.")