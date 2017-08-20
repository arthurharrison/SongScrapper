class TreeTrie:
    #---------------
    #some mistakes of security were made
    #global teste
    #global tete
    #tete = ''
    #--------------


    teste = [] #inicializando variavel necessária
    #Function newTrie
    def __init__(self, *words):
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
                
        #return tree
        self.tree = tree #ATTENTION

    #Function that adds words in a already existed Trie's Tree
    #It works very similar to the creation of a new Tree's
    def addTrie(self,*words):
        currentDic = self.tree                       #trie #It  receives the Tree's to a variable that will change TESTE


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


    def percorra(self, trie):
        aux = list(self.tree)
        tete = ''
        teste=[]
        self.teste = teste
        for i in range(len(aux)):
            if(len(aux) == 1 and 'value' in aux):
                continue
            if('value' in aux):#if it encounters a 'word' it resets the counter
                tete = ''
            
            tete = aux[i]
            teste.append(tete)
            
            #print(tete)#debugger
            #print(trie) #debugger
            #print(inTrie(trie,tete))#debugger
            if(type(self.tree[aux[i]]) == int): #or type(aux[i]) == int):
                continue
            self.percorra(self.tree[aux[i]])

    #creates a list with all the itens found in the tree with value
    def percorraTor(self, lista):
        tec = []
        while 'value' in lista:
            lista.remove('value')
        for i in range(len(lista)):
            if(inTrie(self.tree,lista[i])):
                tec.append(lista[i])
            
        return tec

    #It gets a value of a word
    def getVal(self, word):
        if(not(inTrie(self.tree,word))):
            return 0
        currentDict = self.tree
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
    #It get all values of all words and returns a list with all the values
    #reomember to compare with the entry list, because it save only the values
    def getAll(self, lista):
        listona = []
        for i in range(len(lista)):
            if(inTrie(self.tree,lista[i])):
                listona.append(getVal(self.tree,lista[i]))
        return listona

    #you need to pass the Trie Tree and the word you are looking for
    def inTrie(self, word):
        currentDict = self.tree
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

x = TreeTrie('salada')
print(x.tree)
x.percorra(x.tree)
x.addTrie('sal','salvador')

print(x.inTrie('sergipe'))
print(x.inTrie('sal'))
print(x.tree)


#Constructor CHECK
#AddTrie CHECK
#percorra NOT CHECK
#percorraTor NOT CHECK
#getVal NOT CHECK
#getAll NOT CHECK
#inTrie CHECK