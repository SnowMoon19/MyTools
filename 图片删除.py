import os
import random
import shutil

# idx = 0
# path = r'C:\Users\Administrator\Desktop\fsdownload\train'
# img_list = os.listdir(path)
# random.shuffle(img_list)
# for i in img_list:
#     if idx == 5000: break
#     if i[0] == "皖":
#         print(i)
#         idx += 1
#         os.remove(path + "//" + i)

path = r'C:\Users\Administrator\Desktop\pic\Dataset'
targetPath = r'C:\Users\Administrator\Desktop\fsdownload\train'
img_list = os.listdir(path)
target_list = os.listdir(targetPath)

random.shuffle(img_list)

idx = 0
for i in img_list:
    if idx == 10000:
        break
    if i not in target_list:
        shutil.copy(path + '/' + i, targetPath + '/' + i)
        idx += 1
    else:
        print(i)



