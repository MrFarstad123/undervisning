#BMI kalkulator // kg/h^2

#Finn vekt og høyde
weight = input("Skriv inn vekten din: ")
height = input("Skriv inn høyden din i meter: ")

#Gjør input om til int
weight = float(weight)
height = float(height)

#Isoler BMI som egen variabel
bmi = (weight / height ** 2)

#Print ut BMI
print  ("Din BMI er : ", bmi)

#Print ut hvor du ligger på skalaen
if bmi < 18 :
    print ("Du er undervektig")

if bmi > 25 :
    print ("Du er overvektig")

else:
    print ("Du er normalvektig")