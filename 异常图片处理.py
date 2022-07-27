# 处理异常图片
import os
import cv2
import numpy as np

path = "C://Users//Administrator//Desktop//fsdownload//pics_5_19//"

def compute(path):
    file_names = os.listdir(path)
    per_image_Rmean = []
    per_image_Gmean = []
    per_image_Bmean = []
    idx = 0

    f = open('C://Users//Administrator//Desktop//dir.txt', 'r+') # 有问题的图片路径保存到txt中

    for file_name in file_names:
        print(file_name)
        #img = cv2.imread(os.path.join(path, file_name), 1)
        img = cv2.imdecode(np.fromfile(os.path.join(path, file_name), dtype=np.uint8), cv2.IMREAD_COLOR)

        r = np.mean(img[:, :, 2])
        g = np.mean(img[:, :, 1])
        b = np.mean(img[:, :, 0])
        print("R:", r, "G:", g, "B:", b)
        # per_image_Bmean.append(np.mean(img[:, :, 0]))
        # per_image_Gmean.append(np.mean(img[:, :, 1]))
        # per_image_Rmean.append(np.mean(img[:, :, 2]))
        # print("R:", per_image_Rmean[idx], "G:", per_image_Gmean[idx], "B:", per_image_Bmean[idx])

        # # 暂定R+10>B时处理
        # if r + 10 > b:
        f.write(os.path.join(file_name) + '\n')

        # idx += 1
        # if idx == 1000: break

    # R_mean = np.mean(per_image_Rmean)
    # G_mean = np.mean(per_image_Gmean)
    # B_mean = np.mean(per_image_Bmean)
    f.close()
    # return R_mean, G_mean, B_mean
    return 0, 0, 0





if __name__ == '__main__':
    R, G, B = compute(path)
    print(R, G, B)

