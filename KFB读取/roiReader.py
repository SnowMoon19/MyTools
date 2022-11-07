import os

from Kfbreader_win10_python36 import kfbReader as kr
import cv2
import numpy as np
import json

scale = 20


file1 = r"G:\paper\dataset\neg_0\T2019_13.kfb"  # kfb文件
label1 = r"G:\paper\dataset\labels\T2019_4.json"  # 对应文件的标签数据

reader = kr.reader()
kr.reader.ReadInfo(reader, file1, scale, True)  # 读取图片，scale为放大倍数


def get_roi(label):
    with  open(label, "r") as f:
        js = json.load(f)  # 解析json对象
    rois = []
    roi = {}
    for dic in js:
        # 类别是roi的对象将其保存到rois列表中，并初始化poses属性
        if dic["class"] == "roi":
            roi = dic
            roi["poses"] = []
            rois.append(roi)
        else:
            pass
    for dic in js:
        if dic["class"] == "roi":
            pass
        else:
            # 第二遍循环找到类别，并寻找其所在的roi区域，添加到rois列表中对应的roi的poses属性中
            for roi1 in rois:
                if roi1["x"] <= dic["x"] and roi1["y"] <= dic["y"] and dic["x"] + dic["w"] <= roi1["x"] + roi1["w"] and \
                        dic["y"] + dic["h"] <= roi1["y"] + roi1["h"]:
                    roi1["poses"].append(dic)
    return rois
#
#
# rois = get_roi(label1)
# for i, roi1 in enumerate(rois):
#     roi = reader.ReadRoi(roi1["x"], roi1["y"], roi1["w"], roi1["h"], scale)
#     for pos in roi1["poses"]:
#         rx = pos["x"] - roi1["x"]
#         ry = pos["y"] - roi1["y"]
#         cv2.rectangle(roi, (rx, ry), (rx + pos["w"], ry + pos["h"]), (0, 255, 0), 4)
#     save_name = "roi" + str(i + 5) + ".jpg"
#     cv2.imwrite(save_name, roi)
#     print("save roi img:" + save_name)

file_dir = r"G:/paper/dataset/neg_0"  # kfb文件目录
json_dir = r"G:/paper/dataset/labels"  # 标签列表
dest_dir = r"G:/paper/dataset/rois"  # 文件保存目录
origin_dir = r"G:/paper/dataset/origins"  # 感兴趣区域原始图片（未加标注框）


files = os.listdir(file_dir)
labels = os.listdir(json_dir)
cnt = 0
# 读取的roi区域并划分出pos
# for label in labels:
#     file = label[:-5] + ".kfb"  # 找到对应的标签的文件\
#     if file in files:
#         # 存在kfb文件
#         file = file_dir + "/" + file
#         kr.reader.ReadInfo(reader, file, scale, True)  # 设置读取文件
#         rois = get_roi(json_dir + "/" + label)  # 解析json得到roi
#         for i, roi1 in enumerate(rois):
#             roi = reader.ReadRoi(roi1["x"], roi1["y"], roi1["w"], roi1["h"], scale)
#             # origin_name = origin_dir + "/" + label[:-5] + "_" + str(i) + ".jpg"
#             # cv2.imwrite(origin_name, roi)
#             for pos in roi1["poses"]:
#                 print(cnt)
#                 cnt += 1
#                 rx = pos["x"] - roi1["x"]
#                 ry = pos["y"] - roi1["y"]
#                 cv2.rectangle(roi, (rx, ry), (rx + pos["w"], ry + pos["h"]), (0, 255, 0), 4)
#             save_name = dest_dir + "/" + label[:-5] + "_" + str(i) + ".jpg"
#             cv2.imwrite(save_name, roi)
#             print("save roi img:" + save_name)

# 滑窗裁剪全部的图片
ct = 0
for label in labels:
    ct += 1
    if ct == 2:
        break
    file = label[:-5] + ".kfb"  # 找到对应的标签的文件\
    if file in files:
        # 存在kfb文件
        file = file_dir + "/" + file
        kr.reader.ReadInfo(reader, file, scale, True)  # 设置读取文件
        rois = get_roi(json_dir + "/" + label)  # 解析json得到roi

        #todo
        height = reader.getHeight()
        width = reader.getWidth()

        for i, roi1 in enumerate(rois):
            roi = reader.ReadRoi(roi1["x"], roi1["y"], roi1["w"], roi1["h"], scale)
            print(reader.getWidth())
            # origin_name = origin_dir + "/" + label[:-5] + "_" + str(i) + ".jpg"
            # cv2.imwrite(origin_name, roi)
            for pos in roi1["poses"]:
                print(cnt)
                cnt += 1
                rx = pos["x"] - roi1["x"]
                ry = pos["y"] - roi1["y"]
                cv2.rectangle(roi, (rx, ry), (rx + pos["w"], ry + pos["h"]), (0, 255, 0), 4)
            # save_name = dest_dir + "/" + label[:-5] + "_" + str(i) + ".jpg"
            # cv2.imwrite(save_name, roi)
            # print("save roi img:" + save_name)

print(cnt)