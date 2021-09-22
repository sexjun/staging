#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import shutil
import hashlib
import stat

class FileHandler:
    '''基本描述

    详细描述

    :param path: The path of the file to wrap
    :type path: str
    :param field_storage: The :class:`FileStorage` instance to wrap
    :type field_storage: FileStorage
    :param temporary: Whether or not to delete the file when the File instance is destructed
    :type temporary: bool
    :returns: A buffered writable file descriptor
    :rtype: BufferedFileStorage
    '''
    def __init__(self):
        pass

    '''查找文件夹中的某个文件

        :dirpath : 目标路径
        :findFile: 查找文件的名字
        rttpe: 
            查找成功： 返回该文件的文件夹的绝对路径
            查找失败： 返回None
        
    '''
    def findMyFileDir(self, dirPath, findFile):
        files = []
        dirs = []
        for root, dirs, files in os.walk(dirPath, topdown=False):
            for file in files:
                if file == findFile:
                    return root
            for dir in dirs:
                findMyFileDir(os.path.join(root, dir), findFile)
    
    #创建一个文件夹
    def createDir(self, dirPath):
        os.makedirs(dirPath, exist_ok=True)

    #删除一个文件
    def delFile(self, filePath):
        if os.path.exists(filePath):
            os.remove(filePath)

def test_file_handler():
    print("Testing file handler")
    filehandler = FileHandler()
    result = filehandler.findMyFileDir(r"C:\Users\cds\Desktop\github_project\staging\python_script\File_Oprator", "ddddd.py")
    print("File handler:{}".format(result))

test_file_handler()