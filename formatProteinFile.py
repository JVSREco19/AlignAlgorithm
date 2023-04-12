homologuesFile = open("homologues.txt")
biolipNoMetalFile = open("NoMetalBioLiP.txt")

biolipList = biolipNoMetalFile.readlines()
biolipNoMetalFile.close()
finalList = []
for line in homologuesFile:
  line = line.split()
  
  proteinLIT = line[0]
  for i in biolipList:
    splittedLine = i.split("\t")
    name = splittedLine[0]
    if(name != proteinLIT):
      continue
    ligand = splittedLine[4]
    residues = splittedLine[7]
    num = splittedLine[11]
    if(num == ''):
      num  = "NA"
    tempList = []
    tempList.append(name)
    tempList.append(num)
    tempList.append(ligand)
    tempList.append(residues)
    finalList.append(tempList)

homologuesFile.close()

newFormatedProtFile = open("proteinsFormated.txt","w")
for i in finalList:
  newFormatedProtFile.write(i[0] + ' ' + i[1] + ' '+i[2] + ' '+i[3]+ '\n')
  
newFormatedProtFile.close()

  
  

