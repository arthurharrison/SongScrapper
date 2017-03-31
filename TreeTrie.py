value = 0
def newTrie(*words):
    print(words)
    tree = dict() #the tree as a dictionary
    for word in words:
        currentDict = tree
        for letter in word:
            currentDict = currentDict.setdefault(letter,{})
            #currentDict['value'] = value
        if('value' in currentDict):
            currentDict['value'] = currentDict['value'] + 1
        else:
            currentDict['value'] = 1
            
    return tree

print(newTrie('bahea','salvado','salvador','sal','sal','bahea','bahia','sergipe'))
