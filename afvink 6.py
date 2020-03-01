

seq = "ACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCC"
#Opent de enzymen bestand, verwijderd het dakje.
def enzymen():
    knipenzymen = {}
    bestand = open ("enzymen.txt")
    for regel in bestand:
        enzym_name, seq = regel.split()
        seqenzym = seq.replace("^","")
        knipenzymen[enzym_name] = seqenzym
    return knipenzymen
    
# zoekt waar het enzym kan knippen
def zoek(seq, eiwit, enzym):
    o = ""
    index = 0
    plaats = []
    while index < len(seq):
        index = seq.find(eiwit, index)
        if index == -1:
              break
        o = o+" " * (index - len(o)) + str(eiwit)
        ff = index
        plaats.append(index)
        index += len(eiwit)
        
    return o,plaats



def match():
#matcht het enzym op de goeie plek
    knipenzymen = enzymen()
    result = {}
    for enzym in knipenzymen:
        if seq.find(knipenzymen[enzym]) != -1:
            o,plaats = zoek(seq, knipenzymen[enzym], enzym)
            print ("er is een match gevonden met " + str (enzym) + " op positie(s)" + str (plaats))
            print (seq)
            print(o)
            
match()
