# 说明

本文件路径下主要：

1. python脚本设计开发



包含：

1. python与命令行
2. 时间获取
3. 文件IO， 文本替换
4. 增删查改文件





### python



```python

with open(dirPath, "w+") as f:
    f.close()
    

# 文件路径是否存在
os.path.exists(dirPath)
# 改变工作路径
os.chdir(dir_path)

#创建文件夹
os.mkdir(dir_name)  

# 获取文件的父路径
os.path.dirname(destFilePath)

# 文件拷贝
shutil.copyfile(sourceFilePath, destFilePath, follow_symlinks=False)

# 绝对路径拼接   路径不能用/开头，但是可以用/结尾
src = os.path.join(path, "ddddd.py")
```

