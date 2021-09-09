#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Profile_name

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
with open('D:\HAO\Hao的研所\實習\Jstorm\ProfileDICT.json', 'r') as f:
    ProfileDICT=json.load(f)

DEBUG_Profile_name = True
userDefinedDICT = {"age": ["年長", "年幼"], "嵐": ["嵐", "ARASHI", "Arashi", "ARS", "Ars"], "TOKIO": ["TOKIO", "東京小子", "T團"], "Jstorm": ["Jstorm", "J strom", "jstorm", "j storm", "JS", "js"], "KAT-TUN": ["KAT-TUN", "KATTUN", "KT"], "城島茂": ["隊長", "城島茂", "城島", "茂", "茂茂"], "大野智": ["大野智", "隊長", "リーダー", "智智", "阿智", "野智", "大野", "智ちゃん", "智哥", "智くん"], "松本潤": ["松本潤", "松本", "潤", "J", "MJ", "潤潤", "弟弟", "潤監督", "總監", "潤總監", "阿潤", "潤ちゃん", "潤くん"], "櫻井翔": ["櫻井翔", "櫻井", "翔", "翔翔", "阿翔", "翔哥", "翔ちゃん", "翔くん"], "薮宏太": ["薮宏太", "薮", "宏太", "薮ちゃん", "薮くん", "薮さん", "やぶ", "阿薮", "薮先生", "薮帝王", "帝王", "やぶぶ"], "上田竜也": ["上田竜也", "上田", "竜也", "上田龍也", "龍也", "老大", "吳愛達", "阿龍", "龍龍"], "中丸雄一": ["中丸雄一", "中丸", "雄一", "丸子"], "中島裕翔": ["中島裕翔", "中島", "裕翔", "yuto", "瘋兔子", "島哥", "副隊長", "yutti", "ゆってぃ"], "亀梨和也": ["亀梨和也", "亀梨", "和也", "龜梨", "龜梨和也", "龜龜", "亀亀", "卡咩", "Kame", "kame"], "二宮和也": ["二宮和也", "二宮", "和也", "NINO", "尼尼", "和總", "尼諾米", "NINOMI", "NINOちゃん"], "伊野尾慧": ["伊野尾慧", "伊野尾", "慧", "慧慧", "伊野尾ちゃん", "蘑菇", "阿慧", "慧哥", "慧老師"], "八乙女光": ["八乙女光", "八乙女", "光", "hika", "HIKA", "ひかる", "ひか", "やおちゃん", "阿光", "光光", "小光", "仙女", "小仙女"], "国分太一": ["國分", "太一", "國分太一", "国分太一", "国分"], "山田涼介": ["山田涼介", "山田", "涼介", "小涼", "小甜", "阿涼", "團霸", "yama"], "有岡大貴": ["有岡大貴", "有岡", "大貴", "阿貴", "貴貴", "大醬", "大ちゃん"], "松岡昌宏": ["松岡昌宏", "松岡", "昌宏", "松兄"], "相葉雅紀": ["相葉雅紀", "相葉", "雅紀", "愛拔", "大兔子", "相葉ちゃん"], "知念侑李": ["知念侑李", "知念", "侑李", "念念", "阿念", "小惡魔", "小野智", "Chi", "ちぃ", "ちっちゃん", "ねんち", "ちぃー", "知念くん", "知念ちゃん"], "髙木雄也": ["高木雄也", "髙木雄也", "雄也", "高木", "髙木", "yuya", "大雄", "大熊", "海", "ゆうちゃん", "髙木くん", "高木くん"], "Hey! Say! JUMP": ["Hey! Say! JUMP", "平成跳", "hsj", "HSJ", "JUMP", "跳跳", "醬噗"]}

