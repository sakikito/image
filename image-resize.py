import cv2
import os

BASE_DIR = os.path.dirname(__file__)

def get_write_dir_path():

    write_dir_path = os.path.join(BASE_DIR, "write_image")

    if not os.path.exists(write_dir_path):

        os.makedirs(write_dir_path)

    return write_dir_path

get_write_dir_path()

image_num = int(input("画像数: "))

for i in range(1,image_num+1):

    img = cv2.imread(f"read_image\img ({str(i+1)}).jpg")

    size = (600,400)

    img_resize = cv2.resize(img,size)

    cv2.imwrite(f"write_image\resize_{i+1}", img_resize)
