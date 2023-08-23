#BMI kalkulator // kg/h^2

#Finn vekt og høyde
weight = input("Skriv inn vekten din: ")
height = input("Skriv inn høyden din: ")

#Gjør input om til int
weight = int(weight)
height = int(height)

#Isoler BMI som egen funksjon
bmi = (weight / height ** 2 * 10000)

#Print ut BMI
print  ("Din BMI er : ", bmi)

#Print ut hvor du ligger på skalaen
if bmi < 18 :
    print ("Du er undervektig")

if bmi > 25 :
    print ("Du er overvektig")

else:
    print ("Du er normalvektig")