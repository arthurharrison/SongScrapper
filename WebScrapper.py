#TODO: Make everything asynchronous?
import re
import urllib.request as UrlReq
from bs4 import BeautifulSoup as BS
import TrieOOP


def getLyrics(artist,songTitle):
    """Given the artist and the song you will get the Lyrics of the song

    Args: Artist, Song Title

    Return: Song Lyric
    """
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
        upPartition = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
        downPartition = '<!-- MxM banner -->'
        lyrics = lyrics.split(upPartition)[1]
        lyrics = lyrics.split(downPartition)[0]
        lyrics = lyrics.replace('<br>','').replace('</br>','').replace('</div>','').strip()
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
        songs = getBandSongs('pink floyd')
        for i in range(len(songs)):
            lyrics = getLyrics('pink floyd',songs[i])
            listlyr.append(lyrics)
            print('%.2f' %(i*100/len(songs)),songs[i])
    except Exception as e:
        print(str(e))
        #return "Exception occurred \n" + str(e)
    return listlyr


#Debugger
tree = TrieOOP.TreeTrie('then', 'i', 'forget')
#print(getAllBandLyrics())
#print(tree.tree)
print(getBandSongs('foo fighters'))
"""
x = getLyrics('pink floyd',"paintbox")
print(getBandSongs('foo fighters'))
print(x);
"""