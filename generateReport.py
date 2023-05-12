bioLipFile = open("BioLIPNonRedundanct.txt")

vetLines = bioLipFile.readlines()

bioLipFile.close()

metalList = ['CD', 'SB', "HG", "GD", "CO", "U", "NI",
             "CU", "NA", 'K', 'MN', 'CA', 'MG', 'FE', 'ZN']

bioLipFile = open("BioLIPNonRedundanct.txt")

vetProteins = []
vetLigands = []
vetRepeatedLigands = []


def remove_repetidos(lista):
    l = []
    for i in lista:
      if i not in l:
        l.append(i)

      l.sort()

    return l

reportFile = open("ReportOfBioLip.txt",'w')
filteredBioLipFile = open("NoMetalBioLiP.txt", 'w')

for line in bioLipFile:
  splitLine = line.split('\t')
  
  if(splitLine[4] in metalList):
    vetLines.remove(line)
    continue
  
  filteredBioLipFile.write(line)
  
  if splitLine[0] not in vetProteins:
    vetProteins.append(splitLine[0])
    
      
  if splitLine[4] not in vetLigands:
    vetLigands.append(splitLine[4])
    
  ligandResidueTuple = (splitLine[4],len(splitLine[7].split()))
  vetRepeatedLigands.append(ligandResidueTuple)

reportFile.write("Report on the BioLiP file\n\n")
reportFile.write("Number of proteins without metal ligands: " + str(len(vetProteins))+'\n')

numOfLigandsOfSameSize = []
vetRepeatedLigands.sort()

vetLigandResidues = remove_repetidos(vetRepeatedLigands)

reportFile.write("Ligand"+ ";" + "Size" + ";" + "Num of occurrences"+'\n')
for i in vetLigandResidues:
  repeatedNum  = vetRepeatedLigands.count(i)
  reportFile.write('"'+str(i[0])+'"' + ";" + str(i[1]) + ";" + str(repeatedNum)+'\n')
 
  for x in range(0,repeatedNum):
    vetRepeatedLigands.remove(i)

  


bioLipFile.close()

