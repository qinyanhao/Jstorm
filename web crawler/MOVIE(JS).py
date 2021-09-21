# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 17:40:34 2021

@author: Hao
"""

import requests
from bs4 import BeautifulSoup

Jurl = 'https://www.j-storm.co.jp/s/js/artist/J0007?ima=0000'
Jresponse = requests.get(Jurl)
Jsoup=BeautifulSoup(Jresponse.text, "html.parser")

Jresult=Jsoup.find_all('a','movieItem--image movie_button')

l1=[]
l2=[]
l3=[]

for r in Jresult:
    l2.append(r['data-youtubeid'])
    l1.append(r['onclick'])
    
for e in l1:
    a=e.replace("ga('send', 'event', 'play-video', 'heysayjump_video_list', '","")
    b=a.replace("_video_heysayjump');","")
    l3.append(b)

jumpMOVIE={l3[0]:'https://www.youtube.com/watch?v='+l2[0],
           l3[1]:'https://www.youtube.com/watch?v='+l2[1],
           l3[2]:'https://www.youtube.com/watch?v='+l2[2],
           l3[3]:'https://www.youtube.com/watch?v='+l2[3],
           l3[4]:'https://www.youtube.com/watch?v='+l2[4],
           l3[5]:'https://www.youtube.com/watch?v='+l2[5],
           l3[6]:'https://www.youtube.com/watch?v='+l2[6],
           l3[7]:'https://www.youtube.com/watch?v='+l2[7],
           l3[8]:'https://www.youtube.com/watch?v='+l2[8],
           l3[9]:'https://www.youtube.com/watch?v='+l2[9]}


Kurl = 'https://www.j-storm.co.jp/s/js/artist/J0006?ima=0000'
Kresponse = requests.get(Kurl)
Ksoup=BeautifulSoup(Kresponse.text, "html.parser")

Kresult=Ksoup.find_all('a','movieItem--image movie_button')

l4=[]
l5=[]
l6=[]

for r in Kresult:
    l4.append(r['onclick'])
    
for n in range(0,8):
    l5.append(list(Kresult)[n]['data-youtubeid'])
    
for e in l4:
    a=e.replace("ga('send', 'event', 'play-video', 'kat-tun_video_list', '","")
    b=a.replace("_video_kat-tun');","")
    l6.append(b)
    
ktMOVIE={l6[0]:'https://www.youtube.com/watch?v='+l5[0],
         l6[1]:'https://www.youtube.com/watch?v='+l5[1],
         l6[2]:'https://www.youtube.com/watch?v='+l5[2],
         l6[3]:'https://www.youtube.com/watch?v='+l5[3],
         l6[4]:'https://www.youtube.com/watch?v='+l5[4],
         l6[5]:'https://www.youtube.com/watch?v='+l5[5],
         l6[6]:'https://www.youtube.com/watch?v='+l5[6],
         l6[7]:'https://www.youtube.com/watch?v='+l5[7]}

Aurl = 'https://www.j-storm.co.jp/s/js/artist/J0004?ima=0000'
Aresponse = requests.get(Aurl)
Asoup=BeautifulSoup(Aresponse.text, "html.parser")

Aresult=Asoup.find_all('a','movieItem--image movie_button')

l7=[]
l8=[]
l9=[]

for r in Aresult:
    l7.append(r['onclick'])
    
    
for e in l7:
    a=e.replace("ga('send', 'event', 'play-video', 'arashi_video_list', '","")
    b=a.replace("_video_arashi');","")
    l9.append(b)
    
arsMOVIE={l9[0]:'https://www.youtube.com/watch?v='+list(Aresult)[0]['data-youtubeid'],
         l9[1]:'https://www.youtube.com/watch?v='+list(Aresult)[1]['data-youtubeid'],
         l9[2]:'https://www.youtube.com/watch?v='+list(Aresult)[2]['data-youtubeid'],
         l9[3]:'https://www.youtube.com/watch?v='+list(Aresult)[3]['data-youtubeid'],
         l9[4]:'https://www.youtube.com/watch?v='+list(Aresult)[4]['data-youtubeid'],
         l9[5]:'https://www.youtube.com/watch?v='+list(Aresult)[5]['data-youtubeid'],
         l9[7]:'https://www.youtube.com/watch?v='+list(Aresult)[7]['data-youtubeid'],
         l9[8]:'https://www.youtube.com/watch?v='+list(Aresult)[8]['data-youtubeid']
        }

movieDICT={"嵐":arsMOVIE,"KAT-TUN":ktMOVIE,"Hey! Say! JUMP":jumpMOVIE}

import json
with open('movieDICT.json', 'w') as f:
      json.dump(movieDICT,f)
