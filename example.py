import WebScrapper as WS
import TrieOOP
import dataWriter as DW

tree = TrieOOP.TreeTrie()
WS.passFunc(tree, 'radiohead','Packt Like Sardines In A Crushed Tin Box', 'Pyramid Song', 'Pull / Pulk Revolving Doors', 'You And Whose Army?'
            , 'I Might Be Wrong', 'Knives Out', 'Amnesiac / Morning Bell', 'Dollars And Cents', 'Like Spinning Plates', 'Life In A Glass House')
toList =  tree.percorra(tree.tree)
data1 = tree.percorraTor(toList)
data2 = tree.getAll(data1)
DW.xlsxWriter(data1, data2, "amnesiac")