nicknameLIST=userDefinedDICT['城島茂']+userDefinedDICT['国分太一']+userDefinedDICT['松岡昌宏']+userDefinedDICT['大野智']+userDefinedDICT['松本潤']+userDefinedDICT['櫻井翔']+userDefinedDICT['二宮和也']+userDefinedDICT['相葉雅紀']+userDefinedDICT['上田竜也']+userDefinedDICT['中丸雄一']+userDefinedDICT['亀梨和也']+userDefinedDICT['薮宏太']+userDefinedDICT['八乙女光']+userDefinedDICT['伊野尾慧']+userDefinedDICT['山田涼介']+userDefinedDICT['有岡大貴']+userDefinedDICT['中島裕翔']+userDefinedDICT['知念侑李']+userDefinedDICT['髙木雄也']
groupLIST=userDefinedDICT['KAT-TUN']+userDefinedDICT['TOKIO']+userDefinedDICT['嵐']+userDefinedDICT['Hey! Say! JUMP']

tokio=['城島茂','国分太一','松岡昌宏']
arashi=['大野智','櫻井翔','相葉雅紀','二宮和也','松本潤']
kattun=['上田竜也','中丸雄一','亀梨和也']
jump=['薮宏太','八乙女光','髙木雄也','伊野尾慧','有岡大貴','中島裕翔','山田涼介','知念侑李']

