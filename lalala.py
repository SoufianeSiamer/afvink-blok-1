from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)

bestand1 = open(root.filename).readlines()[1:]
bestand1 = "".join(bestand1).replace("\n","")

from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)

bestand2 = open(root.filename).readlines()[2:]
bestand2 = "".join(bestand2).replace("\n","")
af=0
totaal=0
seq1= bestand1
seq2= bestand2
if len(seq1) >len(seq2):
    for a in range(len(seq2)):
        if seq1[a] != seq2[a]:
            totaal+=1
    lengte = len(seq1)-len(seq2)
    af=totaal+lengte
    perc = int((af/len(seq1))*100)
else:
    for a in range(len(seq1)):
        if seq1[a] != seq2[a]:
            totaal +=1
    lengte= len(seq2)-len(seq1)
    af=totaal+lengte
    perc= float((af/len(seq2))*100)
print (str(perc)+ "% fouut ")
print (100-(perc))
