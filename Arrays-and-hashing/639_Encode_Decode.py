def encode(strs):
    text = ""
    for x in strs:
        text += str(len(x)) + "#" + x
    return text


def decode(strs):
    hashFound = False
    wordLength = 0
    numStr = ""
    wrd = ""
    lst = []
    for x in strs:
        if wordLength == 0 and hashFound == False and x != "#":
            numStr += x
            hashFound = False
        elif wordLength == 0 and hashFound == False and x == "#":
            wordLength = int(numStr)
            hashFound = True
        elif wordLength > 0 and hashFound == True:
            wrd += x
            wordLength -= 1
        elif wordLength == 0 and hashFound == True:
            lst.append(wrd)
            wordLength = 0
            wrd = ""
            hashFound = False
    lst.append(wrd)
    return lst


enc = encode(['9#5belal5', '5#5hosen5555'])
dc = decode(enc)
print(enc)
print(dc)
