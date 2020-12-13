def solution(s):
    length = len(s)
    duoList = []
    
    if length == 0:
        return duoList
    elif length % 2 == 0:
        for indexNo in range(0, len(s)-1, 2):
            duo = s[indexNo] + s[indexNo+1]
            duoList.append(duo)
        return duoList
    else:
        s+="_"
        for indexNo in range(0, len(s)-1, 2):
            duo = s[indexNo] + s[indexNo+1]
            duoList.append(duo)
        return duoList

solution("abcdefg")