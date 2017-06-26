#!/usr/bin/env pyhton
#Musicbot-download music!

import requests, bs4, webbrowser
from urllib.request import urlopen
import urllib
from urllib import parse

def dload(song,artist):
    print("Searching for %s by %s"%(song,artist))
    # Search on google for the music
    res=requests.get('https://www.google.co.in/search?q=parent+directory+%s+%s'%(song.replace(' ','+'),artist.replace(' ','+')))
    if res.status_code!=requests.codes.ok:
        return -1
    soup=bs4.BeautifulSoup(res.text,"html.parser")
    elems=soup.select('.s cite')
    n=0
    # iterate through the results
    while n!= -1:
        
        res2=requests.get('http://%s'%elems[n].getText())
        if res2.status_code==requests.codes.ok:
            print("happy")
        soup2=bs4.BeautifulSoup(res2.text,"html.parser")
        elems2=soup2.select('a')
        # iterate through the files to fing the right mp3
        for i in range(0,len(elems2)):
            if song in elems2[i].getText().lower() and '.mp3' in elems2[i].getText().lower():
                try:
                    print('Found : %s'%elems2[i].getText()) 
                    print('*** Downloading %s ***'%song)

                    link='http://'+elems[n].getText()+elems2[i].get('href')

                    #print(link)
                    link = urllib.parse.quote(link)
                    #print(urllib.parse.unquote(link))
                    openmp3=open(song+'.mp3','wb')
                    dl=urlopen(urllib.parse.unquote(link))
                    # dl=urlopen(link)
                    dl2=dl.read()
                    openmp3.write(dl2)
                    openmp3.close()
                    print("<<<<<<<   DONE   >>>>>>>")
                    n=-2
                    return 1
                except:
                    continue


            print('..')

        n+=1
        if(n>10):
            print("\n\n Sorry could not find %s by %s\nEXITING...."%(song,artist))
            n=-1
            return -1

        
        
if __name__=='__main__':
    op='y'
    while op == 'y':
        song=input("enter the name of the song > ")
        artist=''
        artist=input("enter the name of the artist(optional) > ")
        flag = dload(song,artist)
        if flag == -1:
            print("Sorry, clould not find '%s' by '%s' OR an unexpected error occured"%(song,artist))
        op=input("Do you want to download more(n/y)? ")
    

