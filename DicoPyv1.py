#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:59:55 2020

@author: teddy


EN = Here you This is import libraries using expression : import 
EN = import json using a libraries json why give a possibility at create and read a json file 
EN = import os using a libraries os give  possibility at acces of systeme occurency and gestion of file 
EN = import MotObject this is Simple import Object class 


FR = Ici, vous importez des bibliothèques en utilisant l'expression: import
FR = importer json utiliser une bibliothèque json pourquoi donner la possibilité de créer et lire un fichier json
FR = importer un os en utilisant une bibliothèque os donner la possibilité d'accéder à l'occurrence du système et à la gestion du fichier
FR = importer MotObject c'est un simple import de l'objet 

"""
import json
import os
import os.path
from time import sleep
from tkinter import *
import speech_recognition as sr  

nameRegist = "Book.json"

"""
EN = this function transforms at file Type json
FR = cette fonction transforme en fichier de type json
"""
def createFormatJsonType(filechecked,textError):
    
    file = open(filechecked, 'w')
    data = {}
    file.write("{}")
    file.close()
    print(textError)
    
"""
EN = this function create file .json
FR = cette fonction cree un ficher en .json
"""
def createFile(nameFile):
    
    print("your file haven't find but this programme have create a new file for you")
    fileCreate = open(nameFile,'a')
    fileCreate.close()
    
    
"""
EN = this function check size of file,and if he are at json file 
FR = cette fonction verifie la taille du fichier , et si il est un fichier json 
"""
def checkJsonType(filechecked):
    
     
    """
    EN = condition check size file 
    FR = verifie la taille du fichier 
    """
    if(os.path.getsize(filechecked) == 0):
            
        Error = "this file was empty but this program write a good expresion"
        createFormatJsonType(filechecked,Error)
            
    else:
        """
        EN = this try check file inside at expresion and if isn't format json he started action creatFormatType ,and checkJsonType for test good proccess
        FR = le try verifie l'expression à l'interieur du fichier et si il n'est pas au format json il demarre l'action creatFormatType ,and checkJsonType pour test le bon processus '
        """
        try:
            file = open(filechecked,'r')
            data = json.load(file)
            if isinstance(data,dict) == False:
                createFormatJsonType(filechecked, "Error inside text change")
            file.close()
            print("json File detected and is good")
        except json.JSONDecodeError as e:
            print("your file isn't a json file ")
            value = filechecked
            Error2 = "this file having not good expression writed at format json he has rewriting"
            createFormatJsonType(value,Error2)
            checkJsonType(value)
                
"""
EN = Check if dataValue existed 

FR = teste si le fichier DicoPyBook.json exist et retourne vrai ou faux 

