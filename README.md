<p align="center">
  <h1 align="center">SongScrapper</h1>
  <p  align="center">A WebScrapper for your favourite bands</p>
  <p align="center">Join explore & Fun</p>
</p>

### What is it? 
* My first published project :')
* A Code that collect the lyrics from a website and writes in a .xlsx file the word and the number of times it shows;
* It also uses Tree Trie Data Structure, so you can use it into another project in case you need this kind of Data Structure.

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
- [x] Make a better console output (?)
- [ ] Conquer the World
- [ ] Create a good Readme for this project

### How does it work?
The 3 Scripts that I used will gather the Data, deal with the Data and write the Data.
* WebScrapper.py module gets the data;
* TrieOOP.py is the Data Structure, it will save the data has a Tree and make it ready and easy to use for what you need;
* dataWriter.py will get the Data from TrieOOP and write it in a .xlsx file with two rows (Word and Value).

You can find more information in the documentation of the Code.

### Examples
```python
import WebScrapper as WS
import TrieOOP
import dataWriter as DW

WS.mainStarter('radiohead', *getAlbumSongs('radiohead', 'amnesiac'))
data1 = WS.tree.getData(WS.tree)
data2 = WS.tree.getAll(data1)
DW.xlsxWriter(data1, data2, "amnesiac")
```
* It will print the following feedback:
```shell
Scraping packt like sardines in a crushed tin box --- Song 1 of 10
Scraping pyramid song --- Song 2 of 10
Scraping pull / pulk revolving doors --- Song 3 of 10
Scraping you and whose army? --- Song 4 of 10
Scraping i might be wrong --- Song 5 of 10
Scraping knives out --- Song 6 of 10
Scraping amnesiac / morning bell --- Song 7 of 10
Scraping dollars and cents --- Song 8 of 10
Scraping like spinning plates --- Song 9 of 10
Scraping life in a glass house --- Song 10 of 10
```

* This is the example.py script, it will create a .xlsx file with the information gathered of the album Amnesiac.

### What we've learned
* How to gather information directly from a WebSite (Web Scrap);

* How to use Tableau to create a image with the Data;

* And in The Dark Side of The Moon the word 'love' appear only once ,but 'mad' appears 6 times.

---
### Contribuitors

![avatar arthur](https://avatars1.githubusercontent.com/u/22755581?s=130&v=4) | ![avatar lucas](https://avatars3.githubusercontent.com/u/26311458?s=130&v=4)
-------------------------------------------------------------------------- | --------------------------------------------------------------------------
  [Arthur Tavares](https://github.com/arthurharrison)                         |  [Lucas Menezes](https://github.com/lucas-menezes)
