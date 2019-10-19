# -*-coding:utf-8-*-
import os, shutil
import re
import time
from PIL import Image

path = input("请输入文件夹路径：")

imgList = os.listdir(path)
print("开始分类。。。")

for a in imgList:
    if not re.search(r'[\s\S]*-[\s\S]*-[\s\S]*\.([jJ][pP][gG])', a):
        continue
    imgName = a.split('-')[0]
    if not os.path.exists(os.path.join(path, imgName)):
        os.mkdir(os.path.join(path, imgName))
    shutil.move(os.path.join(path, a), os.path.join(path, imgName))
    print(a + "被分入：" + imgName)






