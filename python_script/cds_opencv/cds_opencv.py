import cv2 as cv
import numpy as np
import os
import logging

# 读取图像
def read_img(filename):
    if(os.path.exists(filename)):
        img = cv.imread(filename, 1)
        cv.imshow("x", img)
    return img
    # logging.

#  拆分图像通道
def split_img_2_rgb_channel(img):
    b, g, r = cv.split(img)
    return r, g, b

# 图像色彩控件转变
def color_space_changed(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return img

def img_info_analysis(img):
    logging.info("img_info_analysis")
    pass


def main():
    LOG_FORMAT = "%(asctime)s-%(levelname)s : %(message)s"
    logging.basicConfig(level=logging.INFO,  filemode = 'a', format=LOG_FORMAT)

    file_path = "1.png"
    img = read_img(file_path)
    cv.imshow("1", color_space_changed(img))    
    img_info_analysis(img)
    cv.waitKey(0)
        

if __name__ == '__main__':
    main()
    