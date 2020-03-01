max = 5 #max 5x vragen
total = 0#start
for counter in range(max):
    gevangen = int(input('Hoeveel bugs gevangen: ')) #vraagt hoeveel er gevangen zijn
    total = total + gevangen#telt ze op
print(total)

            

ronden = int(input('hoeveel rondes gereden '))#input hoeveel er gereden is
total= 0.0#start
snelste =1000
langzaam=0
for i in range(ronden):
    rondetijd= float(input('geef je rondetijd op: '))#input hoeveel rondjes
    total= total + rondetijd#telt op
    if rondetijd > langzaam:
        langzaam=rondetijd
    if rondetijd < snelste:
        snelste=rondetijd
    
    
gemiddelde= total/ronden#berekend de gemiddelde
 
print('de totale tijd is'+(total))
print('de gemiddelde rondetijd:'+(gemiddelde))
print('de snelste ronde is: +'(snelste))
print('de tijd van de traagste ronde is: '+(langzaam))


num = int(input("enter a number: "))#vraagt input
fac = 1
for i in range(1, num + 1):
    fac = fac * i
print("macht van ", num, " is ", fac)
