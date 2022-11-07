import kfbReader
import cv2 as cv

def ReadInfo(self, kfbPath, scale=0, readAll=False):
    return kfbReader._kfbReader.reader_ReadInfo(self, kfbPath, scale, readAll)

path = r'G:\论文\数据集\neg_0\T2019_13.kfb'
scale = 20
# 实例化Reader类
read = kfbReader.reader()
read.ReadInfo(path, scale, False)

roi = read.ReadRoi(10240, 10240, 512, 512, scale)
cv.imshow('roi', roi)
cv.waitKey(0)