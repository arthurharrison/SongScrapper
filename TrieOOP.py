class TreeTrie:
    #---------------
    #Do I Have something to say?
    #CurrentDict = the variable that is going to get in the Dictonary and explore every branch of it
    #progLetter = is the Progression of the word, it starts with the first letter and in the end will be the whole word
    #
    #--------------

    def __init__(self, *words):
        tree = dict() #the tree as a dictionary

        for word in words:
            currentDict = tree
            progLetter = ''
            for letter in word:
                progLetter = progLetter + letter
                currentDict = currentDict.setdefault(progLetter,{})
            if('value' in currentDict):
                currentDict['value'] = currentDict['value'] + 1
            else:
                currentDict['value'] = 1

        self.tree = tree #ATTENTION

    #Function that adds words in a already existed Trie's Tree
    #It works very similar to the creation of a new Tree's
    def addTrie(self,*words):

        for word in words: #looping all words given
            currentDict = self.tree 
            progLetter = ''
            for letter in word: #creating every letter of the given word
                progLetter = progLetter + letter
                if(progLetter in currentDict): #This will enable that if the letter already exists it will just get in it, NOT CREATE A NEW
                    currentDict = currentDict[progLetter]
                else:
                    currentDict = currentDict.setdefault(progLetter,{}) #And if not, it will Create one

            if('value' in currentDict): #it will enter in the final letter of the word
                currentDict['value'] = currentDict['value'] + 1  #If for some reason the word already exists, it will only Add +1 to the Counter
            else:
                currentDict['value'] = 1 #If not, it will create the Counter
                
        return self.tree

#-------------
#TODO: Delete ?
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
            return self.percorra(self.tree[aux[i]])
        


    #creates a list with all the itens found in the tree with value
    def percorraTor(self, lista):
        tec = []
        while 'value' in lista:
            lista.remove('value')
        for i in range(len(lista)):
            if(inTrie(self.tree,lista[i])):
                tec.append(lista[i])
            
        return tec
#------------------
    
    #It gets a value of a word
    def getVal(self, word):
        if(not(self.inTrie(word))):
            return 0
        currentDict = self.tree
        progLetter = ''
        for letter in word:
            progLetter = progLetter + letter
            if(progLetter in currentDict):
                currentDict = currentDict[progLetter]
            else:
                return 0
        if('value' in currentDict):
            return currentDict['value']
        else:
            return 0
    #It get all values of all words and returns a list with all the values
    #remember to compare with the entry list, because it save only the values
    def getAll(self, lista):
        listona = []
        for i in range(len(lista)):
            if(self.inTrie(lista[i])):
                listona.append(self.getVal(lista[i]))
        return listona

    #As the name says, 'in Trie ?'
    def inTrie(self, word):
        currentDict = self.tree
        progLetter = '' 
        for letter in word:
            progLetter = progLetter + letter
            #it runs every letter
            if(progLetter in currentDict):
                #it will run until the last letter found
                currentDict = currentDict[progLetter]
            else:
                return False
        else:
            #if it runs and FIND ALL LETTERS IN THE WORD
            #it will look if it has a value on it
            if ('value' in currentDict):
                return True
            else:
                return False



#Debugger
x = TreeTrie('salada')
print(x.tree)
#x.percorra(x.tree) #WRONG
print(x.addTrie('sal','salvador','salada','salada'))
ll = ['sal','salvador','salada']
print(x.getAll(ll))
print(x.getVal('salada'))
print(x.inTrie('sergipe'))
print(x.inTrie('sal'))
print(x.tree)


#Constructor CHECK
#AddTrie CHECK
#percorra NOT CHECK (?)
#percorraTor NOT CHECK (?)
#getVal CHECK
#getAll CHECK
#inTrie CHECK
