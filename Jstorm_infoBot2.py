# -*- coding:utf-8 -*-

import logging
import datetime
import discord
import json
import math
import re
from pprint import pprint

from Jstorm2 import runLoki
logging.basicConfig(level=logging.INFO)

# <取得多輪對話資訊>
client = discord.Client()

requestTemplate ={"group":"",
                 "member": "",
                 "request": "",}

mscDICT = {# "userID": {requestTemplate}
           }
# </取得多輪對話資訊>

with open("account.info", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())
# 另一個寫法是：accountDICT = json.load(open("account.info", encoding="utf-8"))
with open('D:\HAO\Hao的研所\實習\Jstorm\ProfileDICT.json', 'r') as f:
    ProfileDICT=json.load(f)

tokio=['国分太一','城島茂','松岡昌宏']
arashi=['相葉雅紀','松本潤','二宮和也','大野智','櫻井翔']
kattun=['亀梨和也','上田竜也','中丸雄一']
jump=['山田涼介','知念侑李','中島裕翔','有岡大貴','髙木雄也','伊野尾慧','八乙女光','薮宏太']

ageDICT={"TOKIO":['城島茂','国分太一','松岡昌宏'],
         "嵐":['大野智','櫻井翔','相葉雅紀','二宮和也','松本潤'],
         "KAT-TUN":['中丸雄一','上田竜也','亀梨和也'],
         "Hey! Say! JUMP":['薮宏太','髙木雄也','伊野尾慧','八乙女光','有岡大貴','山田涼介','中島裕翔','知念侑李']}

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Loki Result => {}".format(resultDICT))
    return resultDICT

def findAge(name): #計算歲數
    '''
    輸入：全名
    輸出：歲數(int)
    '''
    if name in tokio:
        for n in range(0,len(ProfileDICT['TOKIO'])):
         if ProfileDICT['TOKIO'][n]['JName']==name:
             birth=ProfileDICT['TOKIO'][n]['Birth'].split(".")
    if name in arashi:
        for n in range(0,len(ProfileDICT['嵐'])):
         if ProfileDICT['嵐'][n]['JName']==name:
             birth=ProfileDICT['嵐'][n]['Birth'].split(".")
    if name in kattun:
        for n in range(0,len(ProfileDICT['KAT-TUN'])):
         if ProfileDICT['KAT-TUN'][n]['JName']==name:
             birth=ProfileDICT['KAT-TUN'][n]['Birth'].split(".")
    if name in jump:
        for n in range(0,len(ProfileDICT['Hey! Say! JUMP'])):
         if ProfileDICT['Hey! Say! JUMP'][n]['JName']==name:
             birth=ProfileDICT['Hey! Say! JUMP'][n]['Birth'].split(".")
    
    birthday=datetime.date(year=int(birth[0]),month=int(birth[1]),day=int(birth[2]))
    today=datetime.date.today()
    age= math.floor((today-birthday).days/365)
    
    return age

def findHeight(name):
    '''
    輸入：全名
    輸出：身高(int)
    '''
    if name in tokio:
        for n in range(len(ProfileDICT["TOKIO"])):
           if name == ProfileDICT["TOKIO"][n]['JName']:
               height=ProfileDICT["TOKIO"][n]['height']
    if name in arashi:
         for n in range(len(ProfileDICT["嵐"])):
            if name == ProfileDICT["嵐"][n]['JName']:
                height=ProfileDICT["嵐"][n]['height']                             
    if name in kattun:
         for n in range(len(ProfileDICT["KAT-TUN"])):
            if name == ProfileDICT["KAT-TUN"][n]['JName']:
                height=ProfileDICT["KAT-TUN"][n]['height']   
    if name in jump:
         for n in range(len(ProfileDICT["Hey! Say! JUMP"])):
            if name == ProfileDICT["Hey! Say! JUMP"][n]['JName']:
                height=ProfileDICT["Hey! Say! JUMP"][n]['height']  
    return height

