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
    

itxt = input()

otxt = list(itxt)

#print(otxt)


file = open('DicoPyBook.json','r')

data = json.load(file)






k = "jsonIndex_"

l = "cleDefinition"

#data = {}

print(len(data))


#data["%s_%s" % (k, itxt)]={"\n %s_%s" % (l, itxt):"nul"}

#data["%s_%s" % (k, itxt)]["%s_%s" % (l, itxt)] = itxt


print(data)

#data["%s_%s" % (k, itxt)] = ["clé_E"] otxt

print ()




data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

#print(data)

file.close()

file = open('DicoPyBook.json','w')

file.write(data)

file.close()


