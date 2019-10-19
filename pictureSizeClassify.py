# -*-coding:utf-8-*-
import os, shutil
import re
from PIL import Image
#path = "E:\\picture"
path = input("请输入文件夹路径：")
n_Path = os.path.join(path, '0000')
w_Path = os.path.join(path, '1920')
h_Path = os.path.join(path, '1080')
x_Path = os.path.join(path, 'xxxx')
if not os.path.exists(n_Path):
    print('创建(0000)文件夹')
    os.makedirs(n_Path)
    print('创建成功')
else:
    print('(0000)文件夹已存在')
if not os.path.exists(w_Path):
    print('创建(1920)文件夹')
    os.makedirs(w_Path)
    print('创建成功')
else:
    print('(1920)文件夹已存在')
if not os.path.exists(h_Path):
    print('创建(1080)文件夹')
    os.makedirs(h_Path)
    print('创建成功')
else:
    print('(1080)文件夹已存在')
if not os.path.exists(x_Path):
    print('创建(xxxx)文件夹')
    os.makedirs(x_Path)
    print('创建成功')
else:
    print('(xxxx)文件夹已存在')
imgList = os.listdir(path)
print("开始分类。。。")
for a in imgList:
    if not re.search(r'[\s\S]*-[\s\S]*\.([jJ][pP][gG]|[pP][nN][gG])', a):
        continue
    imgFullPath = os.path.join(path, a)
    img = Image.open(imgFullPath)
    img.close()
    size = img.size
    if ((size[0] == 1920) and (size[1] >= 1080)) or ((size[0] >= 1920) and (size[1] == 1080)):
        movePath = n_Path
        b = '0000'
        #print(str(size[0]) + '   ' + str(size[1]))
    elif (size[0]/size[1]) >= (1920/1080):
        movePath = h_Path
        b = '1080'
    elif (size[0]/size[1]) < (1920/1080):
        movePath = w_Path
        b = '1920'
    else:
        movePath = x_Path
        b = 'xxxx'
    i = 0
    [a1, a2] = os.path.splitext(a)
    while(True):
        if os.path.exists(os.path.join(movePath, a)):
            if os.path.exists(os.path.join(movePath, a1 + '..........' + str(i) + a2)):
                i = i + 1
                print(i)
                continue
            else:
                shutil.move(imgFullPath, os.path.join(movePath, a1 + '..........' + str(i) + a2))
                print(a + "已被重名为：......" + str(i) + "；并被分入：" + b)
                break
        else:
            shutil.move(imgFullPath, movePath)
            print(a + "已被分入：" + b)
            break
print('分类成功')






