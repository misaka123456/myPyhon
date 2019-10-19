import re
import os, shutil
import random

#pathSource = "D:\\mikasa\\OneDrive\\动漫壁纸"
f = open('pathSource.txt', 'r', encoding='utf-8')
pathSource = f.read()
f.close()
pathAim = "F:\\图片视频\\桌面壁纸"
if os.path.exists(pathAim):
    shutil.rmtree(pathAim)
    print("已删除")
os.makedirs(pathAim)
imgSourceList = os.listdir(pathSource)
imgAimList = random.sample(imgSourceList, 100)
i = 0
for a in imgAimList:
    shutil.copy(os.path.join(pathSource, a), pathAim)






