# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:46:36 2021

@author: Hao
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 19:33:41 2021

@author: HAO
"""

import requests
from bs4 import BeautifulSoup

soup=[]
for n in [3,4,6,7]:
    url = 'https://www.j-storm.co.jp/s/js/page/information?ima=0000&tpar=J000'+str(n)
    response = requests.get(url)
    soup.append(BeautifulSoup(response.text, "html.parser"))
    #print(soup.prettify())  #輸出排版後的HTML內容


l1=[]
l2=[]
Group=['TOKIO','嵐','KAT-TUN','Hey! Say! JUMP']

for n in range(0,len(soup)):
    result=soup[n].find_all("a","k-text")
    
    
    for r in result:
        if r.string != None:
            l1.append(r.string)
            l1.append('https://www.j-storm.co.jp'+r['href'])


infoLINK={'TOKIO':{l1[0]:l1[1],l1[2]:l1[3],l1[4]:l1[5]},
          '嵐':{l1[6]:l1[7],l1[8]:l1[9],l1[10]:l1[11],l1[12]:l1[13],l1[14]:l1[15]},
          'KAT-TUN':{l1[16]:l1[17],l1[18]:l1[19],l1[20]:l1[21],l1[22]:l1[23],l1[24]:l1[25],l1[26]:l1[27]},
          'Hey! Say! JUMP':{l1[28]:l1[29],l1[30]:l1[31],l1[32]:l1[33],l1[34]:l1[35],l1[36]:l1[37],l1[38]:l1[39]},
          }

import json
with open('infoLINK.json', 'w') as f:
      json.dump(infoLINK,f)