#! pyhton3
#Dmusic-download music

import requests,bs4,webbrowser
from urllib.request import urlopen

def dload(song,artist):
    print("Searching for %s by %s"%(song,artist))
    
    res=requests.get('https://www.google.co.in/search?q=parent+directory+%s+%s'%(song.replace(' ','+'),artist.replace(' ','+')))
    if res.status_code!=requests.codes.ok:
        return -1
    soup=bs4.BeautifulSoup(res.text,"html.parser")
    elems=soup.select('.s cite')
    n=0
    while n!= -1:
        
        res2=requests.get('http://%s'%elems[n].getText())
        if res2.status_code==requests.codes.ok:
            print("happy")
        soup2=bs4.BeautifulSoup(res2.text,"html.parser")
        elems2=soup2.select('a')
        for i in range(0,len(elems2)):
            if song in elems2[i].getText().lower():
                print(elems2[i].getText()) 
                link='http://'+elems[n].getText()+elems2[i].get('href')
                print(link)
                openmp3=open('song.mp3','wb')
                dl=urlopen(link)
                dl2=dl.read()
                openmp3.write(dl2)
                openmp3.close()
                print("DONE>>>>>>>>>")


            print('..')
        n+=1

        
        
if __name__=='__main__':
    song=input("enter the name of the song > ")
    artist=''
    artist=input("enter the name of the artist(optional) > ")
    flag = dload(song,artist)
    print(flag)
