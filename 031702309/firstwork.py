#coding=utf-8
import json
import string
import re
import cpca
import pandas as pd
import numpy as np
def en_json(ob):              #编码为JSON类型
    result = json.dumps(ob,ensure_ascii=False)
    print(result)

d = {"姓名": '',
     "手机": '',
     "地址":[ '','','','','']
     }
ob = input("请输入：")
ob = ob.split(",")            #分割名字
d["姓名"] = ob[0]
ob = ob[1]  
l = len(ob)
ob = ob.split(".")
ob = ob[0]                    #地址+手机号的混合
num = re.findall(r"\d+",ob)   #提取手机号
i=0
while 1 :
    if i >= len(num) :
        break
    elif len(num[i]) == 11 :
        break
    else:
        i = i+1
d["手机"] = num[i]
ob = re.sub(d["手机"],"",ob)   #纯地址
ob = ob.split()
ob = cpca.transform(ob)
address = np.array(ob)
address = address[0]
i=0
while 1:
    d["地址"][i] = address[i]
    i = i +1
    if i >=3 :
        break
if d["地址"][0][2] == "市" :
    d["地址"][0] = d["地址"][0][:2]
address = address[3]           #查找第四级
i = 0
while 1:
    if address[i]=="镇":
        d["地址"][3] = address[:(i+1)]
        d["地址"][4] = address[(i+1):]
        break
    elif address[i]=="乡":
        d["地址"][3] = address[:(i+1)]
        d["地址"][4] = address[(i+1):]
        break
    elif address[i]=="街" and address[i+1]=="道" :
        d["地址"][3] = address[:(i+2)]
        d["地址"][4] = address[(i+2):]
        break
    elif i>=(len(address)-1) :
        d["地址"][4] = address
        break
    else :
        i = i+1


print(en_json(d))


