from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

def generating(artist, title, save):
        artist = artist.lower().replace(" ", "%20")
        title = title.lower().replace(" ", "%20")
        generate_url = 'http://azlyrics.com/lyrics/'+artist+'/'+title +'.html'
        processing(generate_url, artist, title, save)
        
def processing(generate_url, artist, title, save):
    response = urllib.request.urlopen(generate_url)
    read_lyrics = response.read()
    soup = BeautifulSoup(read_lyrics)
    lyrics = soup.find_all("div", attrs={"class": None, "id": None})
    lyrics = [x.getText() for x in lyrics]
    printing(artist, title, save, lyrics)
    
def printing(artist, title, save, lyrics):    
    for x in lyrics:
        print(x, end="\n\n")
    if save == True:
        saving(artist, title, lyrics)
    elif save == False:
        pass
            
def saving(artist, title, lyrics):
        f = open(artist + '_' + title + '.txt', 'w')
        f.write("\n".join(lyrics).strip())
        f.close()

        

