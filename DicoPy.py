#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:50:04 2020

@author: teddy
"""
import json
import os
from MotObject import *

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



dico = Tk()
dico.geometry("700x700")
dico.title("DicoPyBook")


champ_label = Label(dico, text="Bienvenu sur DicoPyBook ")

buttonStart = Button(dico, text="FILE", fg="white", bg="red").place(x="350",y="350")
#buttonStart.grid(row=0,column=4)

#btn=tkinter.Button(dico, texte="yo")
#btn.pack()
buttonStart.pack()
champ_label.pack(side=TOP)


dico.mainloop()



