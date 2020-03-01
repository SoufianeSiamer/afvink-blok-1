list_ = []
#openen van het bestand en in een lijst zetten
def openbestand_():
    bestand = open("SC_expression.csv")
    bestand.readline()
    
    for regel in range(6071):
        regel = bestand.readline()
        regel = regel.strip()
        regel = regel.split(",")
        list_.append(regel)



#gemiddelde berekenen van een kolom
def gemiddelde_():
    kolom = int(input ("Welke kolom wil je hebben?"))
    gem = 0
    for getal in range(len(list_)):
        gem += float (list_[getal][kolom])
          
    gem = gem / len(list_)
    print (gem)


#bekijken welke values boven 50 zijn
def hogerdan():
    kolom = int(input ("Welke kolom wil je hebben?"))
    for getal in range(len(list_)):
        waarde = float (list_[getal][kolom])
        if waarde > 50 or waarde == 50:
            print (list_[getal][0])
        


def main():
    openbestand_()
    gemiddelde_()
    hogerdan()
main()
