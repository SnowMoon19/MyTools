import csv

import numpy as np


def readTxt():
    data = []
    with open("C:/Users/Administrator/Desktop/m01_s01_positions.txt","r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line = line.split()
            data.append(line)
    print(np.shape(data))

    f = open('data3.csv', 'w', encoding='utf-8', newline='')
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)
    for i in range(0, 2300):
        csv_writer.writerow(data[i])

    return data

if __name__ == '__main__':
    readTxt()