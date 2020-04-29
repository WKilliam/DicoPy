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
from MotObject import *
from time import sleep

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
        
        
nameRegist = "Book.json"

checkExistence(nameRegist)


file = open(nameRegist,'r')

data = json.load(file)

print(type(data),"1")

toto = True

while toto:
    
    print("\nhi your dictionary owns : ",len(data),"word" ,
      "\nplease select your command number :",
      "\n[1]you would like  add a word ?",
      "\n[2]you would like  search a word ?",
      "\n[3]you would like  search a difinition ?",
      "\n[4]you would like  print a dictionary from A to Z ?")
    
    itxt = input()
    
    swht = {1,2,3,4}
    goodBad = False
    
    for s in swht:
        try:
            if int(itxt) == s:
                goodBad = True
                break
        except:
            break
    if goodBad:
        toto = False
        break
    else:
        print("your choise is not good ")
    
if itxt == "1":
    acces = True
    while acces:
            print("you would like add a word please follow instructions")
            os.system('clear')
            sleep(0.5)
            print("First write word :")
            word = input()
            os.system('clear')
            sleep(0.5)
            checker = True
            while checker:
                try:
                    print("seconde write number definition of word => ",word ," : ")
                    numberdef = int(input())
                    break
                except:
                    print("please select number")
                    os.system('clear')
                    sleep(0.5)
                    
            
            key1 = "keyDef"
            
            file = open(nameRegist,'r')
            
            data = json.load(file)
            
            data[word] = {}
            
            data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
            
            file.close()
    
            file = open(nameRegist,'w')
    
            file.write(data)
    
            file.close()
            
            for defin in range(int(numberdef)):
                    
                    file = open(nameRegist,'r')
    
                    data = json.load(file)
                    
                    print("please write definition number ",defin ,word,"%s_%s" % (key1, defin))
                    
                    aDefinition = input()
                     
                    
                    data[word]["%s_%s" % (key1,defin)]= aDefinition
                    
                    data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
                    
                    file.close()
    
                    file = open(nameRegist,'w')
    
                    file.write(data)
    
                    file.close()
            
            result=input()
            if result != "y":
                acces = False
            
elif itxt == "2":
    print("tu es au 2")
elif itxt == "3":
    print("valeur 3")
elif itxt == "4":
    print("vague 4")
    
file.close()