import os
import random
import shutil


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


def getData(src_path):
    img_list = get_imlist(src_path)
    random.shuffle(img_list)
    le = int(len(img_list) * 0.8)  # 这个可以修改划分比例
    for f in img_list[le:]:
        os.remove(f, dest_dir)


getData(r'C:\Users\Administrator\Desktop\pic\Dataset')
