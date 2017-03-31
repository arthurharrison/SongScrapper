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


#Function that adds words in a already existed Trie's Tree
#It works very similar to the creation of a new Tree's
def addTrie(trie,*words):
    currentDic = trie #It  receives the Tree's to a variable that will change
    for word in words:
        currentDict = currentDic #CurrentDic will bet the variable that is going to get in the Dictonary
        for letter in word:
            if(letter in currentDict):
                currentDict = currentDict[letter] #This will enable that if the letter already exists it will just get in it, NOT CREATE A NEW
            else:
                currentDict = currentDict.setdefault(letter,{}) #And if not, it will Create one
        if('value' in currentDict): 
            currentDict['value'] = currentDict['value'] + 1  #If for some reason the word already exists, it will only Add +1 to the Counter
        else:
            currentDict['value'] = 1 #If not, it will create the Counter
            
    return currentDic #Returns the Trie's Tree
        
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
print(arvore)
arvore = addTrie(arvore,'banana','presunto','bahia')
print(arvore)
#print(inTrie(arvore,'ser'))
#teste = remTrie(arvore,'salvador')
#print(teste)
