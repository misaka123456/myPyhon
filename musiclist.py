# -*-coding:utf-8-*-
import os, shutil
import re
import eyed3
import json

fileListPath = "F:\\workspace\\test01\\qqmusic\\mymusic"
fileList = os.listdir(fileListPath)

# 命名方式  歌曲-歌手.mp3
musicList = []
i = 0
for m in fileList:
    if m == "musiclist.json":
        continue
    fileName = os.path.splitext(m)
    if fileName[1] == '.jpg':
        continue
    # filePath = os.path.join(fileListPath, m)
    if fileName[1] == '.mp3':
        i = i + 1
        musicPath = os.path.join(fileListPath, m)
        musicName = fileName[0].split(' - ')
        # print(musicName)
        jsonTemp = {}
        jsonTemp["name"] = musicName[0]
        jsonTemp["singer"] = musicName[1]
        musicPathTemp = os.path.join(fileListPath, str(i)+'.mp3')
        os.rename(musicPath, musicPathTemp)
        musicTime = eyed3.load(musicPathTemp).info.time_secs
        album = eyed3.load(musicPathTemp).tag.album
        jsonTemp["album"] = album
        second = musicTime % 60
        minute = musicTime // 60
        secondStr = ''
        minuteStr = ''
        if second == 0:
            secondStr = '00'
        elif second <= 9:
            secondStr = '0' + str(second)
        else:
            secondStr = str(second)
        if minute <= 9:
            minuteStr = '0' + str(minute)
        else:
            minuteStr = str(minute)
        # print(minuteStr, secondStr)
        # print(str(minute), str(second))
        jsonTemp["time"] = minuteStr + ':' + secondStr
        # print(jsonTemp["time"])
        os.rename(musicPathTemp, musicPath)
        jsonTemp["link_url"] = "./mymusic/" + m
        jsonTemp["cover"] = "./mymusic/" + fileName[0] + '.jpg'
        musicList.append(jsonTemp)
        print(jsonTemp)
        # if i == 5:
        #     break
# print(musicList)

with open("F:\\workspace\\test01\\qqmusic\\mymusic\\musiclist.json", 'w') as file:
    json.dump(musicList, file)




