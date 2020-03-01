# Naam:Soufiane Si Amer
# Datum: 28-10-2019 
# Versie:1.0


DdeI   = "CTGAG"    #knipt op C^TGAG      Desulfovibrio desulfuricans    	
BspMII = "TCCGGA"   #knipt op T^CCGGA     Klebsiella pneumoniae 
EcoRI  = "GAATTC"   #knipt op G^AATTC     Escherichia coli
HindIII= "AAGCTT"   #knipt op A^AGCTT     Haemophilus influenzae
TaqI   = 'TCGA'     #knipt op T^CGA    	  Thermus aquaticus
    
def lees_inhoud():#Deze functie opent het fastabestand, leest het door verwijderd de wittekens
    bestand = "lamaseq.fasta"
    lijst = open(bestand)
    line= lijst.readline()
    header = ""
    seq = ""
    while line:
        line = line.replace("\t", "")
        line= line.replace('\n','')#verwijder alle enters
        if '>' in line:#zoekt naar deze teken, Stopt deze in de header regel
            header= line
        else:#de rest is de sequentie
            seq= seq+ line
        line= lijst.readline()
    return seq

#deze functie controleert of het DNA is 
def is_dna():
    seq= lees_inhoud()#haalt de sequentie op
    total_length= len(seq)#telt de volledige lengte
    ATCGtel= seq.count('A')+seq.count('T')+seq.count('C')+seq.count('G')#telt alle ATCG op
    if total_length == ATCGtel: #als de lengte even groot is
        print("dit is DNA")#print
    else:#anders print dit
        print("dit is geen DNA")
#deze functie controleert of er enzymen kunnen knippen in dit stuk DNA
def knipt():
    seq = lees_inhoud()
    if DdeI in seq: #leest de seq van het enzyme uit en bepaalt of het in het dna zit
        print('DdeI knipt wel')#als het erin zit print hij dit uit
    else: # anders print hij het onderstaande uit
        print('DdeI knipt niet')
    if BspMII in seq:#leest de seq van het enzyme uit en bepaalt of het in het dna zit
        print('BspMII knipt wel')#als het erin zit print hij dit uit
    else:# anders print hij het onderstaande uit
        print('BspMII knipt niet')
    if EcoRI in seq:#leest de seq van het enzyme uit en bepaalt of het in het dna zit
        print('EcoRI knipt wel')#als het erin zit print hij dit uit
    else:# anders print hij het onderstaande uit
        print('EcoRI knipt niet')
    if HindIII in seq:#leest de seq van het enzyme uit en bepaalt of het in het dna zit
        print('HindIII knipt wel')#als het erin zit print hij dit uit
    else:# anders print hij het onderstaande uit
        print('HindIII knipt niet')
    if TaqI in seq:#leest de seq van het enzyme uit en bepaalt of het in het dna zit
        print('TaqI knipt  wel')#als het erin zit print hij dit uit
    else:# anders print hij het onderstaande uit
        print('TaqI knipt niet')
#roept alle functies aan
def main():
    bestand = "lamaseq.fasta" 
    sequentie = lees_inhoud()
    dna= is_dna()
    enzymen= knipt()


    
main()
