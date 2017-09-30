#------------------------
#TODO: Documentation and other stuff
#------------------------
import re
import urllib.request as UrlReq
from bs4 import BeautifulSoup as BS
 

def get_lyrics(artist,songTitle):
    artist = artist.lower()
    songTitle = songTitle.lower()
    if artist.startswith("the "):# Remove starting 'the' from artist
        artist = artist[3:]

    # RegEx removes everything except alphanumeric characters from artist and songTitle
    artist = re.sub('[^A-Za-z0-9]+', "", artist)
    songTitle = re.sub('[^A-Za-z0-9]+', "", songTitle)
    
    url = "http://azlyrics.com/lyrics/"+artist+"/"+songTitle+".html"
    
    try:
        content = UrlReq.urlopen(url).read()
        soup = BS(content, 'html.parser')
        lyrics = str(soup)
        # lyrics lies between up_partition and down_partition
        up_partition = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
        down_partition = '<!-- MxM banner -->'
        lyrics = lyrics.split(up_partition)[1]
        lyrics = lyrics.split(down_partition)[0]
        lyrics = lyrics.replace('<br>','').replace('</br>','').replace('</div>','').strip()
        return lyrics
    except Exception as e:
        return "Exception occurred \n" +str(e)


#if its empty send a information
#ignore text beetween []. And ignore album, and EP
def get_band(artist):
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
        print(songs) #Debugger
    except Exception as e:
        return "Exception occurred \n" +str(e)


#Debugger
#x = get_lyrics('pink floyd',"Summer '68");
x = get_lyrics('The Who','My Generation')
#get_band('foo fighters')
print(x); 
