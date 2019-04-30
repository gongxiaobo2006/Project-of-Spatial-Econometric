# -*- coding: utf-8 -*-

#调用高德开放平台API
import urllib.request  
from urllib import parse  
import json  
from openpyxl import load_workbook  
import numpy as np  
dict = {}  
nameList = []  
distanceList = []  
name = load_workbook('dongguan.xlsx')  
nameSheet = name["data"]  
for row in range(2,35):  
    nameList.append(str(nameSheet["A%d"%(row)].value))  
k = len(nameList)  
for i in nameList:  
    url1 = 'http://restapi.amap.com/v3/place/text?keywords='+i+'&city=东莞&output=json&offset=1&page=1&extensions=all'  
    #省略秘钥  
    newUrl1 = parse.quote(url1, safe="/:=&?#+!$,;'@()*[]")  
    response1 = urllib.request.urlopen(newUrl1)  
    data1 = response1.read()  
    jsonData1 = json.loads(data1)  
    dict[i] = jsonData1['pois'][0]['location']  
    locations = dict[i].split(",")  
for m in range(k):  
    subList = []  
    for n in range(k):  
        origin = dict[nameList[m]]  
        destination = dict[nameList[n]]  
        url2 = 'https://restapi.amap.com/v3/distance?origins='+origin+'&destination='+destination+'&type=1&output=json'  
        #省略秘钥  
        newUrl2 = parse.quote(url2, safe="/:=&?#+!$,;'@()*[]")  
        response2 = urllib.request.urlopen(newUrl2)  
        data2 = response2.read()  
        jsonData2 = json.loads(data2)  
        distance = jsonData2['results'][0]['distance']  
        subList.append(int(distance))  
        print(nameList[m],nameList[n],distance)  
    distanceList.append(subList)  
for u in range(k):  
    for v in range(u,k):  
        m = min(distanceList[u][v],distanceList[v][u])  
        distanceList[v][u],distanceList[u][v] = m,m  
distanceArray = np.array(distanceList)  
np.save('distance.npy')