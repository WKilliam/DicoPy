from bs4 import BeautifulSoup
import urllib.request

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
import urllib.request

with urllib.request.urlopen('https://www.linternaute.fr/dictionnaire/fr/definition/a-bas/') as response:
   html = response.read()
   


file = open("Html.txt",'a')
file.close()
file = open("Html.txt",'w')
file.write(str(html))
file.close()
file = open("Html.txt",'r')

tab = []
for k in file:
    tab.append(k)

tabhtml = list(tab[0])
#print(tabhtml)


fin = 0


for k in range(len(tabhtml)):
    
    #let = tabhtml.pop(0).lower()
    tabtestingletter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','<','>']
    
    if tabhtml[k] in tabtestingletter:
        fichier=open("htmlPurgeLv1.txt","a") # N'AFFICHE PAS LA LETTRE SUR LE RESULTAT SI c'est vrai 
        fichier.write(tabhtml[k])
        fichier.close()
    else:
        pass



textpurge =  tabhtml


tableaupropre = []


for key in range(len(textpurge)):
    
    if (textpurge[key]=='<' 
        and textpurge[key+1]  == 's'
        and textpurge[key+2]  == 'p'
        and textpurge[key+3]  == 'a'
        and textpurge[key+4]  == 'n'
        and textpurge[key+5]  == ' '
        and textpurge[key+6]  == 'c'
        and textpurge[key+7]  == 'l'
        and textpurge[key+8]  == 'a'
        and textpurge[key+9]  == 's'
        and textpurge[key+10] == 's'
        and textpurge[key+11] == '='
        and textpurge[key+12] == '"'
        and textpurge[key+13] == 'd'
        and textpurge[key+14] == 'i'
        and textpurge[key+15] == 'c'
        and textpurge[key+16] == 'o'
        and textpurge[key+17] == '_'
        and textpurge[key+18] == 't'
        and textpurge[key+19] == 'i'
        and textpurge[key+20] == 't'
        and textpurge[key+21] == 'l'
        and textpurge[key+22] == 'e'
        and textpurge[key+23] == '_'
        and textpurge[key+24] == '2'
        and textpurge[key+25] == '"'
        and textpurge[key+26] == '>'):
        print("yes")
        
        keys = key
        
        for keys in range(len(textpurge)):
            
            tableaupropre.append(textpurge[keys])
            
            if(textpurge[keys]        =='<'
               and textpurge[keys+1]  =='/' 
               and textpurge[keys+2]  =='a' 
               and textpurge[keys+3]  =='>' 
               and textpurge[keys+4]  =='.' 
               and textpurge[keys+5]  =='<' 
               and textpurge[keys+6]  =='/' 
               and textpurge[keys+7]  =='d' 
               and textpurge[keys+8]  =='i'
               and textpurge[keys+9]  =='v'
               and textpurge[keys+10] =='>'):
                break
            
newtab = ''

for i in range(len(tableaupropre)):
    
    newtab = newtab + tableaupropre[i]
    
    

for k in range(newtab.count('>\n')):
    newtab.replace('>\n', '=', k)
    print(k)

    


'<span class="dico_title_2">'


file.close()



filea = open("test.txt","a")

filea.write(str(newtab))

filea.close()

filea = open("test.txt","r")

ligne= filea.readlines()


filea.close()

ligne[0]= ligne[0].replace(' ', '')
ligne[0]= ligne[0].replace('\n', '')
ligne[0]= ligne[0].replace("[", '')
ligne[0]= ligne[0].replace("ahref=", '')
ligne[0]= ligne[0].replace("/dictionnaire/fr/definition/",'')
ligne[0]= ligne[0].replace("@",'')

ligne[0]= ligne[0].replace("/",'')
ligne[0]= ligne[0].replace("//",'')
ligne[0]= ligne[0].replace("///",'')
ligne[0]= ligne[0].replace("////",'')
ligne[0]= ligne[0].replace("_",'')
ligne[0]= ligne[0].replace("=",'')
ligne[0]= ligne[0].replace("'",'')
ligne[0]= ligne[0].replace("&",'')
ligne[0]= ligne[0].replace("#",'')
ligne[0]= ligne[0].replace("||",'')
ligne[0]= ligne[0].replace(";",'')
ligne[0]= ligne[0].replace("$",'')
ligne[0]= ligne[0].replace("%",'')
ligne[0]= ligne[0].replace("+",'')
ligne[0]= ligne[0].replace("*",'')
ligne[0]= ligne[0].replace("!",'')

ligne[0]= ligne[0].replace("?",'')

ligne[0]= ligne[0].replace(".",'')

ligne[0]= ligne[0].replace(",",'')

ligne[0]= ligne[0].replace("}",'')
ligne[0]= ligne[0].replace("{",'')
ligne[0]= ligne[0].replace("]",'')
ligne[0]= ligne[0].replace("[",'')

