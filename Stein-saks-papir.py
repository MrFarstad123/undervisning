# Stein, saks, papir

# Importer moduler som skal brukes
import random

# Lag en robot med tilfeldig output
bot = random.randint(0,2)

# Få input fra bruker
bruker = input("Skriv inn 0 for stein, 1 for saks, og 2 for papir: ")

bruker = int(bruker)
bot = int(bot)

# Sette opp spillet
if bruker == 2 :
    if bot == 0 : 
        print ("Du vinner!")
    if bot == 1 : 
        print("Bot vinner!")

if bruker == 1 :
    if bot == 2 : 
        print ("Du vinner!")
    if bot == 0 : 
        print("Bot vinner!")

if bruker == 0 :
    if bot == 1 : 
        print ("Du vinner!")
    if bot == 2 : 
        print("Bot vinner!")

if bruker == bot :
    print ("Uavgjort")

if bruker > 2 :
    print ("Prøv på nytt") 