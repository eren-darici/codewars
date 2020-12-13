def find_it(seq):
    setSeq = set(seq)
    occurenceList = []
    for item in setSeq:
        occurenceList.append(seq.count(item))
    

    setSeq = list(setSeq)

    indexOf = 0

    for item in occurenceList:
        if item % 2 != 0:
            indexOf = occurenceList.index(item)
    
    
    return setSeq[indexOf]

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))