import customtkinter as ct
import pyperclip
from CTkMessagebox import CTkMessagebox

liste=[]
mot=("")

fenetre = ct.CTk()
fenetre.title("Liste Creator")

texte=()

entree=ct.CTkTextbox(fenetre)

def construire():
    global non_liste
    global yes_no
    global liste
    global mot
    non_liste=entree.get(0.0,"end")
    non_liste+=("\n")
    for i in range(len(non_liste)):
        if non_liste[i]!="\n":
            mot+=non_liste[i]
        else:
            liste.append(mot)
            mot=("")
    texte=("["+'"'+'","'.join(liste)+"]")
    if len(texte)>50:
        affiche=texte[0:15]+("     (...)     ")+texte[-16:-1]
    else:
        affiche=texte
    yes_no=CTkMessagebox(title="Copy ?",message=affiche,icon="question", option_1="Copy",option_2="Non Tanks")
    reponse=yes_no.get()
    if reponse=="Copy":
        pyperclip.copy(texte)
        pyperclip.paste()
    else:
        texte=()

def ecrire():
    Input.destroy()
    global OK
    global non_liste
    OK=ct.CTkButton(fenetre,text="OK")
    OK.pack()
    OK.bind("<Button-1>",lambda event:construire())
    entree.pack()

Input=ct.CTkButton(fenetre,text="Liste Creator")
Input.pack()
Input.bind("<Button-1>",lambda event:ecrire())

fenetre.mainloop()

