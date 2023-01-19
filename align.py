import re
homologuesFile = open("homologues.txt")


def compare_vectors(vector1, vector2):
    result = []
    for i in range(len(vector1)):
        if vector1[i] != vector2[i]:
            result.append((vector1[i], vector2[i]))
    return result

def compareSequences(mainSeq,senquencesToCompare):
    ligands = re.findall(r'[a-zA-Z]{1,5}',mainSeq)
    compareLigands= []
    mutations = []
    for i in senquencesToCompare:
        for j in i:
            aux = re.findall(r'[a-zA-Z]{1,5}', j)
            if (aux.__len__() == ligands.__len__()):
                compareLigands.append(aux)
    

    
    for i in compareLigands:
        if(i == ligands):
            continue
        else:
            mutations.append(compare_vectors(ligands, i))
            
    
    
    return mutations
    

def findEqualBindingSites(bindingSite,vet):
    seqListToCompare = []
    for j in vet:
        for i in j:
            if (i[i.__len__()-2] == bindingSite):
                    seq = i[:i.__len__()-2]
                    seqListToCompare.append(seq)
    return seqListToCompare


def findSeq(template):
    allProtSeq = []
    bioLipFile = open("BioLiP_2013-03-6_nr.txt")
    for line in bioLipFile:
        lineVet = line.split('\t')
       
            
        if(lineVet[0]==template):
            seqVet = lineVet[7:lineVet.__len__()-9]
            
            stopCondition = False
            while (stopCondition == False):
                try:
                    seqVet.remove('')

                except ValueError:
                    stopCondition = True
                
            for i in range(seqVet.__len__()-1,-1, -2):
                seqVet.pop(i)
            
            seqVet.append(lineVet[4])
            seqVet.append(lineVet[0])
            
            allProtSeq.append(seqVet)
    return allProtSeq
            

for line in homologuesFile:
    line = line.split()
    mainProtein = line[0]
    homologues = line[1:line.__len__()]
    proteinSequences = []
    for i in line:
        proteinSequences.insert(line.index(i), findSeq(i))
    
    for i in proteinSequences[0]:
        if(i[i.__len__()-1] == mainProtein):
            mainSequence = i[:i.__len__()-2]
            
            bindingSite = i[i.__len__()-2]
            senquencesToCompare = findEqualBindingSites(bindingSite,proteinSequences[1:])
            
            for seq in mainSequence:
                mutations = compareSequences(seq,senquencesToCompare)
                print(mutations)
                
    
    break
    
    
