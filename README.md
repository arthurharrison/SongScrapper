<p align="center">
  <h1 align="center">SongScrapper</h1>
  <p  align="center">A WebScrapper but with your favorite band songs.</p>
</p>

### What is it? 
* My first published project :')
* A Code that collect the lyrics from a website and writes in a .xlsx file the word and the number the times it shows
* It also uses Tree Trie Data Structure, so it can be harvested into another project in case you need this kind of Data Structure

Here's what I was able to do with the Data and the help of [Tableau](https://tableau.com) for visualiation purposes.

Have a look in this Word Cloud image made with the words that we retrieve from the album The Dark Side of The Moon by Pink Floyd
![darkside of the moon](https://i.imgur.com/buMJFIp.png)

And here is another Word Cloud image from the words gathered from the album Amnesiac by Radiohead
![amnesiac](https://i.imgur.com/NUQw5Wc.png)

### Work to do
- [x] Get Lyrics in AZLycrics.com
- [x] Construct a Tree Trie
- [x] Make the Data ready for use (.csv)
- [x] Create things with the Data
- [ ] Make the code more customable and easier for use
- [ ] Make it automatic (maybe?)
- [ ] Make a better console output (?)
- [ ] Conquer the World
- [ ] Create a good Readme for this project

### How does it work?
The 3 Scripts that I used will gather the Data, deal with the Data and write the Data.
* WebScrapper module gets the data;
* TrieOOP is the Data Structure, it will save the data has a Tree and make it ready and easy to use for what you need;
* dataWriter will get the Data from TrieOOP and write it in a .xlsx file with two rows (Word and Value).

You can find more information in the documetation of the Code.

### Examples
```python
import WebScrapper as WS
import TrieOOP
import dataWriter as DW

tree = TrieOOP.TreeTrie()
WS.passFunc(tree, 'radiohead','Packt Like Sardines In A Crushed Tin Box','Pyramid Song', 'Pull / Pulk Revolving Doors','You And Whose Army?'
            ,'I Might Be Wrong','Knives Out','Amnesiac / Morning Bell','Dollars And Cents','Like Spinning Plates','Life In A Glass House')
toList =  tree.percorra(tree.tree)
data1 = tree.percorraTor(toList)
data2 = tree.getAll(data1)
DW.xlsxWriter(data1, data2, "amnesiac")
```
* This is the example.py script, it will create a .xlsx file with the information gathered of the album Amnesiac.
* I typed song by song of the album, but later I will make it easier to call an album.

### What we've learned
* How to gather information directly from a WebSite (Web Scrap);

* Other Stuff 

---
### Contribuitors

![avatar arthur](https://avatars1.githubusercontent.com/u/22755581?s=130&v=4) | ![avatar lucas](https://avatars3.githubusercontent.com/u/26311458?s=130&v=4)
-------------------------------------------------------------------------- | --------------------------------------------------------------------------
  [Arthur Tavares](https://github.com/arthurharrison)                         |  [Lucas Menezes](https://github.com/lucas-menezes)