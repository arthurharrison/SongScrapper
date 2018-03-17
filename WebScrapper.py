import re
import urllib.request as UrlReq
from bs4 import BeautifulSoup as BS
import TrieOOP
import time
import dataWriter as DW


def getLyrics(artist,songTitle, treatment = True ): #when treatment works make it true
    """Given the artist and the song you will get the Lyrics of the song

    Args: Artist, Song Title

    Return: Song Lyric
    """
    notWanted = ['the','a','an','and','it','to','for','in','on','of','at','as', 'is', 'are'] #articles, prepositions -> words that are not usable in the analysis (Reconsider the words used)
    toChange = ['ive','im','id','its','youre','youd','youll','shes','hes','itll'] #words that are actually two ; I don't know if i want to create a loop for this
    toChanged = ['i have', 'i am','i would','it is', 'you are','you would','you will','she is', 'he is', 'it will']
    artist = artist.lower()
    songTitle = songTitle.lower()
    if artist.startswith("the "):
        artist = artist[3:]
    artist = re.sub('[^A-Za-z0-9]+', "", artist)
    songTitle = re.sub('[^A-Za-z0-9]+', "", songTitle)

    url = "http://azlyrics.com/lyrics/"+artist+"/"+songTitle+".html"

    try:
        content = UrlReq.urlopen(url).read()
        soup = BS(content, 'html.parser')
        lyrics = str(soup)
        lyrics = lyrics.split('<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->')[1]
        lyrics = lyrics.split('<!-- MxM banner -->')[0]
        lyrics = lyrics.replace('<br>','').replace('</br>','').replace('</div>','').strip()
        if('<i>' in lyrics):
            lyrics = lyrics.replace('<i>','').replace('</i>','').strip()
        lyrics = lyrics.lower()
        lyrics = re.sub('[^a-z\n ]+', "", lyrics)
        
        if(treatment == True):
            for i, word in enumerate(toChange):
                lyrics = re.sub(r"\b%s\b"%word, toChanged[i], lyrics)
            for y in notWanted:
                lyrics = re.sub(r"\b%s\b"%y,'',lyrics)

        return lyrics
    except Exception as e:
        return "Exception occurred \n" + str(e)


def getBandSongs(artist):
    """Given the Artist you will get all the songs from all the albums and EPs

    Args: Artist

    Return: A List with all the songs
    """
    artist = artist.lower()
    if artist.startswith("the "):
        artist = artist[3:]

    artist = re.sub('[^A-Za-z0-9]+', "", artist)

    url = "http://www.azlyrics.com/"+artist[0]+"/"+artist+".html"

    try:
        content = UrlReq.urlopen(url).read()
        soup = BS(content, 'html.parser')
        songs = []
        songsBackbone = str(soup)
        songsBackbone = songsBackbone.split('songlist')[1]
        songsBackbone = songsBackbone.split('var res')[0]
        for i in range(len(songsBackbone))[1::]:
            try:
                passValue = songsBackbone.split("s:")[i]
                passValue = passValue.split('", h:')[0]
                songs.append(passValue.split('"')[1])
            except IndexError:
                break
        return songs 
    except Exception as e:
        return "Exception occurred \n" + str(e)


def getAlbumSongs(band, album):
    """ Given the Artist and album you will get all songs from the album given

    Args: Band name and Album

    Return: a List of Songs from the Album
    """
    band = band.lower()
    if band.startswith("the "):
        band = band[3:]

    band = re.sub('[^A-Za-z0-9]+',"", band)

    url = "http://www.azlyrics.com/"+band[0]+"/"+band+".html"

    try:
        content = UrlReq.urlopen(url).read()
        soup = BS(content, 'html.parser')
        songs = []
        backbone = str(soup).lower()
        backbone = backbone.split('<div id="listalbum">')[1]
        backbone = backbone.split('album: <b>"%s"</b>'%album)[1]
        backbone = backbone.split('</div>')[1]
        backbone = backbone.split('<a id=')[0]
        backbone = backbone.split('target="_blank">')[1:]
        for i in backbone:
            song = i.split('</a>')[0]
            songs.append(song)
            
        return songs
        
    except Exception as e:
        return "Exception occurred \n" + str(e)


def getAllBandLyrics(band):
    listlyr = []
    counter = 1
    try:
        songs = getBandSongs(band)
        for song in songs:
            counter = counter + 1
            #I don't want to overrun the website, maybe later it would be better to find a new way.
            if(not counter % 12):
                time.sleep(10)
            if(not counter % 20):
                time.sleep(40)

            lyrics = getLyrics(band,song)
            listlyr.append(lyrics)
    except Exception as e:
        print(str(e))
        
    return listlyr


def passFunc(tree, band, *songs):
    """ It work as a 'Messenger' it get a generator with the song titles and get the lyric one by one; then puts on the Tree Trie

    Args: The Tree, The Band name, and any number of songs

    Return: None, it just adds in the Tree Trie
    """
    counter = 1
    for i, song in enumerate(songs):
        counter = counter + 1
        print('Scraping {0} --- Song {1} of {2}'.format(song, i+1, len(songs)))
        #I don't want to overrun the website, maybe later it would be better to find a new way.
        if(not counter % 12):
            time.sleep(10)
        if(not counter % 20):
            time.sleep(40)
        actualSong = getLyrics(band, song)
        actualSong = actualSong.split('\n')
        
        for x in actualSong:
            y = x.split(' ')
            for y in y:
                if y == '' or y == 'x': continue
                tree.addTrie(y)
        

def mainStarter(band, *songs):
    """ It makes the module easier to use and to call.
    We will always use this configuration, at least 99% of the time, so making a function that do this work is a good thing

    Args: The Band and the songs that we will gather the Data from

    Return: None, the function only exists to execute other functions
    """
    global tree
    tree = TrieOOP.TreeTrie()
    passFunc(tree, band, *songs)
    

#Debugger
if __name__ == "__main__":
    mainStarter('radiohead', *getAlbumSongs('radiohead', 'amnesiac'))
    data1 = tree.getData(tree)
    data2 = tree.getAll(data1)
    DW.xlsxWriter(data1, data2, "amnesiac")
    print("-Tree Information-\nNumber of unique words: {0} \nTotal number of words: {1}".format(len(data1),tree.sumAll(data1)))
    