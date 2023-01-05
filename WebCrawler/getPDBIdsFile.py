def remove_repetidos(lista):
    l = []

    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


archive = open("BioLip_X_M-CSA.csv")
listOfIDs=[]
counter = 0
for line in archive:
  if (counter == 0):
    counter = 1
    continue
  line = line.split(',')
  listOfIDs.append(line[0])
archive.close()

listOfIDs = remove_repetidos(listOfIDs)
archive = open("listOfPDBIDs.txt","w")
archive.write(' '.join(listOfIDs))
archive.close()