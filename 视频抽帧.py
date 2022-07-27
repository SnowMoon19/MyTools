import cv2
import os

dir = r"C:\Users\Administrator\Documents\WeChat Files\wxid_q4300fnfjw3721\FileStorage\Video\2022-03"

count = 0
name = 0

for eachVid in os.listdir(dir):
    vPath = dir + "\\" + eachVid  # 多个视频
    vidcap = cv2.VideoCapture(vPath)
    success, image = vidcap.read()
    while success:
        # 每60帧抽一次
        if count % 60 == 0:
            name+=1
            cv2.imwrite(
                f'C:\\Users\\Administrator\\Documents\\WeChat '
                f'Files\\wxid_q4300fnfjw3721\\FileStorage\\Video\\2022-03\\pic\\{name}.jpg',
                image)  # save frame as JPEG file
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1
