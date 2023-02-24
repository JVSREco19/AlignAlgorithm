import blosum as bl
matrix = bl.BLOSUM(62)

mutationsFile = open("mutationsOneOnlyReady.txt")
linesToMantain = []
for mutation in mutationsFile:
  
  line = mutation.split()
  protein = line[0]
  first = line[1][0]
  second = line[1][2]
  
  if(matrix[str(first+second)]>0):
    print(mutation[0:mutation.__len__()-1], matrix[str(first+second)])
    linesToMantain.append(mutation)


mutationsFile.close()

newFile = open("mutationsFinalVersion.txt",'w')

for i in linesToMantain:
  newFile.write(i)

newFile.close()
