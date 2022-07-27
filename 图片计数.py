# 文件计数
import os


def count(path):
    files = os.listdir(path)
    province_total = {}
    for file in files:
        key = file[0]
        if key not in province_total:
            province_total[key] = 1
        else:
            province_total[key] += 1
    return province_total


if __name__ == '__main__':
    path = r'C:\Users\Administrator\Desktop\fsdownload\train'
    cnt = count(path)
    print(cnt)