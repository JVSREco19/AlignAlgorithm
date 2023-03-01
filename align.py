import re
from Bio import Align

homologuesFile = open("homologues.txt")
mutationFile = open("mutationsOneOnly.txt","w")


def remove_repetidos(lista):
    l = []
    for i in lista:
      if i not in l:
        l.append(i)

      l.sort()
      
    return l


def compare_vectors(list1, list2):
    result = []
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            result.append((list1[i], list2[i]))
    
    if result.__len__() == 1:
        print(result)
        print(list1,list2)
        result = result[0]
    else:
        result = None
      
    return result

def compareSequences(mainSeq,senquencesToCompare):
    ligands = re.findall(r'[a-zA-Z]{1,5}',mainSeq)
    compareLigands= []
    mutations = []
    for i in senquencesToCompare:
            aux = re.findall(r'[a-zA-Z]{1,5}', i)
            if (aux.__len__() == ligands.__len__()):
                compareLigands.append(aux)
  
    for i in compareLigands:
        if(i == ligands):
            continue
        else:
            resultOfComparation = compare_vectors(ligands, i)
            if resultOfComparation != None:
                mutations.append(resultOfComparation)
            
    if mutations == [] or mutations== None:
        mutations = None
        print("NoMutations")
       
    return mutations
    

def findEqualBindingSites(bindingSite,vet):
    seqListToCompare = []
    for j in vet:
        for i in j:
            if (i[1] == bindingSite):
                    seq = i[0]
                    seqListToCompare.append(seq)
    return seqListToCompare


def findSeq(template):
    allProtSeq = []
    metalList = ['CD', 'SB', "HG","GD","CO","U","NI","CU","NA",'K','MN','CA','MG','FE','ZN']
    bioLipFile = open("BioLiP_2013-03-6_nr.txt")
    for line in bioLipFile:
        
            
        lineVet = line.split('\t')
        if(lineVet[4] in metalList): #Verifies if it is a metal ligand
            continue
            
        if(lineVet[0]==template):
            
            seqVet = []
            seqVet.append(lineVet[7])
            seqVet.append(lineVet[4])
            seqVet.append(lineVet[0])
            allProtSeq.append(seqVet)
    bioLipFile.close()
    return allProtSeq
            
markTheProgress = 0

for line in homologuesFile:
    markTheProgress += 1
    line = line.split()
    print(str(markTheProgress)+ ' of 620')
    mainProtein = line[0]
    allProtMutations = []
    homologues = line[1:line.__len__()]
    proteinSequences = []
    for i in line:
        proteinSequences.append(findSeq(i))
        
    for i in proteinSequences[0]:
        if(i[i.__len__()-1] == mainProtein):
            mainSequence = i[0]
            bindingSite = i[1]
            senquencesToCompare = findEqualBindingSites(bindingSite,proteinSequences[1:])
            if(senquencesToCompare == [] or senquencesToCompare == None):
                continue
            
            mutations = compareSequences(mainSequence, senquencesToCompare)
            if mutations == None or mutations[0] == []:
                continue
            allProtMutations.extend(mutations)
    if(allProtMutations == None or allProtMutations == []):
        NoMutationFile = open('NoMutatioFile.txt','a')
        NoMutationFile.write(mainProtein + '\n')
        continue
    allProtMutations = remove_repetidos(allProtMutations)
    for stringToWrite in allProtMutations:
        mutationFile.write(
            mainProtein + ' ' + str(stringToWrite[0])+',' + str(stringToWrite[1]) + "\n")

    
mutationFile.close()