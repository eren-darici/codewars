def decodeMorse(morse_code):
    stuff = morse_code.split(" ")
    finalString = ""

    for i in range(len(stuff)):
        if stuff[i] != "":
            finalString += MORSE_CODE[stuff[i]]
        elif i != len(stuff)-1:
            if stuff[i] =="" and stuff[i+1] == "" and stuff[i-1] != "":
                finalString += " "
            
        

    return finalString.strip()
