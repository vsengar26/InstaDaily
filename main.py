# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:30:59 2020

@author: vseng
"""

import argparse
import instaloader
import json
import os
from os import system,name
from textblob import TextBlob
import demoji
import pickle
import playsound
import itertools
from PIL import Image
demoji.download_codes()


       
def clear(): 
    if name == 'nt': 
        _ = system('cls')



def sentimentComment(corpus):
    res=TextBlob(corpus)
    sent=res.sentiment.polarity
    return sent



def downloadContent(keyword,count,postLikeThresh,is_fast=True):
    L = instaloader.Instaloader(download_videos=False,save_metadata=False,compress_json=False,download_comments=True,download_geotags=False)
    L.login(userName, userPassword)
    L.download_hashtag(keyword,max_count=count,fast_update=is_fast,post_filter=lambda post: post.likes>postLikeThresh,profile_pic=False)
    clear()
    print("Fetching complete.")
    listOfImages=[]
    for filename in os.listdir(path+"/#"+keyword):
        if filename.endswith(".json"):
            f=open(path+"/#{}/".format(keyword)+filename,)
            data=json.load(f)
            count=0
            tot=0
            likesOnPost=int(data[0]['post_like_count'])
            for i in range(len(data)):
                corpus1=demoji.replace(data[i]['text'],"")
                corpus=" ".join(filter(lambda x:x[0]!='@', corpus1.split()))
                if len(corpus)>0:
                    tot+=1
                    val=sentimentComment(corpus)
                    if val>0:
                        count+=1
            listOfImages.append((filename[:-14],likesOnPost*round(((count/tot)*100),2)))
            f.close()
            
    rankedList=sorted(listOfImages,key = lambda x: x[1],reverse=True)
    return(rankedList)

parser=argparse.ArgumentParser()
parser.add_argument("-t","--hashtag",help="The hashtag you want to retrieve without '#' or any colons",required=True,type=str)
parser.add_argument("-n","--count", help="Maximumm number of results you want to view (default is 5)",default=5,type=int)
args = parser.parse_args()
count=args.count
keyword=args.hashtag
path=os.getcwd()
os.chdir(path)

file1 = open('details.txt', 'r') 
Lines = file1.readlines() 
userDetails=[]
tempCount=0
for line in Lines: 
    detail=line.strip()
    userDetails.append(detail[detail.index(':')+2:])
    tempCount+=1
    if tempCount==2:
        break
file1.close()

userName=str(userDetails[0])
userPassword=str(userDetails[1])


postLikeThresh=500
countOverAll=0
clear()
print("\n\n\n\n\n\t\t\tFetching {} Results with hashtag: #{}".format(count,keyword))
rankedList=downloadContent(keyword, count, postLikeThresh)


while countOverAll<count:
    
    
    dest=path+("/#{}/".format(keyword))
    
    try:
        dbfile = open(path+'/Records/record_'+keyword, 'rb')
        records1=[]
        while 1:
            try:
                records1.append(pickle.load(dbfile))
            except EOFError:
                break
            
        records=list(itertools.chain.from_iterable(records1))
        dbfile.close()
        countShown=0

        for i in range(len(rankedList)):

            if rankedList[i][0] not in records:
                countShown+=1
                try:
                    im=Image.open(dest+rankedList[i][0]+".jpg")
                    im.show()
                    im.close()    
                    countOverAll+=1

                except FileNotFoundError as e1:
                    ext=1
                    while True:
                        try:
                            im=Image.open(dest+rankedList[i][0]+"_"+str(ext)+".jpg")
                            im.show()
                            im.close()
                            countOverAll+=1
                            ext+=1
                            
                        except FileNotFoundError as e2:
                            break
                        
            
            if(countOverAll>=count):
                dbfile=open(path+'/Records/record_'+keyword,'ab')
                pickle.dump([item[0] for item in rankedList[:countShown]],dbfile)
                dbfile.close()
                break
            
            
            
    except FileNotFoundError as e:
        countShown=0

        for i in range(len(rankedList)):
            countShown+=1
            try:
                im=Image.open(dest+rankedList[i][0]+".jpg")
                im.show()
                im.close()
                countOverAll+=1

            except FileNotFoundError as e1:
                ext=1
                #print("6")
                while True:
                    try:
                        im=Image.open(dest+rankedList[i][0]+"_"+str(ext)+".jpg")
                        im.show()
                        im.close()
                        countOverAll+=1
                        ext+=1

                    except FileNotFoundError as e2:
                        #print("8")
                        break
            if(countOverAll>=count):
                dbfile=open(path+'/Records/record_'+keyword,'ab')
                pickle.dump([item[0] for item in rankedList[:countShown]],dbfile)
                dbfile.close()
                break


        
    else:
        
        if countOverAll==0:
            playsound.playsound("Alerts/zeroRes.mp3",True)
            clear()
            print("\n\n\n\n\t\t\t Fetching New Results")
            rankedList=downloadContent(keyword, count+10, postLikeThresh-50,False)
            continue
            
        elif countOverAll<count:
            playsound.playsound("Alerts/exiting.mp3",True)
            dbfile=open(path+'/Records/record_'+keyword,'ab')
            pickle.dump([item[0] for item in rankedList],dbfile)
            dbfile.close()
            clear()
            print("To re run: \n\n\t1- Press the up arrow key and it will return the previously used command on the console. \n\n\t2- Press enter to re run the same command. \n")
            print("Thanks for cooperation.Hope you understand.Hope you stay healthy.")
            break
        
        else:
            break
        
    
    
print("\n\n\n\t\t\t\tThank You For Using The Program.")
