def newTrie(*words):
    tree = dict() #the tree as a dictionary
    for word in words:
        currentDict = tree
        c = ''
        for letter in word:
            c = c + letter
            currentDict = currentDict.setdefault(c,{})
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
        c = ''
        for letter in word:
            c = c + letter
            if(c in currentDict):
                currentDict = currentDict[c] #This will enable that if the letter already exists it will just get in it, NOT CREATE A NEW
            else:
                currentDict = currentDict.setdefault(c,{}) #And if not, it will Create one
        if('value' in currentDict): 
            currentDict['value'] = currentDict['value'] + 1  #If for some reason the word already exists, it will only Add +1 to the Counter
        else:
            currentDict['value'] = 1 #If not, it will create the Counter
            
    return currentDic #Returns the Trie's Tree

#
global teste
teste = []
global tete
tete = ''
def percorra(trie):
    aux = list(trie)
    #dictonon = trie
    #teste = []
    global tete
    for i in range(len(aux)):
        #teste.append(aux[i])
        if(len(aux) == 1 and 'value' in aux):
            continue
        if('value' in aux):
            #print(tete)
            tete = ''
            #print('ta aqui  ')
            #continue
        #print(inTrie(trie,tete))
        
        tete = aux[i]
        teste.append(tete)
        if(inTrie(trie,tete)):
            teste.append(tete)
            print(teste)
        print(tete)
        
        
            
        #print(trie)
        #print(inTrie(trie,tete))
        if(type(trie[aux[i]]) == int): #or type(aux[i]) == int):
            continue
        percorra(trie[aux[i]]) 

def percorraTor(trie,lista):
    tec = []
    while 'value' in lista:
        lista.remove('value')
    for i in range(len(lista)):
        if(inTrie(trie,lista[i])):
            tec.append(lista[i])
        
    return tec

#
def getVal(trie,word):
    if(not(inTrie(trie,word))):
        return 0
    currentDict = trie
    c = ''
    for letter in word:
        c = c + letter
        if(c in currentDict):
            currentDict = currentDict[c]
        else:
            return 0
    if('value' in currentDict):
        return currentDict['value']
    else:
        return 0

def getAll(trie,lista):
    listona = []
    for i in range(len(lista)):
        if(inTrie(trie,lista[i])):
            listona.append(getVal(trie,lista[i]))
    return listona

#you need to pass the Trie Tree and the word you are looking for
def inTrie(trie, word):
    currentDict = trie
    c = '' 
    for letter in word:
        c = c + letter
        #it runs every letter
        if(c in currentDict):
            #it will run until the last letter found
            currentDict = currentDict[c]
        else:
            return False
    else:
        #if it runs and FIND ALL LETTERS IN THE WORD
        #it will look if it has a value on it
        if ('value' in currentDict):
            return True
        else:
            return False




a = newTrie('bahea','bahea','salvado','salvador','sal','sal','bahia','sergipe')
print(a)
a = addTrie(a,'baba','salvei','presente','natal','natal','natalino')
print(a)
print(inTrie(a,'baba'))
print(inTrie(a,'natali'))
print(inTrie(a,'b'))
print(inTrie(a,'sal'))
percorra(a)
teste = percorraTor(a,teste)
print(teste)
print(len(teste))
print(getVal(a,'salv'))
print(getAll(a,teste))
