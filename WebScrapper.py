#TODO: Make everything asynchronous? Add a limit of songs to scrap, so it doesnt overrun the server
import re
import urllib.request as UrlReq
from bs4 import BeautifulSoup as BS
import TrieOOP
import time
import dataWriter as DW


def getLyrics(artist,songTitle, treatment = False ): #when treatment works make it true
    """Given the artist and the song you will get the Lyrics of the song

    Args: Artist, Song Title

    Return: Song Lyric
    """
    notWanted = ['the','a','an','to','for','in','on','at'] #articles, prepositions -> words that are not usable in the analysis
    #toChange = ['ive','youre'] #words that are actually two ; I don't know if i want to create a loop for this
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
        #THIS DOESNT WORK, WHY???????????????????
        if ('ive' in lyrics and treatment == True):
            lyrics = re.sub(r'\bive\b','i have',lyrics)
        if(treatment == True):
            for y in range(len(notWanted)):
                #editor = re.sub(r"\b%s\b" % s[0] , s[1], editor)
                lyrics = re.sub(r"\b%s\b"%notWanted[y],'',lyrics)
                print(len(notWanted),y)
                #lyrics =lyrics.replace(notWanted[i],'').strip()
        #WHY IT DOESNT WORK??????
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


def getAllBandLyrics():
    #This is only a test
    listlyr = []
    try:
        songs = getBandSongs('them crooked vultures')
        for i in range(len(songs)):
            lyrics = getLyrics('them crooked vultures',songs[i])
            listlyr.append(lyrics)
            print('%.2f' %(i*100/len(songs)),songs[i])
            """if(not bool(i % 5)):
                time.sleep(2)"""
    except Exception as e:
        print(str(e))
        #return "Exception occurred \n" + str(e)
    return listlyr


def passFunc(tree, band, *songs):
    for song in songs:
        actualSong = getLyrics(band, song)
        actualSong = actualSong.split('\n')
        for x in actualSong:
            y = re.sub('[^A-Za-z ]',"",x)
            y = y.split(' ')
            for y in y:
                if y == '' or y == 'x': continue
                #print(y)
                tree.addTrie(y.lower())
#Debugger
'''

#x = getLyrics('them crooked vultures','bandoliers')
x = getLyrics('pink floyd',"echoes")
#x = getAllBandLyrics()
x = x.split('\n')
for x in x:
    y = re.sub('[^A-Za-z ]',"",x)
    y = y.split(' ')
    for y in y:
        if y=='' or y == 'x': continue
        print(y)
        tree.addTrie(y.lower())
'''
tree = TrieOOP.TreeTrie()
passFunc(tree, 'pink floyd','speak to me', 'breathe', 'time', 'the great gig in the sky', 'money', 'us and them', 'brain damage', 'eclipse')
#passFunc(tree, 'radiohead','15 step', 'bodysnatchers', 'lotus flower')
#print(tree.tree)
toList = tree.percorra(tree.tree)
data1 = tree.percorraTor(toList)
data2 = tree.getAll(data1)
DW.xlsxWriter(data1, data2, "darkside2")
print("-Tree Information-\nNumber of unique words: {0} \nTotal number of words: {1}".format(len(tree.percorraTor(toList)),tree.sumAll(toList)))
"""
x = getLyrics('pink floyd',"paintbox")
print(getBandSongs('foo fighters'))
print(x);
"""