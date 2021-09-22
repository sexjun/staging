#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import shutil
import hashlib
import stat

#获取文件的md5
def getFileMd5(filePath):
    with open(filePath, 'rb') as f:
        content = f.read()
    hash = hashlib.md5()
    hash.update(content)
    return hash.hexdigest()

class FileAdd:
    '''文件增加相关操作

    createDir(self, dirPath)： 创建文件夹
    def copyFile(self, sourceFilePath, destFilePath):拷贝文件

    '''
    def __init__(self):
        pass
    #创建一个文件
    def create_file(self, dirPath, cover_old_file = True):
        if cover_old_file:
            with open(dirPath, "w+") as f:
                f.close()
        else:
            if (os.path.exists(dirPath)):
                return True
            else:
                with open(dirPath, "w+") as f:
                    f.close()

        #创建一个文件夹 dir_path 路径下，建dir_name文件夹
    def createDir(self, dir_path, dir_name):
        # os.makedirs(dirPath, exist_ok=False)   
        path = os.getcwd()
        os.chdir(dir_path)
        os.mkdir(dir_name)   
        os.chdir(path)
    # 拷贝文件
    def copyFile(self, sourceFilePath, destFilePath):
        if not(os.path.exists(sourceFilePath)):
            return False

        if os.path.exists(destFilePath):
            if getFileMd5(sourceFilePath) == getFileMd5(destFilePath):
                return True
            else:
                os.remove(destFilePath)

        destFileDir = os.path.dirname(destFilePath)
        os.makedirs(destFileDir, exist_ok=True)
        if not(shutil.copyfile(sourceFilePath, destFilePath, follow_symlinks=False)):
            return False            
        return True


def test_file_handler():
    path = r"C:\Users\cds\Desktop\github_project\staging\python_script\File_Oprator"
    print("Testing file handler")
    filehandler = FileAdd()

    filehandler.createDir(path, "tes3")
    src = os.path.join(path, "ddddd.py")
    dest = os.path.join(path, "tes3/aa.py")
    filehandler.copyFile(src, dest)

test_file_handler()