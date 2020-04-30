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
            
newtab =[]

for i in range(len(tableaupropre)):
    
    tableaupropre[i].lstrip(' ')
    
    test = True
    
    if tableaupropre[i] == '<':
        test= False
        print("false")
    elif tableaupropre[i] == '>':
        test = True
        print("true")
    elif test == True:
        newtab.append(tableaupropre[i])


print(newtab)
    
print("succes !!!")  

"""
'<span class="dico_title_2">'

file.close()

file2 = open('text.txt','a')


file2.write(str(tableaupropre))

file2.close()



file2 = open("htmlpurge.txt",'a')

file2.write(str(tableaupropre))

file2.close

file2 = open("htmlpurge.txt",'r')






file2.close

"""