def findBirthday(name):
    '''
    輸入：全名
    輸出：[年,月,日]
    '''
    birthday=[]
    if name in tokio:
        for n in range(len(tokio)):
            if name==ProfileDICT["TOKIO"][n]["JName"]:
                birthday = ProfileDICT["TOKIO"][n]["Birth"].split(".")
    if name in arashi:
        for n in range(len(arashi)):
            if name==ProfileDICT["嵐"][n]["JName"]:
                birthday = ProfileDICT["嵐"][n]["Birth"].split(".")
    if name in kattun:
        for n in range(len(kattun)):
            if name==ProfileDICT["KAT-TUN"][n]["JName"]:
                birthday = ProfileDICT["KAT-TUN"][n]["Birth"].split(".")
    if name in jump:
        for n in range(len(tokio)):
            if name==ProfileDICT["Hey! Say! JUMP"][n]["JName"]:
                birthday = ProfileDICT["Hey! Say! JUMP"][n]["Birth"]
    return birthday

def maxIndex(list): #找最大值的index
    index=[]
    maxOne=max(list)
    for i in range(len(list)):
        if list[i] == maxOne:
            index.append(i)
    return index

def minIndex(list): #找最小值的index
    index=[]
    minOne=min(list)
    for i in range(len(list)):
        if list[i] == minOne:
            index.append(i)
    return index

@client.event
async def on_ready():
    logging.info("[READY INFO] {} has connected to Discord!".format(client.user))
    print("[READY INFO] {} has connected to Discord!".format(client.user))