ligne[0]= ligne[0].replace("(",'')
ligne[0]= ligne[0].replace(")",'')
ligne[0]= ligne[0].replace("0",'')
ligne[0]= ligne[0].replace("1",'')
ligne[0]= ligne[0].replace("2",'')
ligne[0]= ligne[0].replace("3",'')
ligne[0]= ligne[0].replace("4",'')
ligne[0]= ligne[0].replace("5",'')
ligne[0]= ligne[0].replace("6",'')
ligne[0]= ligne[0].replace("7",'')
ligne[0]= ligne[0].replace("8",'')
ligne[0]= ligne[0].replace("9",'')
ligne[0]= ligne[0].replace("-",'')

ligne[0]= ligne[0].replace('"','')
b='\\'
ligne[0]= ligne[0].replace(":",'')
ligne[0]= ligne[0].replace(b,'')

#ligne[0]= ligne[0].replace('div class="grid_line gutter grid--norwd"','')


    
filea = open("test.txt","w")

filea.write(str(ligne))

filea.close()

good = list(ligne[0])

#print(good)

hide =[]
lol =""
n = 0

for h in range(len(good)):
    
    if good[h] == '>':
        lol = lol + good[h]
        hide.append(lol)
        lol =""
        n = 0
    elif good[h] == '<' or n == 1:
        lol = lol + good[h]
        n = 1

#print(hide)   

delm=''

for p in range(len(hide)):
    delm=delm+hide[p]

fileA = open("test2.txt","a")

fileA.write(str(delm))

fileA.close()

fileA = open("test2.txt","r")

ligneA= fileA.readlines()


fileA.close()

ligneA[0]= ligneA[0].replace('<a>', '')
ligneA[0]= ligneA[0].replace('<li>', '')
ligneA[0]= ligneA[0].replace('<div>', '')
ligneA[0]= ligneA[0].replace('<script>', '')
ligneA[0]= ligneA[0].replace('<em>', '')
ligneA[0]= ligneA[0].replace('<ul>', '')
ligneA[0]= ligneA[0].replace('<button>', '')
ligneA[0]= ligneA[0].replace('<divclassccmcssoffcanvas>', '')
ligneA[0]= ligneA[0].replace('<ulclassdicoliste>', '')

ligneA[0]= ligneA[0].replace('<divclassgridleft>', '')
ligneA[0]= ligneA[0].replace('<spanclassdicotitle>', '')
ligneA[0]= ligneA[0].replace('<divclassgridlineguttergridnorwd>', '')
ligneA[0]= ligneA[0].replace('<ulclassdicoliste>', '')

ligneA[0]= ligneA[0].replace('<ifltIE>', '')
ligneA[0]= ligneA[0].replace('<divclassgridlast>', '')
ligneA[0]= ligneA[0].replace('<etreturngetrtoRGBivisiblefunctionereturne>', '')

ligneA[0]= ligneA[0].replace('<httpswwwlinternautecomlifestylelist>', '')
ligneA[0]= ligneA[0].replace('<nav>', '')
ligneA[0]= ligneA[0].replace('<span>', '')
ligneA[0]= ligneA[0].replace('<h>', '')
ligneA[0]= ligneA[0].replace('<divclassgridlast>', '')

ligneA[0]= ligneA[0].replace('<liclassfillin>', '')

ligneA[0]= ligneA[0].replace('<legend>', '')

ligneA[0]= ligneA[0].replace('<buttontypesubmit>', '')

ligneA[0]= ligneA[0].replace('<section>', '')
ligneA[0]= ligneA[0].replace('<from>', '')
ligneA[0]= ligneA[0].replace('<svg>', '')
ligneA[0]= ligneA[0].replace('<g>', '')
ligneA[0]= ligneA[0].replace('<head>', '')

ligneA[0]= ligneA[0].replace('<p>', '')

ligneA[0]= ligneA[0].replace('<dividctnnativeatf>', '')

ligneA[0]= ligneA[0].replace('<liclassjEventjEvenementdatakeyjContentEvenements>', '')

fileA = open("test2.txt","w")

fileA.write(str(ligneA))

fileA.close()

good2 = list(ligneA[0])

#print(good2)

hide2 =[]
lol2 =""
n2 = 0

for h in range(len(good2)):
    
    if good2[h] == '>':
        lol2 = lol2 + good2[h]
        hide2.append(lol2)
        lol2 =""
        n2 = 0
    elif good2[h] == '<' or n2 == 1:
        lol2 = lol2 + good2[h]
        n2 = 1
        
print(hide2)  
#for j in range(len(ligne[0])):
#    print()
    
"""


file2 = open("htmlpurge.txt",'a')

file2.write(str(tableaupropre))

file2.close

file2 = open("htmlpurge.txt",'r')
file2.close
"""