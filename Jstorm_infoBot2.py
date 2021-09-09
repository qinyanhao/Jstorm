#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
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

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Loki Result => {}".format(resultDICT))
    return resultDICT


@client.event
async def on_ready():
    logging.info("[READY INFO] {} has connected to Discord!".format(client.user))
    print("[READY INFO] {} has connected to Discord!".format(client.user))


@client.event
async def on_message(message):
    if message.channel.name != "bot_test":
        return

    if not re.search("<@[!&]{}> ?".format(client.user.id), message.content):    # 只有 @Bot 才會回應
        return

    if message.author == client.user:
        return
    
    # Greetings
    try:
        print("client.user.id =", client.user.id, "\nmessage.content =", message.content)
        msgSTR = re.sub("<@[!&]{}> ?".format(client.user.id), "", message.content)    # 收到 User 的訊息，將 id 取代成 ""
        logging.info(msgSTR)
        #print("msgSTR =", msgSTR)
        replySTR = ""    # Bot 回應訊息

        if msgSTR in ["哈囉","嗨","嗨嗨","你好","您好","在嗎","早安","午安","晚安","こんにちは","こんばんは","やっほー","やっはろ","やほー","Hi","hi","hello","Hello","安安"]:
            replySTR = "你好呀~有什麼可以為你服務的？\n我可以提供你Jstorm旗下藝人的基本資料喔！\n（各團成員、日英姓名、生日、年齡、血型、出身地）"
            await message.reply(replySTR)
            return

        lokiResultDICT=getLokiResult(msgSTR)    # 取得 Loki 回傳結果
    
    
        # 多輪對話
        if lokiResultDICT:
            if client.user.id not in mscDICT:    # 判斷 User 是否為第一輪對話
                mscDICT[client.user.id] = {"Group":"",
                                           "member":"",
                                           "request":"",
                                           "completed": False
                                           } 
            
            for k in lokiResultDICT.keys():    # 將 Loki Intent 的結果，存進 Global mscDICT 變數，可替換成 Database。
                if k == "Group":
                    mscDICT[client.user.id]["Group"] = lokiResultDICT["Group"]
                elif k == "member":
                    mscDICT[client.user.id]["member"] = lokiResultDICT["member"]
                elif k == 'request':
                    mscDICT[client.user.id]["request"] = lokiResultDICT["request"]
                # elif k == "msg":
                #     replySTR = lokiResultDICT[k]
                #     if mscDICT[client.user.id]["request"] == {} :
                #         replySTR += "\n請問你想問什麼呢？"
                #     print("Loki msg:", replySTR, "\n")
                    
            if mscDICT[client.user.id]["Group"] == "" and replySTR == "":    # 多輪對話的問句。
                replySTR = "請問您是問哪一個團體呢？"
            elif mscDICT[client.user.id]["member"] == "" and replySTR == "":
                replySTR = "請問您是問哪一個成員呢？"
            
            if mscDICT[client.user.id]['request']=='yes':
                replySTR='沒錯，正是如此'
            
            result=''
            for e in mscDICT[client.user.id].values():
                if e !="":
                    result+='y'
                else:
                    result+='n'
                
            if result == 'yyyy':
                replySTR=f"是 {mscDICT[client.user.id]['request']['Group']}的{mscDICT[client.user.id]['request']['member']}"
                mscDICT[client.user.id]["completed"] = True
                    
        print("mscDICT =")
        pprint(mscDICT)

        if mscDICT[client.user.id]["completed"]:    # 清空 User Dict
            del mscDICT[client.user.id]

        if replySTR:    # 回應 User 訊息
            await message.reply(replySTR)
        return

    except Exception as e:
        logging.error("[MSG ERROR] {}".format(str(e)))
        print("[MSG ERROR] {}".format(str(e)))




if __name__ == "__main__":
    client.run(accountDICT["discord_token"])

    #getLokiResult("")
    