@client.event
async def on_message(message):
    if not re.search("<@[!&]{}> ?".format(client.user.id), message.content):    # 只有 @Bot 才會回應
        return

    if message.author == client.user:
        return

    # Greetings
    print("client.user.id =", client.user.id, "\nmessage.content =", message.content)
    msgSTR = re.sub("<@[!&]{}> ?".format(client.user.id), "", message.content)    # 收到 User 的訊息，將 id 取代成 ""
    logging.info(msgSTR)
    #print("msgSTR =", msgSTR)
    replySTR = ""    # Bot 回應訊息

    if msgSTR in ("","哈囉","嗨","嗨嗨","你好","您好","在嗎","早安","午安","晚安","こんにちは","こんばんは","やっほー","やっはろ","やほー","Hi","hi","hello","Hello","安安"):
        replySTR = "你好呀~有什麼可以為你服務的？\n我可以提供你Jstorm旗下藝人的基本資料喔！\n（各團成員、日英姓名、生日、年齡、血型、出身地）"
        await message.reply(replySTR)

    else:
        lokiResultDICT=getLokiResult(msgSTR)    # 取得 Loki 回傳結果
        print(lokiResultDICT)
        
        if client.user.id not in mscDICT:    # 判斷 User 是否為第一輪對話
            mscDICT[client.user.id] = {"group":"",
                                       "member":"",
                                       "request":"",
                                       "completed": False,
                                       "updatetime": datetime.datetime.now()
                                              }
            
        if len(lokiResultDICT.keys())==1:
            mscDICT[client.user.id]["member"] = ""
            mscDICT[client.user.id]["request"] = ""
        #多輪對話
        if lokiResultDICT:
            for k in lokiResultDICT.keys():    # 將 Loki Intent 的結果，存進 Global mscDICT 變數，可替換成 Database。
                if k == "Group":
                    mscDICT[client.user.id]["group"] = lokiResultDICT["Group"]
                elif k == "member":
                    mscDICT[client.user.id]["member"] = lokiResultDICT["member"]
                elif k == 'request':
                    mscDICT[client.user.id]["request"] = lokiResultDICT["request"]
        
        if len(lokiResultDICT.keys()) == 1 and lokiResultDICT.keys() == 'Group':
            mscDICT[client.user.id]['member']=""
            mscDICT[client.user.id]["request"]=""

        print("mscDICT =")
        pprint(mscDICT)
        
        if mscDICT[client.user.id]["request"] == "":  # 多輪對話的問句。
            replySTR = '請問你想問的是哪方面呢？（各團成員、日英姓名、生日、年齡、血型、出身地）'
        
        elif mscDICT[client.user.id]["group"] == "" and mscDICT[client.user.id]["member"] == "": 
            if mscDICT[client.user.id]["request"] in ("age","height","birth",'year','month','day'):
                replySTR = "請問您是問哪一個團體的哪位成員呢？"   
            elif mscDICT[client.user.id]["request"] in ("age.max","age.min","age.sort.HtoL","age.sort.LtoH","height.max","height.min","height.sort.HtoL","height.sort.LtoH"):
                replySTR = "請問您是問哪一個團體的呢？"
        
        elif mscDICT[client.user.id]["group"] == "":
            replySTR = "請問您是問哪一個團體呢？"
            
        else:  #給答案
            #Group
            if type(mscDICT[client.user.id]["group"])==list and mscDICT[client.user.id]["member"] =="":
                if type(mscDICT[client.user.id]["request"]) == int:
                    replySTR = '共有 '+str(mscDICT[client.user.id]["request"])+' 團。'
                    
    
                else:
                    answerSTR=""
                    for n in range(0,len(lokiResultDICT['Group'])):
                        answerSTR+=lokiResultDICT['Group'][n]+lokiResultDICT['request'][lokiResultDICT['Group'][n]]+'\n'
    
                    replySTR = "有以下團體：\n"+answerSTR
                    
            elif type(mscDICT[client.user.id]["group"])==str and mscDICT[client.user.id]["request"] in ('yes','no'):
                if mscDICT[client.user.id]["request"]=='yes':
                    replySTR = '沒錯，正是如此。'
                else: 
                    replySTR = mscDICT[client.user.id]["group"]+' 並不是Jstorm旗下的團體。'
            
            #member
            elif type(mscDICT[client.user.id]["member"])==list:
                if type(mscDICT[client.user.id]["request"])==list:
                    for e in mscDICT[client.user.id]["request"]:
                        if e in ("A型","B型","O型","AB型"):  #問各血型
                            answerSTR=""
                            for n in range(len(mscDICT[client.user.id]["member"])):
                                answerSTR+=lokiResultDICT['member'][n]+' 是 '+lokiResultDICT['request'][n]+'。\n'
                            replySTR = answerSTR
                            
                            
                        else:  #問整團成員
                            answerSTR=""
                            for n in range(len(mscDICT[client.user.id]["member"])):
                                answerSTR+=lokiResultDICT['member'][n]+lokiResultDICT['request'][n]+'\n'
                            replySTR = "有以下成員：\n"+answerSTR
                            
                    
                    
                else: #type(mscDICT[client.user.id]["request"])!=list   
                    if len(mscDICT[client.user.id]["request"])>2:#問特定出生地
                        answerSTR=""
                        for n in range(len(mscDICT[client.user.id]["member"])):
                            answerSTR+=lokiResultDICT['member'][n]+" "
                        replySTR =answerSTR+"來自 "+mscDICT[client.user.id]["request"]+"。"
                        
                    else: #問特定血型
                        answerSTR=""
                        for n in range(len(mscDICT[client.user.id]["member"])):
                            answerSTR+=lokiResultDICT['member'][n]+" "
                        replySTR =answerSTR+"是 "+mscDICT[client.user.id]["request"]+"。"
                        
                    
            
            elif type(mscDICT[client.user.id]["member"])==str:
                if mscDICT[client.user.id]["request"] == 'yes': #成員和團體有對上
                    replySTR='沒錯，正是如此。'
                          
                elif mscDICT[client.user.id]["request"] == 'no': #成員和團體沒對上
                    replySTR=f'不， {mscDICT[client.user.id]["member"]} 是 {mscDICT[client.user.id]["group"]} 的成員。'
                    
                 
                #name
                elif mscDICT[client.user.id]["request"] == 'yes.group': #有這個人
                    replySTR=f'有的， {mscDICT[client.user.id]["member"]} 是 {mscDICT[client.user.id]["group"]} 的成員。'
                    
                elif mscDICT[client.user.id]["request"] == 'no.group': #沒這個人
                    replySTR=f'{mscDICT[client.user.id]["member"]} 不是Jstorm旗下的人。'
                    
                    
                elif  mscDICT[client.user.id]["request"] in ("JName","EName","JLname","JFname","ELname","EFname"):
                    for n in range(len(ProfileDICT[mscDICT[client.user.id]["group"]])):
                        if ProfileDICT[mscDICT[client.user.id]["group"]][n]['JName']==mscDICT[client.user.id]["member"]:
                            index=n
                    if mscDICT[client.user.id]["request"] == "JName":
                        replySTR= mscDICT[client.user.id]['member']
                        
                    if mscDICT[client.user.id]["request"] == "EName":
                        replySTR=ProfileDICT[mscDICT[client.user.id]["group"]][index]['EName']
                        
                    if mscDICT[client.user.id]["request"] == "JLname":
                        replySTR=ProfileDICT[mscDICT[client.user.id]["group"]][index]['JLname']
                        
                    if mscDICT[client.user.id]["request"] == "JFname":
                        replySTR=ProfileDICT[mscDICT[client.user.id]["group"]][index]['JFname']
                        
                    if mscDICT[client.user.id]["request"] == "EFname":
                        replySTR=ProfileDICT[mscDICT[client.user.id]["group"]][index]['EFname']
                        
                    if mscDICT[client.user.id]["request"] == "ELname":
                        replySTR=ProfileDICT[mscDICT[client.user.id]["group"]][index]['ELname']
                        
                
                #age
                elif mscDICT[client.user.id]["request"] in ("age","age.max","age.min","age.sort.HtoL","age.sort.LtoH"):
                    ageLIST=[]
                    for n in range(len(ProfileDICT[mscDICT[client.user.id]["group"]])) :
                        ageLIST.append(findAge(ProfileDICT[mscDICT[client.user.id]["group"]][n]['JName']))
                        
                    if mscDICT[client.user.id]["request"] == 'age': #回報歲數
                        replySTR=str(findAge(mscDICT[client.user.id]["member"]))+"歲"
                        
                        
                    elif mscDICT[client.user.id]["request"] == 'age.max': #回報最年長
                        indexLIST=maxIndex(ageLIST)
                        if len(indexLIST) != 1:  #如果很多人同歲比較生日
                            birthLIST=[]
                            for i in indexLIST:
                                birthLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][i]['Birth'])
                            index=birthLIST.index(min(birthLIST))
                            replySTR="是 "+ProfileDICT[mscDICT[client.user.id]["group"]][indexLIST[index]]['JName']+f" ，他 {ageLIST[indexLIST[index]]} 歲。"
                            
                        else: #len(indexLIST) == 1
                            index=ageLIST.index(max(ageLIST))
                            replySTR="是 "+ProfileDICT[mscDICT[client.user.id]["group"]][index]['JName']+f" ，他 {ageLIST[index]} 歲。"
                            
                            
                            
                    elif mscDICT[client.user.id]["request"] == 'age.min': #回報最年幼
                        indexLIST=minIndex(ageLIST)
                        if len(indexLIST) != 1: #如果很多人同歲比較生日
                            birthLIST=[]
                            for i in indexLIST:
                                birthLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][i]['Birth'])
                            index=birthLIST.index(max(birthLIST))
                            replySTR="是 "+ProfileDICT[mscDICT[client.user.id]["group"]][indexLIST[index]]['JName']+f" ，他 {ageLIST[indexLIST[index]]} 歲。"
                            
                        else: #len(indexLIST) == 1
                            index=ageLIST.index(min(ageLIST))
                            replySTR="是 "+ProfileDICT[mscDICT[client.user.id]["group"]][index]['JName']+f" ，他 {ageLIST[index]} 歲。"
                            
                            
                    elif mscDICT[client.user.id]["request"] == 'age.sort.HtoL': #年齡從大排到小
                        groupLIST=ageDICT[mscDICT[client.user.id]["group"]]
                        answerSTR=""
                        for n in range(len(groupLIST)):
                            answerSTR+=groupLIST[n]+' ， '+str(findAge(groupLIST[n]))+' 歲。\n'
                        replySTR='年齡從大排到小為：\n'+answerSTR
                        
    
                    elif mscDICT[client.user.id]["request"] == 'age.sort.LtoH':  #年齡從小排到大
                        ageDICT[mscDICT[client.user.id]["group"]].reverse()
                        groupLIST=ageDICT[mscDICT[client.user.id]["group"]]
                        answerSTR=""
                        for n in range(len(groupLIST)):
                            answerSTR+=groupLIST[n]+' ， '+str(findAge(groupLIST[n]))+' 歲。\n'
                        replySTR='年齡從小排到大為：\n'+answerSTR
                        
                        
                        
                elif mscDICT[client.user.id]["request"] in ("year","month","day"): #問年月日
                    birthday=findBirthday(mscDICT[client.user.id]["member"])
                
                    if mscDICT[client.user.id]["request"] == 'year':
                        replySTR='他是 '+birthday[0]+'年出生的。'
                        
                    elif mscDICT[client.user.id]["request"] == 'month':
                        replySTR='他是 '+birthday[1]+'月出生的。'
                        
                    elif mscDICT[client.user.id]["request"] == 'day':
                        replySTR='他是 '+birthday[2]+'日出生的。'
                        
                        
                       
                elif mscDICT[client.user.id]["request"] in ("height.max","height.min","height.sort.HtoL","height.sort.LtoH"):
                    heightLIST=[]
                    for n in range(len(ProfileDICT[mscDICT[client.user.id]["group"]])):
                        heightLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][n]['height'])
                        
                    if mscDICT[client.user.id]["request"] =="height": #身高
                        replySTR= mscDICT[client.user.id]["member"]+"，他 "+str(findHeight(mscDICT[client.user.id]["member"]))+" cm。"
                        
                    
                    
                    if mscDICT[client.user.id]["request"] =="height.max":  #最高
                        indexLIST=maxIndex(heightLIST)
                        answerSTR=""
                        for n in indexLIST:
                            answerSTR += ProfileDICT[mscDICT[client.user.id]["group"]][n]["JName"]+"，他 "+ str(heightLIST[n])+ "cm。\n"
                        replySTR = answerSTR
                        
                        
                    elif mscDICT[client.user.id]["request"] =="height.min":  #最矮
                        indexLIST=minIndex(heightLIST)
                        answerSTR=""
                        for n in indexLIST:
                            answerSTR+=ProfileDICT[mscDICT[client.user.id]["group"]][n]["JName"]+"，他 "+str(heightLIST[n])+ "cm。\n"
                        replySTR =answerSTR
                        
    
                    elif mscDICT[client.user.id]["request"] =="height.sort.LtoH":  #矮到高
                        sortedLIST=sorted(heightLIST)
                        indexLIST=[]
                        for n in range(len(heightLIST)):
                            indexLIST.append(heightLIST.index(sortedLIST[n]))
                        lostIndex=[]
                        for n in range(min(indexLIST),max(indexLIST)):
                            if n not in indexLIST:
                                lostIndex.append(n)
                        for e in indexLIST:
                            if indexLIST.count(e)>1:
                                for l in lostIndex:
                                  indexLIST[indexLIST.index(e)]= l
                        answerSTR=""
                        for n in indexLIST:
                            answerSTR += ProfileDICT[mscDICT[client.user.id]["group"]][n]['JName']+"，"+str(ProfileDICT[mscDICT[client.user.id]["group"]][n]['height'])+"cm\n"
                        replySTR = "身高從矮到高是：\n"+answerSTR
                        
                        
                    elif mscDICT[client.user.id]["request"] =="height.sort.HtoL":  #高到矮
                        sortedLIST=sorted(heightLIST)
                        sortedLIST.reverse()
                        indexLIST=[]
                        for n in range(len(heightLIST)):
                            indexLIST.append(heightLIST.index(sortedLIST[n]))
                        lostIndex=[]
                        for n in range(min(indexLIST),max(indexLIST)):
                            if n not in indexLIST:
                                lostIndex.append(n)
                        for e in indexLIST:
                            if indexLIST.count(e)>1:
                                for l in lostIndex:
                                  indexLIST[indexLIST.index(e)]= l
                        answerSTR=""
                        for n in indexLIST:
                            answerSTR += ProfileDICT[mscDICT[client.user.id]["group"]][n]['JName']+"，"+str(ProfileDICT[mscDICT[client.user.id]["group"]][n]['height'])+"cm\n"
                        replySTR = "身高從高到矮是：\n"+answerSTR
                        
                       
                elif mscDICT[client.user.id]["request"].encode('UTF-8').isalnum() == True: #request是身高
                    replySTR= mscDICT[client.user.id]["member"]+"，他 "+str(findHeight(mscDICT[client.user.id]["member"]))+" cm。"
                    
                
                elif mscDICT[client.user.id]["request"].encode('UTF-8').isalpha() == False: 
    
                    if len(mscDICT[client.user.id]["request"]) == 2 :#request 為血型
                        if mscDICT[client.user.id]["member"] == 'no': #沒有是該血型的人
                            replySTR=mscDICT[client.user.id]["group"]+" 中沒有寫血型是 "+mscDICT[client.user.id]["request"]+" 的成員。"
                            
                        elif mscDICT[client.user.id]["request"].isdigit() == True: #距離生日的天數是兩位數
                            replySTR="離 "+mscDICT[client.user.id]["member"]+" 的生日還有 "+mscDICT[client.user.id]["request"]+" 天。"
                            
                        else: #回報血型
                            replySTR="他是 "+mscDICT[client.user.id]["request"]+" 。"
                            
                    
                    elif 2< len(mscDICT[client.user.id]["request"]) <5 : #request是地名
                        if mscDICT[client.user.id]["member"] == 'no': #沒有來自該地的人
                            replySTR=mscDICT[client.user.id]["group"]+" 中沒有來自 "+mscDICT[client.user.id]["request"]+" 的成員。"
                            
                        elif mscDICT[client.user.id]["request"].isdigit() == True: #距離生日的天數是三位數
                            replySTR="離 "+mscDICT[client.user.id]["member"]+" 的生日還有 "+mscDICT[client.user.id]["request"]+" 天。"
                            
                        else: #回報地名
                            replySTR="他來自 "+mscDICT[client.user.id]["request"]+" 。"
                            
                            
                    else: #request是生日
                        if mscDICT[client.user.id]["request"].isdigit(): #距離生日的天數是個位數
                            replySTR="離 "+mscDICT[client.user.id]["member"]+" 的生日還有 "+mscDICT[client.user.id]["request"]+" 天。"
                            
                        else: #request是生日
                            replySTR="他的生日是 "+mscDICT[client.user.id]["request"]+" 。"
                            
                    
            elif type(mscDICT[client.user.id]["request"]) == list:  #回報多個問題
                for e in mscDICT[client.user.id]["request"]:
                    if e in ("age.max","age.min"):
                        ageLIST=[]
                        for n in range(len(ProfileDICT[mscDICT[client.user.id]["group"]])) :
                            ageLIST.append(findAge(ProfileDICT[mscDICT[client.user.id]["group"]][n]['JName']))
                        if e == 'age.max': #回報最年長
                            maxLIST=[]
                            indexLIST=maxIndex(ageLIST)
                            if len(indexLIST) != 1:  #如果很多人同歲比較生日
                                birthLIST=[]
                                for i in indexLIST:
                                    birthLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][i]['Birth'])
                                index=birthLIST.index(min(birthLIST))
                                maxLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][indexLIST[index]]['JName'])
                                maxLIST.append(ageLIST[indexLIST[index]])
                            else: #len(indexLIST) == 1
                                index=ageLIST.index(max(ageLIST))
                                maxLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][index]['JName'])
                                maxLIST.append(str(ageLIST[index]))
                        if e == 'age.max': #回報最年長
                            minLIST=[]
                            indexLIST=minIndex(ageLIST)
                            if len(indexLIST) != 1:  #如果很多人同歲比較生日
                                birthLIST=[]
                                for i in indexLIST:
                                    birthLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][i]['Birth'])
                                index=birthLIST.index(max(birthLIST))
                                minLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][indexLIST[index]]['JName'])
                                minLIST.append(ageLIST[indexLIST[index]])
                            else: #len(indexLIST) == 1
                                index=ageLIST.index(min(ageLIST))
                                minLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][index]['JName'])
                                minLIST.append(str(ageLIST[index]))
                        print(maxLIST)
                        print(minLIST)
                        replySTR=f'最年長是 {maxLIST[0]}，{maxLIST[1]} 歲。\n最年幼是 {minLIST[0]}，{minLIST[1]} 歲。'
                        
       
        if msgSTR in ("謝謝","我問完了","掰掰","88","bye","byebye","再見","再會"):
            replySTR = "感謝你的使用，期待再次相見~"
            mscDICT[client.user.id]["completed"]=True

        if mscDICT[client.user.id]["completed"]:    # 清空 User Dict
            del mscDICT[client.user.id]
        
        print(replySTR)
        
        if replySTR:    # 回應 User 訊息
            await message.reply(replySTR)
        return




if __name__ == "__main__":
    client.run(accountDICT["discord_token"])

    #getLokiResult("")
