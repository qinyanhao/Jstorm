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
        
        if client.user.id not in mscDICT:    # 判斷 User 是否為第一輪對話
            mscDICT[client.user.id] = {"group":"",
                                       "member":"",
                                       "request":"",
                                       "completed": False,
                                       "updatetime": datetime.datetime.now()
                                               }
        #多輪對話
        if lokiResultDICT:
            for k in lokiResultDICT.keys():    # 將 Loki Intent 的結果，存進 Global mscDICT 變數，可替換成 Database。
                if k == "Group":
                    mscDICT[client.user.id]["group"] = lokiResultDICT["Group"]
                elif k == "member":
                    mscDICT[client.user.id]["member"] = lokiResultDICT["member"]
                elif k == 'request':
                    mscDICT[client.user.id]["request"] = lokiResultDICT["request"]
                # elif k == "msg":
                #     replySTR = lokiResultDICT[k]
                #     if mscDICT[client.user.id]["request"] == "":
                #         replySTR += "\n請問你想問什麼呢？"
                #     print("Loki msg:", replySTR, "\n")

        print("mscDICT =")
        pprint(mscDICT)
        
        if mscDICT[client.user.id]["request"] == "":  # 多輪對話的問句。
            replySTR = '請問你想問的是哪方面呢？（各團成員、日英姓名、生日、年齡、血型、出身地）'

        elif mscDICT[client.user.id]["group"] == "" and mscDICT[client.user.id]["member"] == "":    
            replySTR = "請問您是問哪一個團體呢？"
            # elif mscDICT[client.user.id]["member"] == "" and mscDICT[client.user.id]["group"] in ('TOKIO','嵐','KAT-TUN','Hey! Say! JUMP'):
            #     replySTR = "請問您是問哪一個成員呢？"


        #給答案
        #Group
        if type(mscDICT[client.user.id]["group"])==list and mscDICT[client.user.id]["member"] =="":
            if type(mscDICT[client.user.id]["request"]) == int:
                replySTR = '共有 '+str(mscDICT[client.user.id]["request"])+' 團。'
                mscDICT[client.user.id]["completed"]=True

            else:
                answerSTR=""
                for n in range(0,len(lokiResultDICT['Group'])):
                    answerSTR+=lokiResultDICT['Group'][n]+lokiResultDICT['request'][lokiResultDICT['Group'][n]]+'\n'

                replySTR = "有以下團體：\n"+answerSTR
                mscDICT[client.user.id]["completed"]=True
        if type(mscDICT[client.user.id]["group"])==str and mscDICT[client.user.id]["request"] in ('yes','no'):
            if mscDICT[client.user.id]["request"]=='yes':
                replySTR = '沒錯，正是如此。'
            else: 
                replySTR = mscDICT[client.user.id]["group"]+' 並不是Jstorm旗下的團體。'
        
        #member
        if type(mscDICT[client.user.id]["member"])==list:
            answerSTR=""
            for n in range(len(mscDICT[client.user.id]["member"])):
                answerSTR+=lokiResultDICT['member'][n]+lokiResultDICT['request'][n]+'\n'
    
            replySTR = "有以下成員：\n"+answerSTR
            mscDICT[client.user.id]["completed"]=True
        
        if type(mscDICT[client.user.id]["member"])==str:
            if mscDICT[client.user.id]["request"] == 'yes': #成員和團體有對上
                replySTR='沒錯，正是如此。'
                mscDICT[client.user.id]["completed"]=True      
            elif mscDICT[client.user.id]["request"] == 'no': #成員和團體沒對上
                replySTR=f'不， {mscDICT[client.user.id]["member"]} 是 {mscDICT[client.user.id]["group"]} 的成員。'
                mscDICT[client.user.id]["completed"]=True
             
            #name
            elif mscDICT[client.user.id]["request"] == 'yes.group': #有這個人
                replySTR=f'有的， {mscDICT[client.user.id]["member"]} 是 {mscDICT[client.user.id]["group"]} 的成員。'
                mscDICT[client.user.id]["completed"]=True
            elif mscDICT[client.user.id]["request"] == 'no.group': #沒這個人
                replySTR=f'{mscDICT[client.user.id]["member"]} 不是Jstorm旗下的人。'
                mscDICT[client.user.id]["completed"]=True
                
            elif  mscDICT[client.user.id]["request"] in ("JName","EName","JLname","JFname","ELname","EFname"):
                for n in range(len(ProfileDICT[mscDICT[client.user.id]["group"]])):
                    if ProfileDICT[mscDICT[client.user.id]["group"]][n]['JName']==mscDICT[client.user.id]["member"]:
                        index=n
                if mscDICT[client.user.id]["request"] == "JName":
                    replySTR= mscDICT[client.user.id]['member']
                    mscDICT[client.user.id]["completed"]=True
                if mscDICT[client.user.id]["request"] == "EName":
                    replySTR=ProfileDICT[mscDICT[client.user.id]["group"]][index]['EName']
                    mscDICT[client.user.id]["completed"]=True
                if mscDICT[client.user.id]["request"] == "JLname":
                    replySTR=ProfileDICT[mscDICT[client.user.id]["group"]][index]['JLname']
                    mscDICT[client.user.id]["completed"]=True
                if mscDICT[client.user.id]["request"] == "JFname":
                    replySTR=ProfileDICT[mscDICT[client.user.id]["group"]][index]['JFname']
                    mscDICT[client.user.id]["completed"]=True
                if mscDICT[client.user.id]["request"] == "EFname":
                    replySTR=ProfileDICT[mscDICT[client.user.id]["group"]][index]['EFname']
                    mscDICT[client.user.id]["completed"]=True
                if mscDICT[client.user.id]["request"] == "ELname":
                    replySTR=ProfileDICT[mscDICT[client.user.id]["group"]][index]['ELname']
                    mscDICT[client.user.id]["completed"]=True
            
                #age
            elif mscDICT[client.user.id]["request"] in ("age","age.max","age.min","age.sort.HtoL","age.sort.LtoH"):
                ageLIST=[]
                for n in range(len(ProfileDICT[mscDICT[client.user.id]["group"]])) :
                    ageLIST.append(findAge(ProfileDICT[mscDICT[client.user.id]["group"]][n]['JName']))
                    
                if mscDICT[client.user.id]["request"] == 'age': #回報歲數
                    replySTR=str(findAge(mscDICT[client.user.id]["member"]))+"歲"
                    mscDICT[client.user.id]["completed"]=True
                    
                if mscDICT[client.user.id]["request"] == 'age.max': #回報最年長
                    indexLIST=maxIndex(ageLIST)
                    if len(indexLIST) != 1:  #如果很多人同歲比較生日
                        birthLIST=[]
                        for i in indexLIST:
                            birthLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][i]['Birth'])
                        index=birthLIST.index(min(birthLIST))
                        replySTR="是 "+ProfileDICT[mscDICT[client.user.id]["group"]][indexLIST[index]]['JName']+f" ，他 {ageLIST[indexLIST[index]]} 歲。"
                        mscDICT[client.user.id]["completed"]=True
                    else: #len(indexLIST) == 1
                        index=ageLIST.index(max(ageLIST))
                        replySTR="是 "+ProfileDICT[mscDICT[client.user.id]["group"]][index]['JName']+f" ，他 {ageLIST[index]} 歲。"
                        mscDICT[client.user.id]["completed"]=True
                        
                        
                if mscDICT[client.user.id]["request"] == 'age.min': #回報最年幼
                    indexLIST=minIndex(ageLIST)
                    if len(indexLIST) != 1: #如果很多人同歲比較生日
                        birthLIST=[]
                        for i in indexLIST:
                            birthLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][i]['Birth'])
                        index=birthLIST.index(max(birthLIST))
                        replySTR="是 "+ProfileDICT[mscDICT[client.user.id]["group"]][indexLIST[index]]['JName']+f" ，他 {ageLIST[indexLIST[index]]} 歲。"
                        mscDICT[client.user.id]["completed"]=True
                    else: #len(indexLIST) == 1
                        index=ageLIST.index(min(ageLIST))
                        replySTR="是 "+ProfileDICT[mscDICT[client.user.id]["group"]][index]['JName']+f" ，他 {ageLIST[index]} 歲。"
                        mscDICT[client.user.id]["completed"]=True
                        
                if mscDICT[client.user.id]["request"] == 'age.sort.HtoL':
                    
        
        
        
        
       
                

        if mscDICT[client.user.id]["completed"]:    # 清空 User Dict
            del mscDICT[client.user.id]
        
        print(replySTR)
        
        if replySTR:    # 回應 User 訊息
            await message.reply(replySTR)
        return




if __name__ == "__main__":
    client.run(accountDICT["discord_token"])

    #getLokiResult("")
