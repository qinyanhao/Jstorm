#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
from pprint import pprint

from Jstorm import runLoki,countBirth,findAge

logging.basicConfig(level=logging.INFO) 

# <取得多輪對話資訊>
client = discord.Client()

questionTemplate ={"group":"",
                 "member": "",
                 "question": "",}

mscDICT = {# "userID": {questionTemplate}
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

        if msgSTR in ["哈囉","嗨","你好","您好","在嗎"]:
            replySTR = "你好呀~有什麼可以為你服務的？\n我可以提供你Jstorm旗下藝人的基本資料喔！\n（各團成員、日英姓名、生日、年齡、血型、出身地）"
            await message.reply(replySTR)
            return

        lokiResultDICT=getLokiResult(msgSTR)    # 取得 Loki 回傳結果
    
    
        # 多輪對話
        if lokiResultDICT:
            if client.user.id not in mscDICT:    # 判斷 User 是否為第一輪對話
                mscDICT[client.user.id] = {"question":{},
                                           "completed": False
                                           } 

            

                    
            
            for k in lokiResultDICT.keys():    # 將 Loki Intent 的結果，存進 Global mscDICT 變數，可替換成 Database。
                if k == "bodypart":
                    mscDICT[client.user.id]["bodypart"] = lokiResultDICT["bodypart"]
                if k == "request":
                    mscDICT[client.user.id]["request"] = lokiResultDICT["request"]
                if k == "confirm":
                    mscDICT[client.user.id]["confirm"] = lokiResultDICT["confirm"]
                if k == "msg":
                    replySTR = lokiResultDICT[k]
                #else:
                    #replySTR = "你是要詢問療程相關的事情嗎？"
                    
    except Exception as e:
        logging.error("[MSG lokiResultDICT ERROR] {}".format(str(e)))


    # bot回覆
    try:
        if lokiResultDICT:
            # input == "我想要除腿的毛"
            # 第一輪和多輪的回覆
            if mscDICT[client.user.id]["request"] == True and mscDICT[client.user.id]["bodypart"] != "":
                if mscDICT[client.user.id]["confirm"] == "" and mscDICT[client.user.id]["bodyQuestionSTR"] != "":
                    replySTR = "OK啊，我就幫您安排{}的除毛療程囉，好不好？".format(mscDICT[client.user.id]["bodypart"])
                    mscDICT[client.user.id]["queryIntentSTR"] = "confirm"

                elif mscDICT[client.user.id]["confirm"] == "" and mscDICT[client.user.id]["bodyQuestionSTR"] == "":
                    if mscDICT[client.user.id]["bodypart"] == "腿":
                        replySTR = "請問是大腿還是小腿呢？"
                        mscDICT[client.user.id]["queryIntentSTR"] = "bodypart"
                        mscDICT[client.user.id]["bodyQuestionSTR"] = replySTR
                        
                    elif mscDICT[client.user.id]["bodypart"] == "手臂":
                        replySTR = "請問是上手臂還是下手臂呢？"
                        mscDICT[client.user.id]["queryIntentSTR"] = "bodypart"
                        mscDICT[client.user.id]["bodyQuestionSTR"] = replySTR
                        
                    elif mscDICT[client.user.id]["bodypart"] == "手":
                        replySTR = "請問是手指、手背還是全手呢？"
                        mscDICT[client.user.id]["queryIntentSTR"] = "bodypart"
                        mscDICT[client.user.id]["bodyQuestionSTR"] = replySTR
                        
                    elif mscDICT[client.user.id]["bodypart"] == "脖子" or mscDICT[client.user.id]["bodypart"] == "頸部":
                        replySTR = "請問是前頸還是後頸呢？"
                        mscDICT[client.user.id]["queryIntentSTR"] = "bodypart"
                        mscDICT[client.user.id]["bodyQuestionSTR"] = replySTR
                    else:
                        replySTR = "沒問題呀，我就幫您安排{}的除毛療程囉，好不好？".format(mscDICT[client.user.id]["bodypart"])
                        mscDICT[client.user.id]["queryIntentSTR"] = "confirm"

                    
                    
            # #############################################################################
            
            # input == "我腿毛好長"
            # 第一輪的回覆
            elif mscDICT[client.user.id]["request"] == "" and mscDICT[client.user.id]["bodypart"] != "":
                if mscDICT[client.user.id]["confirm"] == "" and mscDICT[client.user.id]["bodyQuestionSTR"] == "":  
                    if mscDICT[client.user.id]["bodypart"] != "毛":
                        if mscDICT[client.user.id]["bodypart"] == "腿":   
                            replySTR = "大腿還是小腿呢？"
                            mscDICT[client.user.id]["queryIntentSTR"] = "bodypart"
                            mscDICT[client.user.id]["bodyQuestionSTR"] = replySTR
                            
                        elif "手臂" in mscDICT[client.user.id]["bodypart"]:
                            replySTR = "上手臂還是下手臂呢？"
                            mscDICT[client.user.id]["queryIntentSTR"] = "bodypart"
                            mscDICT[client.user.id]["bodyQuestionSTR"] = replySTR
    
                        elif "手" in mscDICT[client.user.id]["bodypart"]:
                            replySTR = "手指、手背還是全手呢？"
                            mscDICT[client.user.id]["queryIntentSTR"] = "bodypart"
                            mscDICT[client.user.id]["bodyQuestionSTR"] = replySTR
                            
                        elif "脖子" in mscDICT[client.user.id]["bodypart"] or "頸部" in mscDICT[client.user.id]["bodypart"]:
                            replySTR = "前頸還是後頸呢？"
                            mscDICT[client.user.id]["queryIntentSTR"] = "bodypart"
                            mscDICT[client.user.id]["bodyQuestionSTR"] = replySTR
                            
                        else:
                            replySTR = "那我就幫您安排{}的除毛療程囉，好嗎？".format(mscDICT[client.user.id]["bodypart"])
                            mscDICT[client.user.id]["queryIntentSTR"] = "confirm"                    


            # #############################################################################
        
            # input == "我想除毛" 
            # 第一輪的回覆
            elif mscDICT[client.user.id]["request"] == True and mscDICT[client.user.id]["bodypart"] == "":
                if mscDICT[client.user.id]["confirm"] == "" and mscDICT[client.user.id]["bodyQuestionSTR"] == "":  
                    replySTR = "請問想處理哪個部位呢？"
                    mscDICT[client.user.id]["queryIntentSTR"] = "bodypart"
                    mscDICT[client.user.id]["bodyQuestionSTR"] = replySTR
                
            else:
                replySTR = "？？？"
                                 
    except Exception as e:
        logging.error("[MSG scene3 ERROR] {}".format(str(e)))


    #print("mscDICT =")
    pprint(mscDICT)

    #if mscDICT[client.user.id]["completed"]:    # 清空 User Dict
        #del mscDICT[client.user.id]

    if replySTR:    # 回應 User 訊息
        await message.reply(replySTR)
    return

    #except Exception as e:
        #logging.error("[MSG ERROR] {}".format(str(e)))
        #print("[MSG ERROR] {}".format(str(e)))


if __name__ == "__main__":
    client.run(accountDICT["discord_token"])

    #print(beautiBot("我腿毛好長"))
    
    #臉可以嗎
    #想除腿毛
    