"""
def checkExistence(dataValue):
    """
    EN = Check if dataValue existed if isn't exist this program go to the else condition 
    FR = Vérifiez si dataValue existait s'il n'existe pas ce programme passe à la condition else
    """
    if(os.path.isfile(dataValue)):
        print("File existed ")
        checkJsonType(dataValue)
    else:
        """
        EN = informe a user than his file's isn't not create then create file for them 
             once this action termined this program restart this fonction 
        FR = informer un utilisateur que son fichier n'est pas créé, puis créer un fichier pour lui
             une fois cette action terminée ce programme redémarrer cette fonction
        """
        fileCreatevariable = dataValue
        
        createFile(fileCreatevariable)
        
        checkExistence(fileCreatevariable)
        
def buttonSubmitAZ(nameRegist):
    
    file = open(nameRegist,'r')
        
    data = json.load(file)
        
    for k in sorted(data.keys()):
        box.insert(END, "%s-" % (k))
        
def buttonSub(nameRegist):
    
    file = open(nameRegist,'r')
    data = json.load(file)
    try:
        value = capture.get()
        if data[value]:
           
            box.insert(END,"\nThe word is : %s"%(value))
            i = 0
            for k in data[value]:
                box.insert(END,"\nDefinition number %s : %s"%(i,data[value][k]))
                i += 1
    except KeyError:
        box.insert(END,"\nThe word is not exist")
    file.close()

def clearBox():
    box.delete('0.0', END)
    
def addWord(nameRegist):
    box.insert(END,"\nYou would like add a word please follow instructions. \nWrite in yellow box your word and red box write number definition. \nIf you have finish press add")
    capture.config(bg="yellow")
    button.config(text="Add Word Submit",command=lambda:pressAdd(nameRegist))
    
def AddDefFinish():
    button.config(text="Submit",command= lambda:buttonSub(nameRegist))
    capture.delete(0,END)
    capture.config(bg='white')
    button1.config(text = 'Add Word',command=lambda:addWord(nameRegist))
    
def pressAdd(nameRegist):
    
    take = capture.get()
    takenumber = capture1.get()
    
    box.insert(END,"\nFirst write word : %s "%(take))
    
    file = open(nameRegist,'r')
                
    data = json.load(file)
                
    data[take] = {}
                
    data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
                
    file.close()
        
    file = open(nameRegist,'w')
        
    file.write(data)
        
    file.close()
                    
    box.insert(END,"\nPlease write definition in green box and press add definition.\n If you have finish press finish Add")
        
    button.config(text="ADD Definition",command=lambda:AddDef(nameRegist,take))
    
    button1.config(text="Finish Add",command=AddDefFinish)
    
    
def AddDef(nameRegist,take):
    
    file = open(nameRegist,'r')
                
    data = json.load(file)
    
    i = 0
    for l in data[take]:
        if data[take][l]:
            i += 1
    
    aDefinition=capture2.get()
    
    data[take]["%s" % (i)]= aDefinition
        
    data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        
    file.close()
    
    file = open(nameRegist,'w')
    
    file.write(data)
    
    file.close()

    print("your word create with succes")
                
    box.inster(END,"your word create with succes")

def recognition(nameRegist):
    
        r  = sr.Recognizer()
        
        with sr.Microphone() as source:
        
            audio = r.listen(source)
            try:
                kiker = True
                while kiker:
                    text = r.recognize_google(audio)
                    print("test ",text)
                    box.insert(END,"you say : %s"%(text))
                    text1 = "sumbit"
                    text3 = "a to z"
                    text4 = "clear"
                    text8 = "leave"
                    finality=text.lower()
                    
                    if finality == text8:
                        kiker=False
                    elif finality == text1:
                        buttonSub(nameRegist)
                    elif finality == text4:
                        clearBox()
                        
            except sr.UnknownValueError:
                print("this sound hasn't understand")
            except sr.RequestError as e:
                print("Le service Google Speech API ne fonctionne plus" + format(e))
                
def startrecognition(nameRegist):
    #box.insert(END,"Please this is expression use : \nSubmit ,\nAdd Word ,\nfrom a to z,\nClear")
    sleep(5)
    recognition(nameRegist)
    
dico = Tk()
dico.geometry("700x700")
dico.title("DicoPyBook")
checkExistence(nameRegist)
champLabel = Label(dico,text="WELCOME TO DICOPYBOOK").pack()
box=Text(dico,height=10, width=100)
box.pack()
text = "\nWelcome to DicoPy select your option please : "

champ_label1 = Label(dico,  text=text).pack()

text1 = "\nHere you have a Submit text \nIf you write text ,press Submit and a word is a data base \nThat definition appears above : "

champ_label2 = Label(dico,  text=text1).pack()

capture = Entry(dico, width=10)
capture.pack()

capture1 = Spinbox(dico, from_=0, to=10)
capture1.pack()

button = Button(dico,text = 'Submit',command= lambda:buttonSub(nameRegist))
button.pack() 

button1 = Button(dico,text = 'Add Word',command=lambda:addWord(nameRegist))
button1.pack()

button2 = Button(dico,text = 'Print a dictionary from A to Z',command= lambda: buttonSubmitAZ(nameRegist))
button2.pack()

button3 = Button(dico,text = 'voice recognition',command=lambda:startrecognition(nameRegist))
button3.pack()

button4 = Button(dico,text = 'clear box text',command=clearBox)
button4.pack()

capture2=Entry(dico,text="def", width=70,bg='green')
capture2.pack()
#saisie = tkinter.Entry ()
dico.mainloop()
#file.close()          
