# Er dette året et skuddår?

# Få input på ønsket år
input_år = int(input("Skriv inn ønsket år: "))

skuddår = (input_år % 4 == 0 and input_år % 100 != 0 )


print(input_år, skuddår)

