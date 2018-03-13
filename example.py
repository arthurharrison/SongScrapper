import WebScrapper as WS
import TrieOOP
import dataWriter as DW

WS.mainStarter('radiohead','Packt Like Sardines In A Crushed Tin Box', 'Pyramid Song', 'Pull / Pulk Revolving Doors', 'You And Whose Army?'
            , 'I Might Be Wrong', 'Knives Out', 'Amnesiac / Morning Bell', 'Dollars And Cents', 'Like Spinning Plates', 'Life In A Glass House')
data1 = WS.tree.getData(WS.tree)
data2 = WS.tree.getAll(data1)
DW.xlsxWriter(data1, data2, "amnesiac")
