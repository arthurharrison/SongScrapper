value = 0 #unnecessary
def newTrie(*words):
    #print(words) #debug
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

#you need to pass the Trie Tree and the word you are looking for
def inTrie(trie, word):
    currentDict = trie
    for letter in word:
        #it runs every letter
        if(letter in currentDict):
            #it will run until the last letter found
            currentDict = currentDict[letter]
        else:
            return False
    else:
        #if it runs and FIND ALL LETTERS IN THE WORD
        #it will look if it has a value on it
        if ('value' in currentDict):
            return True
        else:
            return False

#remover
#In Progress
def remTrie(trie,word):
    currentDict = trie
    for letter in word:
        if(letter in currentDict): #it will run until the last letter found
            currentDict = currentDict[letter]
    else:
        if('value' in currentDict): # the last letter of a phrase
            if(len(currentDict) == 1):
                del[currentDict['value']]
            elif(len(currentDict) > 1):
                del[currentDict['value']]
    #print(currentDict)
    #print(trie) Debug
    return trie
            
            
                
                

    
    
arvore = newTrie('bahea','salvado','salvador','sal','sal','bahea','bahia','sergipe')
#print(arvore)
#print(inTrie(arvore,'ser'))
#teste = remTrie(arvore,'salvador')
#print(teste)
