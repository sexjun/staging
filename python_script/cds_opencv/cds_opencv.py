import cv2 as cv
import numpy as np
import os
import logging

# 读取图像
def read_img(filename):
    run_path = os.path.join(os.getcwd(), "python_script\cds_opencv")
    os.chdir(run_path)
    logging.info("workpath: {}".format(run_path))
    if(os.path.exists(filename)):
        img = cv.imread(filename, flags=cv.IMREAD_UNCHANGED)
        # img = cv.imread(filename, 1)
        if(img is None):
            logging.info("img isnull")
            return None
        else:
            cv.imshow("x", img)
            return img 
    else:
        logging.error("filename:{} is null or empty".format(filename))


#  拆分图像通道
def split_img_2_rgb_channel(img):
    if(img is None):
        logging.error("img is null")
        return None
    if(img.shape[2] == 3):
        logging.error("img is rgb")
        b, g, r = cv.split(img)
        return r, g, b
    elif(img.shape[2] == 4):
        logging.error("img is argb")
        a, b, g, r = cv.split(img)
        return a, r, g, b
        


# 图像色彩控件转变
def color_space_changed(img):
    if (img is None):
        logging.error("img is None")
        return False

    if(img is None):
        logging.error("img is null")
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return img

# 图像的信息分析
def img_info_analysis(img):
    if (img is None):
        return False
    hight, width, chanel = img.shape
    logging.info("hight:{}, width:{}, chanel:{}".format(hight, width, chanel))


def main():
    LOG_FORMAT = "%(asctime)s-%(levelname)s : %(message)s"
    logging.basicConfig(level=logging.INFO,  filemode = 'a', format=LOG_FORMAT)

    # file_path = "./1.png"
    file_path = "touming.png"
    img = read_img(file_path)
    
    split_img_2_rgb_channel(img)
    cv.imshow("1", color_space_changed(img))    
    img_info_analysis(img)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
    