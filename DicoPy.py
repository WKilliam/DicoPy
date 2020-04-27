#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:50:04 2020

@author: teddy
"""
import json
import os
from MotObject import *

itxt = input()

otxt = list(itxt)

print(otxt)


file = open('DicoPyBook.json','r')

data = json.load(file)

data["toto"] = otxt

data = json.dumps(data)

print(data)

file.close()

file = open('DicoPyBook.json','w')

file.write(data)

file.close()