eng=['英文','英語','英語姓名','英文姓氏','英語姓氏','英文姓名']
jan=['日文','日語','日語姓名','日文姓氏','日語姓氏','日文姓名']
Fname=['名字','名']
Lname=['姓氏','姓']

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Profile_name:
        print("[Profile_name] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    if utterance == "[尼尼]的[英文][名字]":
        if args[0] in nicknameLIST:
            if args[1] in eng:
                for k in userDefinedDICT.keys():
                    if args[0] in userDefinedDICT[k]:
                        key=k
                
                if key in tokio:
                    for n in range(len(tokio)):
                        if key in ProfileDICT['TOKIO'][n]['JName']:
                            resultDICT['Group']='TOKIO'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['TOKIO'][n]['EName']
                if key in arashi:
                    for n in range(len(arashi)):
                        if key in ProfileDICT['嵐'][n]['JName']:
                            resultDICT['Group']='嵐'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['嵐'][n]['EName']
                if key in kattun:
                    for n in range(len(kattun)):
                        if key in ProfileDICT['KAT-TUN'][n]['JName']:
                            resultDICT['Group']='KAT-TUN'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['KAT-TUN'][n]['EName']
                if key in jump:
                    for n in range(len(jump)):
                        if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                            resultDICT['Group']='Hey! Say! JUMP'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['EName']
                            
            if args[1] in jan:
                for k in userDefinedDICT.keys():
                    if args[0] in userDefinedDICT[k]:
                        key=k
                
                if key in tokio:
                    for n in range(len(tokio)):
                        if key in ProfileDICT['TOKIO'][n]['JName']:
                            resultDICT['Group']='TOKIO'
                            resultDICT['member']=key
                            resultDICT['request']=key
                if key in arashi:
                    for n in range(len(arashi)):
                        if key in ProfileDICT['嵐'][n]['JName']:
                            resultDICT['Group']='嵐'
                            resultDICT['member']=key
                            resultDICT['request']=key
                if key in kattun:
                    for n in range(len(kattun)):
                        if key in ProfileDICT['KAT-TUN'][n]['JName']:
                            resultDICT['Group']='KAT-TUN'
                            resultDICT['member']=key
                            resultDICT['request']=key
                if key in jump:
                    for n in range(len(jump)):
                        if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                            resultDICT['Group']='Hey! Say! JUMP'
                            resultDICT['member']=key
                            resultDICT['request']=key

    if utterance == "[潤潤]本名是什麼":
        if args[0] in nicknameLIST:
            for k in userDefinedDICT.keys():
                    if args[0] in userDefinedDICT[k]:
                        key=k
                
            if key in tokio:
                for n in range(len(tokio)):
                    if key in ProfileDICT['TOKIO'][n]['JName']:
                        resultDICT['Group']='TOKIO'
                        resultDICT['member']=key
                        resultDICT['request']=key
            if key in arashi:
                for n in range(len(arashi)):
                    if key in ProfileDICT['嵐'][n]['JName']:
                        resultDICT['Group']='嵐'
                        resultDICT['member']=key
                        resultDICT['request']=key
            if key in kattun:
                for n in range(len(kattun)):
                    if key in ProfileDICT['KAT-TUN'][n]['JName']:
                        resultDICT['Group']='KAT-TUN'
                        resultDICT['member']=key
                        resultDICT['request']=key
            if key in jump:
                for n in range(len(jump)):
                    if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                        resultDICT['Group']='Hey! Say! JUMP'
                        resultDICT['member']=key
                        resultDICT['request']=key

    if utterance == "[翔翔]的[日語姓名]":
         if args[0] in nicknameLIST:
             if args[1] in jan:
                if args[0] in nicknameLIST:
                    for k in userDefinedDICT.keys():
                        if args[0] in userDefinedDICT[k]:
                            key=k
                        
                    if key in tokio:
                        for n in range(len(tokio)):
                            if key in ProfileDICT['TOKIO'][n]['JName']:
                                resultDICT['Group']='TOKIO'
                                resultDICT['member']=key
                                resultDICT['request']=key
                    if key in arashi:
                        for n in range(len(arashi)):
                            if key in ProfileDICT['嵐'][n]['JName']:
                                resultDICT['Group']='嵐'
                                resultDICT['member']=key
                                resultDICT['request']=key
                    if key in kattun:
                        for n in range(len(kattun)):
                            if key in ProfileDICT['KAT-TUN'][n]['JName']:
                                resultDICT['Group']='KAT-TUN'
                                resultDICT['member']=key
                                resultDICT['request']=key
                    if key in jump:
                        for n in range(len(jump)):
                            if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                                resultDICT['Group']='Hey! Say! JUMP'
                                resultDICT['member']=key
                                resultDICT['request']=key
             if args[1] in eng:
                if args[0] in nicknameLIST:
                    for k in userDefinedDICT.keys():
                        if args[0] in userDefinedDICT[k]:
                            key=k
                
                    if key in tokio:
                        for n in range(len(tokio)):
                            if key in ProfileDICT['TOKIO'][n]['JName']:
                                resultDICT['Group']='TOKIO'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['TOKIO'][n]['EName']
                    if key in arashi:
                        for n in range(len(arashi)):
                            if key in ProfileDICT['嵐'][n]['JName']:
                                resultDICT['Group']='嵐'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['嵐'][n]['EName']
                    if key in kattun:
                        for n in range(len(kattun)):
                            if key in ProfileDICT['KAT-TUN'][n]['JName']:
                                resultDICT['Group']='KAT-TUN'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['KAT-TUN'][n]['EName']
                    if key in jump:
                        for n in range(len(jump)):
                            if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                                resultDICT['Group']='Hey! Say! JUMP'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['EName']
        
            

    if utterance == "[阿慧][全名]是什麼":
        if args[0] in nicknameLIST:
            for k in userDefinedDICT.keys():
                    if args[0] in userDefinedDICT[k]:
                        key=k
                
            if key in tokio:
                for n in range(len(tokio)):
                    if key in ProfileDICT['TOKIO'][n]['JName']:
                        resultDICT['Group']='TOKIO'
                        resultDICT['member']=key
                        resultDICT['request']=key
            if key in arashi:
                for n in range(len(arashi)):
                    if key in ProfileDICT['嵐'][n]['JName']:
                        resultDICT['Group']='嵐'
                        resultDICT['member']=key
                        resultDICT['request']=key
            if key in kattun:
                for n in range(len(kattun)):
                    if key in ProfileDICT['KAT-TUN'][n]['JName']:
                        resultDICT['Group']='KAT-TUN'
                        resultDICT['member']=key
                        resultDICT['request']=key
            if key in jump:
                for n in range(len(jump)):
                    if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                        resultDICT['Group']='Hey! Say! JUMP'
                        resultDICT['member']=key
                        resultDICT['request']=key

    if utterance == "[雅紀]的[英文][名字]是什麼":
        if args[0] in nicknameLIST:
            if args[1] in eng:
                if args[2] in Lname:
                    for k in userDefinedDICT.keys():
                        if args[0] in userDefinedDICT[k]:
                            key=k
                    
                    if key in tokio:
                        for n in range(len(tokio)):
                            if key in ProfileDICT['TOKIO'][n]['JName']:
                                resultDICT['Group']='TOKIO'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['TOKIO'][n]['ELname']
                    if key in arashi:
                        for n in range(len(arashi)):
                            if key in ProfileDICT['嵐'][n]['JName']:
                                resultDICT['Group']='嵐'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['嵐'][n]['ELname']
                    if key in kattun:
                        for n in range(len(kattun)):
                            if key in ProfileDICT['KAT-TUN'][n]['JName']:
                                resultDICT['Group']='KAT-TUN'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['KAT-TUN'][n]['ELname']
                    if key in jump:
                        for n in range(len(jump)):
                            if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                                resultDICT['Group']='Hey! Say! JUMP'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['ELname']
                    
                    
                if args[2] in Fname:
                    for k in userDefinedDICT.keys():
                        if args[0] in userDefinedDICT[k]:
                            key=k
                    
                    if key in tokio:
                        for n in range(len(tokio)):
                            if key in ProfileDICT['TOKIO'][n]['JName']:
                                resultDICT['Group']='TOKIO'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['TOKIO'][n]['EFname']
                    if key in arashi:
                        for n in range(len(arashi)):
                            if key in ProfileDICT['嵐'][n]['JName']:
                                resultDICT['Group']='嵐'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['嵐'][n]['EFname']
                    if key in kattun:
                        for n in range(len(kattun)):
                            if key in ProfileDICT['KAT-TUN'][n]['JName']:
                                resultDICT['Group']='KAT-TUN'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['KAT-TUN'][n]['EFname']
                    if key in jump:
                        for n in range(len(jump)):
                            if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                                resultDICT['Group']='Hey! Say! JUMP'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['EFname']
            if args[1] in jan:
                if args[2] in Lname:
                    for k in userDefinedDICT.keys():
                        if args[0] in userDefinedDICT[k]:
                            key=k
                    
                    if key in tokio:
                        for n in range(len(tokio)):
                            if key in ProfileDICT['TOKIO'][n]['JName']:
                                resultDICT['Group']='TOKIO'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['TOKIO'][n]['JLname']
                    if key in arashi:
                        for n in range(len(arashi)):
                            if key in ProfileDICT['嵐'][n]['JName']:
                                resultDICT['Group']='嵐'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['嵐'][n]['JLname']
                    if key in kattun:
                        for n in range(len(kattun)):
                            if key in ProfileDICT['KAT-TUN'][n]['JName']:
                                resultDICT['Group']='KAT-TUN'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['KAT-TUN'][n]['JLname']
                    if key in jump:
                        for n in range(len(jump)):
                            if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                                resultDICT['Group']='Hey! Say! JUMP'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['JLname']
                    
                    
                if args[2] in Fname:
                    for k in userDefinedDICT.keys():
                        if args[0] in userDefinedDICT[k]:
                            key=k
                    
                    if key in tokio:
                        for n in range(len(tokio)):
                            if key in ProfileDICT['TOKIO'][n]['JName']:
                                resultDICT['Group']='TOKIO'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['TOKIO'][n]['JFname']
                    if key in arashi:
                        for n in range(len(arashi)):
                            if key in ProfileDICT['嵐'][n]['JName']:
                                resultDICT['Group']='嵐'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['嵐'][n]['JFname']
                    if key in kattun:
                        for n in range(len(kattun)):
                            if key in ProfileDICT['KAT-TUN'][n]['JName']:
                                resultDICT['Group']='KAT-TUN'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['KAT-TUN'][n]['JFname']
                    if key in jump:
                        for n in range(len(jump)):
                            if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                                resultDICT['Group']='Hey! Say! JUMP'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['JFname']

    if utterance == "有人叫[知念]嗎":
        if args[0] in nicknameLIST:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    name=k
            
            if name in tokio:
                resultDICT['Group']='TOKIO'
                resultDICT['member']=name
                resultDICT['request']='yes.group'
            elif name in arashi:
                resultDICT['Group']='嵐'
                resultDICT['member']=name
                resultDICT['request']='yes.group'
            elif name in kattun:
                resultDICT['Group']='KAT-TUN'
                resultDICT['member']=name
                resultDICT['request']='yes.group'
            elif name in jump:
                resultDICT['Group']='Hey! Say! JUMP'
                resultDICT['member']=name
                resultDICT['request']='yes.group'
            else:
                resultDICT['request']='no'
                    
                    
    if utterance == "[大貴][姓]什麼":
        if args[0] in nicknameLIST:
            for k in userDefinedDICT.keys():
                if args[0] in userDefinedDICT[k]:
                    key=k
            if args[1] in Lname:
                if key in tokio:
                    for n in range(len(tokio)):
                        if key in ProfileDICT['TOKIO'][n]['JName']:
                            resultDICT['Group']='TOKIO'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['TOKIO'][n]['JLname']
                if key in arashi:
                    for n in range(len(arashi)):
                        if key in ProfileDICT['嵐'][n]['JName']:
                            resultDICT['Group']='嵐'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['嵐'][n]['JLname']
                if key in kattun:
                    for n in range(len(kattun)):
                       if key in ProfileDICT['KAT-TUN'][n]['JName']:
                            resultDICT['Group']='KAT-TUN'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['KAT-TUN'][n]['JLname']
                if key in jump:
                    for n in range(len(jump)):
                        if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                            resultDICT['Group']='Hey! Say! JUMP'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['JLname']
            
            if args[1] in Fname:
                if key in tokio:
                    for n in range(len(tokio)):
                        if key in ProfileDICT['TOKIO'][n]['JName']:
                            resultDICT['Group']='TOKIO'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['TOKIO'][n]['JFname']
                if key in arashi:
                    for n in range(len(arashi)):
                        if key in ProfileDICT['嵐'][n]['JName']:
                            resultDICT['Group']='嵐'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['嵐'][n]['JFname']
                if key in kattun:
                    for n in range(len(kattun)):
                       if key in ProfileDICT['KAT-TUN'][n]['JName']:
                            resultDICT['Group']='KAT-TUN'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['KAT-TUN'][n]['JFname']
                if key in jump:
                    for n in range(len(jump)):
                        if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                            resultDICT['Group']='Hey! Say! JUMP'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['JFname']

    if utterance == "[涼介]的[英文]名字是什麼":
        if args[0] in nicknameLIST:
            if args[1] in eng:
                for k in userDefinedDICT.keys():
                    if args[0] in userDefinedDICT[k]:
                        key=k
                
                if key in tokio:
                    for n in range(len(tokio)):
                        if key in ProfileDICT['TOKIO'][n]['JName']:
                            resultDICT['Group']='TOKIO'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['TOKIO'][n]['EName']
                if key in arashi:
                    for n in range(len(arashi)):
                        if key in ProfileDICT['嵐'][n]['JName']:
                            resultDICT['Group']='嵐'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['嵐'][n]['EName']
                if key in kattun:
                    for n in range(len(kattun)):
                        if key in ProfileDICT['KAT-TUN'][n]['JName']:
                            resultDICT['Group']='KAT-TUN'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['KAT-TUN'][n]['EName']
                if key in jump:
                    for n in range(len(jump)):
                        if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                            resultDICT['Group']='Hey! Say! JUMP'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['EName']
                            
            if args[1] in jan:
                for k in userDefinedDICT.keys():
                    if args[0] in userDefinedDICT[k]:
                        key=k
                
                if key in tokio:
                    for n in range(len(tokio)):
                        if key in ProfileDICT['TOKIO'][n]['JName']:
                            resultDICT['Group']='TOKIO'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['TOKIO'][n]['JName']
                if key in arashi:
                    for n in range(len(arashi)):
                        if key in ProfileDICT['嵐'][n]['JName']:
                            resultDICT['Group']='嵐'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['嵐'][n]['JName']
                if key in kattun:
                    for n in range(len(kattun)):
                        if key in ProfileDICT['KAT-TUN'][n]['JName']:
                            resultDICT['Group']='KAT-TUN'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['KAT-TUN'][n]['JName']
                if key in jump:
                    for n in range(len(jump)):
                        if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                            resultDICT['Group']='Hey! Say! JUMP'
                            resultDICT['member']=key
                            resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['JName']

    if utterance == "[雄也]的[英文姓氏]是什麼":
        if args[0] in nicknameLIST:
            if args[1] in eng:
                if args[1][-2:] in Lname:
                    for k in userDefinedDICT.keys():
                        if args[0] in userDefinedDICT[k]:
                            key=k
                    
                    if key in tokio:
                        for n in range(len(tokio)):
                            if key in ProfileDICT['TOKIO'][n]['JName']:
                                resultDICT['Group']='TOKIO'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['TOKIO'][n]['ELname']
                    if key in arashi:
                        for n in range(len(arashi)):
                            if key in ProfileDICT['嵐'][n]['JName']:
                                resultDICT['Group']='嵐'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['嵐'][n]['ELname']
                    if key in kattun:
                        for n in range(len(kattun)):
                            if key in ProfileDICT['KAT-TUN'][n]['JName']:
                                resultDICT['Group']='KAT-TUN'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['KAT-TUN'][n]['ELname']
                    if key in jump:
                        for n in range(len(jump)):
                            if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                                resultDICT['Group']='Hey! Say! JUMP'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['ELname']
                    
                    
                if args[1][-2:] in Fname:
                    for k in userDefinedDICT.keys():
                        if args[0] in userDefinedDICT[k]:
                            key=k
                    
                    if key in tokio:
                        for n in range(len(tokio)):
                            if key in ProfileDICT['TOKIO'][n]['JName']:
                                resultDICT['Group']='TOKIO'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['TOKIO'][n]['EFname']
                    if key in arashi:
                        for n in range(len(arashi)):
                            if key in ProfileDICT['嵐'][n]['JName']:
                                resultDICT['Group']='嵐'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['嵐'][n]['EFname']
                    if key in kattun:
                        for n in range(len(kattun)):
                            if key in ProfileDICT['KAT-TUN'][n]['JName']:
                                resultDICT['Group']='KAT-TUN'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['KAT-TUN'][n]['EFname']
                    if key in jump:
                        for n in range(len(jump)):
                            if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                                resultDICT['Group']='Hey! Say! JUMP'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['EFname']
            if args[1] in jan:
                if args[1][-2:] in Lname:
                    for k in userDefinedDICT.keys():
                        if args[0] in userDefinedDICT[k]:
                            key=k
                    
                    if key in tokio:
                        for n in range(len(tokio)):
                            if key in ProfileDICT['TOKIO'][n]['JName']:
                                resultDICT['Group']='TOKIO'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['TOKIO'][n]['JLname']
                    if key in arashi:
                        for n in range(len(arashi)):
                            if key in ProfileDICT['嵐'][n]['JName']:
                                resultDICT['Group']='嵐'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['嵐'][n]['JLname']
                    if key in kattun:
                        for n in range(len(kattun)):
                            if key in ProfileDICT['KAT-TUN'][n]['JName']:
                                resultDICT['Group']='KAT-TUN'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['KAT-TUN'][n]['JLname']
                    if key in jump:
                        for n in range(len(jump)):
                            if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                                resultDICT['Group']='Hey! Say! JUMP'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['JLname']
                    
                    
                if args[1][-2:] in Fname:
                    for k in userDefinedDICT.keys():
                        if args[0] in userDefinedDICT[k]:
                            key=k
                    
                    if key in tokio:
                        for n in range(len(tokio)):
                            if key in ProfileDICT['TOKIO'][n]['JName']:
                                resultDICT['Group']='TOKIO'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['TOKIO'][n]['JFname']
                    if key in arashi:
                        for n in range(len(arashi)):
                            if key in ProfileDICT['嵐'][n]['JName']:
                                resultDICT['Group']='嵐'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['嵐'][n]['JFname']
                    if key in kattun:
                        for n in range(len(kattun)):
                            if key in ProfileDICT['KAT-TUN'][n]['JName']:
                                resultDICT['Group']='KAT-TUN'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['KAT-TUN'][n]['JFname']
                    if key in jump:
                        for n in range(len(jump)):
                            if key in ProfileDICT['Hey! Say! JUMP'][n]['JName']:
                                resultDICT['Group']='Hey! Say! JUMP'
                                resultDICT['member']=key
                                resultDICT['request']=ProfileDICT['Hey! Say! JUMP'][n]['JFname']


    return resultDICT