textDict = dict()
text1 = open("text1.txt", "r")
for line in text1:
    for word in line.split():
        if word in textDict:
            textDict[word] += 1
        else:
            textDict[word] = 1
textDictFile = open("textDict.txt", "w")
for word in textDict:
    textDictFile.write(word + ": " + str(textDict[word]) + "\n")
