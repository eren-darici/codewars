def number(lines):
    newList = []
    if len(lines) == 0:
        return []
    else:
        for i in range(len(lines)):
            newList.append("{}: {}".format(i+1, lines[i]))
    
    return newList

