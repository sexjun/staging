[CSDN博客地址](https://editor.csdn.net/md/?articleId=128474961)


CSV (Comma Separated Values) 格式是电子表格和数据库中最常见的输入、输出文件格式。在 RFC 4180 规范推出的很多年前，CSV 格式就已经被开始使用了，由于当时并没有合理的标准，不同应用程序读写的数据会存在细微的差别。这种差别让处理多个来源的 CSV 文件变得困难。但尽管分隔符会变化，此类文件的大致格式是相似的，所以编写一个单独的模块以高效处理此类数据，将程序员从读写数据的繁琐细节中解放出来是有可能的。

csv 模块实现了 CSV 格式表单数据的读写。其提供了诸如“以兼容 Excel 的方式输出数据文件”或“读取 Excel 程序输出的数据文件”的功能，程序员无需知道 Excel 所采用 CSV 格式的细节。此模块同样可以用于定义其他应用程序可用的 CSV 格式或定义特定需求的 CSV 格式。

**推荐教程：**  [python官网：csv模块中文使用教程](https://docs.python.org/zh-cn/3/library/csv.html)
> 官网的教程是最全面的，但是比较晦涩，大家要耐心阅读！

## 总览
csv总共有二重要API：
-  `read`
	- 函数接口：
		```python
		with open('eggs.csv', newline='') as csvfile:
		    spamreader = csv.reader(csvfile)
		    for row in spamreader:
		        print(row)
		```
	- 字典接口![在这里插入图片描述](https://img-blog.csdnimg.cn/524fa26ff952423da2a5e0bbcfb3b39b.png)

		```python
		with open("./test.csv", "r") as csvfile:
		    reader = csv.DictReader(csvfile)
		    for row in reader:
		        print(row['nnc'])
		        print(row['input'])
		        print(row['output'])
		```
- `write`
	- 函数接口： ![在这里插入图片描述](https://img-blog.csdnimg.cn/f9974e4402a9405a9dc485af225f28a7.png)

		```python
		test_list = [
		    "January",
		    "February",
		    "March",
		    "April",
		    "May",
		    "June",
		]
		with open("./test2.csv", "w") as f:
		    cw = csv.writer(f)
		    cw.writerow(test_list)
		```
	- 字典接口![在这里插入图片描述](https://img-blog.csdnimg.cn/451e713834b7447aaf7ce020b39309f8.png)

		```python
			with open("test.csv", "w") as f:
			    fieldnames = ['nnc', 'input', 'output']
			    writer = csv.DictWriter(f, fieldnames=fieldnames)
			    writer.writeheader()
			    for j in j_info:
			        writer.writerow(j)
			        print(j)
		```
# write csv file
- 字典接口


## 写csv

假如说要写入以下内容，则可以从json文件中，序列化对象，然后转位json对象，将json对象在写入csv文件中。
![在这里插入图片描述](https://img-blog.csdnimg.cn/513f31d30bd74ea899e9159e8809f0fd.png)

```python

import csv
import json

with open("./test.json", "r") as f:
    j_info = json.loads(f.read())
with open("test.csv", "w") as f:
    fieldnames = ['nnc', 'input', 'output']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for j in j_info:
        writer.writerow(j)
        print(j)


```


- `test.json` 文件内容
```json
[
    {
        "nnc": "name",
        "input": [
            1,
            2,
            3
        ],
        "output": [
            2,
            3,
            4
        ]
    },
    {
        "nnc": "name",
        "input": [
            1,
            2,
            3
        ],
        "output": [
            2,
            3,
            4
        ]
    },
    {
        "nnc": "name",
        "input": [
            1,
            2,
            3
        ],
        "output": [
            2,
            3,
            4
        ]
    },
    {
        "nnc": "name",
        "input": [
            1,
            2,
            3
        ],
        "output": [
            2,
            3,
            4
        ]
    },
    {
        "nnc": "name",
        "input": [
            1,
            2,
            3
        ],
        "output": [
            2,
            3,
            4
        ]
    }
]

```
