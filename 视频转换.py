import os
import time

import cv2


def video_rename(file_path,save_path):
    for video_name in os.listdir(file_path):
        new_name = video_name.split('.')[0] + '.h264'
        os.rename(os.path.join(file_path,video_name),os.path.join(save_path,new_name))
    print("视频格式转换完成，dav 转 h264 !!")

# 视频转换 mp4
def video2mp4(video_name,save_name,save_fps = 25,video_w = 1920,video_h=1080):
    if video_name.split('.')[-1] == 'mp4':
        return -1
    cap = cv2.VideoCapture(video_name)
    tmp_video_mp4 =  cv2.VideoWriter(save_name, cv2.VideoWriter_fourcc('M','P','E','G'), save_fps, (video_w,video_h))
    start_time = time.time()
    while True:
        success, origin_img = cap.read()
        if not success or len(origin_img) < 2:
            break
        tmp_video_mp4.write(cv2.resize(origin_img,(video_w,video_h)))
    end_time = time.time()
    tmp_video_mp4.release()
    print("video {} change done! spand time = {}".format(save_name,end_time - start_time))


if __name__ == '__main__':
    origin = "C:/Users/Administrator/Downloads/cc"
    aim = "C:/Users/Administrator/Downloads/cc"
    video_rename(origin, aim)
    video2mp4(aim+'/cc.h264', aim+'/cc.mp4')