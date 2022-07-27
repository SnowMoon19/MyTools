# encoding=utf-8
import os
import shutil


rootdir=r"C:\Users\Administrator\Desktop\pic\xiang"
filelist=os.listdir(rootdir)

def objFileName():
    fileNameList = r"C:\Users\Administrator\Desktop\dir.txt"
    objNameList = []
    for i in open(fileNameList, 'r'):
        objNameList.append(i.replace('\n', ''))
    return objNameList

# 文件复制
def copyImg():
    sourcePath = r'C:\Users\Administrator\Desktop\fsdownload\pics_5_19'
    # 指定图片原始路径A
    targetPath = r'C:\Users\Administrator\Desktop\za'
    # 指定图片存放目录B
    for i in objFileName():
        objName = i
        shutil.copy(sourcePath + '/' + objName, targetPath + '/浙' + objName)
        # 删除被复制的文件
        os.remove(sourcePath + '/' + objName)



if __name__ == '__main__':
    copyImg()



