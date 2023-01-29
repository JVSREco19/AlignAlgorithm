import requests
import bs4
import lxml.etree as xml
import re

homologuesFile = open("homologues.txt", "w")

listOfIdsBIO = open("listOfPDBIDsBIOLIP.txt")
idsList = []
idsListBIO = []
for line in listOfIdsBIO:
    idsListBIO = line.split()

listOfIdsBIO.close()

def remove_repetidos(lista):
    l = []
    
    for i in lista:
        if i not in l:
            if i in idsListBIO:
                l.append(i)
    l.sort()
    return l


for counter in range(1,1006):
    if(counter == 203):
        continue
    URL = "https://www.ebi.ac.uk/thornton-srv/m-csa/entry/"+str(counter) +"/pdb_homologues/"

    page = requests.get(URL)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    Lit = soup.find_all('h3')
    if (Lit.__len__() == 0):
        continue
    Lit = str.split(Lit[0].get_text())

    LIT = Lit[4]
    print(LIT)
    if(idsListBIO.count(LIT)==0):
        print("Not in the list")
        continue
    
    LitR = soup.find_all('tbody')[0].get_text()
    vetLitR = LitR.split()
    if (vetLitR.__len__() == 0):
        continue
    
    templateMatch = re.findall(
    r'\b[a-zA-Z][a-zA-Z0-9]{3}\b|\b[a-zA-Z0-9][a-zA-Z][a-zA-Z0-9]{2}\b|\b[a-zA-Z0-9]{2}[a-zA-Z][a-zA-Z0-9]\b|\b[a-zA-Z0-9]{3}[a-zA-Z]\b', LitR)
    
    if (templateMatch.__len__() == 0):
        continue
    
    templateMatch.sort()
    
    
    homologues = remove_repetidos(templateMatch)
    homologues.remove(LIT)
    
    
    homologuesFile.write(LIT + " ")
    homologuesFile.write(' '.join(homologues) + "\n")
    
    
    counter+=1

homologuesFile.close()