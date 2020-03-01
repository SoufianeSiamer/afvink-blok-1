def berekening():
    afstand = float(input("Geef de afstand aan: "))
    omzetting= afstand * 0.6214
    print(omzetting)
berekening()

#opdracht 15

def main():
    print(calc_average())

def calc_average():
    cijfer1= int(input("geef cijfer 1 op: "))
    cijfer2= int(input("geef cijfer 2 op: "))
    cijfer3= int(input("geef cijfer 3 op: "))
    cijfer4= int(input("geef cijfer 4 op: "))
    cijfer5= int(input("geef cijfer 5 op: "))
    average= (cijfer1+cijfer2+cijfer3+cijfer4+cijfer5)/5
    print(average)

def determine_grade(arg):
    cijferbepaal= int(input("geef je cijfer op"))
    if cijferbepaal >=90:
        print("A")
    elif cijferbepaal >= 80 and cijferbepaal <=89:
        print ("B")
    elif cijferbepaal >= 70 and cijferbepaal <=79:
        print("C")
    elif cijferbepaal >= 60 and cijferbepaal <=69:
        print("D")
    else:
        print("F")


main()

def main():

    print(kinetic_energy())

def kinetic_energy():
    mass= int(input("wat is de massa van het object: " ))
    velocity= int(input("wat is de snelheid van het object: "))
    kin= 0.5*(mass*(velocity**2))
    return kin


main()

def priem():
    num = int(input("geef een getal op: "))  
  
    if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               print(num,"is geen priemgetal")   
               break  
       else:  
           print(num,"is een priemgetal")  
         
    else:  
       print(num,"is geen priemgetal")
priem()

def getal():
    from random import seed
    from random import randint
# seed random number generator
    seed(1)
# generate some integers
    value = randint(1, 100)
    for i in range(value):
        getal= int(input("Geef een getal op: "))
        print(value)
        if getal == value:
            print('het is goed')
        elif getal >= value:
            print('het getal is kleiner')
        else:
            print('het getal is groter')
getal()
def rps():
    from random import seed
    from random import randint
# seed random number generator
    seed(1)
# generate some integers
    value = randint(1, 3)
    keuze= int(input('geef een getal tussen 1-3 op:'))
    for i in range(value)
    print(value)
    if keuze == value:
        print(
            

