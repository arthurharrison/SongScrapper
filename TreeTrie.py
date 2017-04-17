def newTrie(*words):
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

def getValues(trie):
    currentDict = trie
    raiz = list(currentDict)
    if(raiz[0] != 'value' and len(raiz) > 0):
        for i in range(len(raiz)):
            percorre(raiz[i])
        
def percorra2(trie):
    aux = list(trie)
    while ( aux[0] != 'value' and len(aux) > 0):
        percorra2(trie(aux[0]))
global teste
teste = []
global tete
tete = ''
def percorra(trie):
    aux = list(trie)
    #teste = []
    global tete
    for i in range(len(aux)):
        #teste.append(aux[i])
        
        #print(tete)
        if(aux[i] == "value"):
            print(tete)
            tete = ''
            print('ta aqui  ')
            continue
        tete += aux[i]
        percorra(trie[aux[i]]) 
    

def getValue(trie):
    currentDict = trie
    raiz = list(currentDict)
    for i in range(len(raiz)): #percorrer todos os nos
        return False #tirar

        #parei de programar pois percebi que devera ser algo recursivo e nao forçar com loops :(
    


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
def remTrie(trie,*words):
    currentDic = trie
    for word in words:
        currentDict = currentDic
        for letter in word:
            if(letter in currentDict): #it will run until the last letter found
                currentDict = currentDict[letter]
        else:
            if('value' in currentDict): # the last letter of a phrase
                if(len(currentDict) == 1):
                    del[currentDict['value']]
                    #del[currentDict]
                elif(len(currentDict) > 1):
                    del[currentDict['value']]
                    
    return currentDic
            

#DEBUGER - OUTPUT             
arvore = newTrie('bahea','salvado','salvador','sal','sal','bahea','bahia','sergipe')
print(arvore)
arvore = addTrie(arvore,'banana','presunto','bahia')
print('\n\n\n')
print(arvore)
arvore = remTrie(arvore,'salvador','salvado')
print('\n\n\n')
print(arvore)
print(inTrie(arvore,'ser'))
print(inTrie(arvore,'presunto'))
print(percorra(arvore))
