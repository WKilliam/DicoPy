import json
import os


a=1
b=2
c = a+b




file = open('DicoPyBook.json')

data = json.load(file)

lol = data["toto"]

print(lol)

#print(data)


##file.close()

