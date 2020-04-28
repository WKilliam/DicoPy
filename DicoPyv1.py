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

def createFormatJsonType(filechecked,textError):
    
    file = open(filechecked, 'w')
    data = {}
    file.write("{}")
    file.close()
    print(textError)
    

def createFile(nameFile):
    
    print("your file haven't find but this programme have create a new file for you")
    fileCreate = open(nameFile,'a')
    fileCreate.close()
    
    
    
def checkJsonType(filechecked):
     
        if(os.path.getsize(filechecked) == 0):
            
            Error = "this file was empty but this program write a good expresion"
            createFormatJsonType(filechecked)
            
        else:
            try:
                file = open(filechecked,'r')
                data = json.load(file)
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
        
         
checkExistence("Book.json")
         
"""
  try:
                file = open('DicoPyBook.json','r')
                data = json.load(file)
                print("toto")
            except json.JSONDecodeError as e:
                    print("ta fais uune gaffe")
   
                
     else:
        try:
            file = open('DicoPyBook.json','r')
            data = json.load(file)
            print("toto")
        except json.JSONDecodeError as e:
                print("ta fais uune gaffe")
        
else:
    print("not")
    
"""