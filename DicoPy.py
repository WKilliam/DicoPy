#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:50:04 2020

@author: teddy
"""
import json
import os
import speech_recognition as sr  

'''
r  = sr.Recognizer()
with sr.Microphone() as source:
    print("Dites quelque chose")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio, language="fr-FR")
    text1 = text.lower()
    toto = 'commande'
    if(text1 == toto):
        print('good')
    print("Vous avez dit : " + text)
except sr.UnknownValueError:
    print("L'audio n'as pas été compris")
except sr.RequestError as e:
    print("Le service Google Speech API ne fonctionne plus" + format(e))
'''
    


from tkinter import *
from DicoPyv1 import *

def buttonSubmitAZ():
    
    contenu = searchbox.get ()
    
    os.system('clear')
    
    sleep(0.5)
    
    file = open(nameRegist,'r')
        
    data = json.load(file)
        
    for k in sorted(data.keys()):
        searchbox.insert(tkinter.END, "\n%s" % (k))
        
nameRegist = "Book.json"

#checkExistence(nameRegist)


dico = Tk()
dico.geometry("700x700")
dico.title("DicoPyBook")
champ_label = Label(dico,  text="WELCOME TO DICOPY").pack()
searchbox = Text(dico,height=10, width=100)

searchbox.pack()

text = "\nWelcome to DicoPy select your option please : "

champ_label1 = Label(dico,  text=text).pack()

text1 = "\nHere you have a Submit text \nIf you write text ,press Submit and a word is a data base \nThat definition appears above : "

champ_label2 = Label(dico,  text=text1).pack()

capture = Entry(dico, width=10)
capture.pack()

button = Button(dico,text = 'Submit',command = buttonSubmit)
button.pack() 

button1 = Button(dico,text = 'Add Word',command = buttonSubmit)
button1.pack()

button2 = Button(dico,text = 'Print a dictionary from A to Z',command = buttonSubmitAZ)
button2.pack()

button3 = Button(dico,text = 'voice recognition',command = buttonSubmit)
button3.pack()

#saisie = tkinter.Entry ()
dico.mainloop()

"""

def comd():
    #contenu = saisie.get ()
    #print(contenu)
    #saisie.delete(0,tkinter.END)
    searchbox.insert(tkinter.END, "kqgldgldjghkqjkqjg")
    #searchbox.configure(state='disabled')
    #searchbox.delete(0,tkinter.END)
"""



