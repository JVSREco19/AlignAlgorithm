def remove_repetidos(lista):
    l = []

    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


archive = open("BioLiP_2013-03-6_nr.txt")
listOfIDs=[]
counter = 0
for line in archive:
  line = line.split()
  listOfIDs.append(line[0])
archive.close()
listOfIDs = remove_repetidos(listOfIDs)
archive = open("listOfPDBIDsBIOLIP.txt","w")
archive.write(' '.join(listOfIDs))
archive.close()