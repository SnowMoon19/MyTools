import os
import random
import shutil


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


def getData(src_path):
    # 这个文件夹需要提前建好
    dest_dir = r"C:\Users\Administrator\Desktop\pic\local_data"
    img_list = get_imlist(src_path)
    random.shuffle(img_list)
    le = int(len(img_list) * 0.8)  # 这个可以修改划分比例
    for f in img_list[le:]:
        shutil.move(f, dest_dir)


getData(r'C:\Users\Administrator\Desktop\pic\Dataset')
