# 智能穿戴



### 12h与24h对应关系


| 24小时制度 | 12小时 |
| ----      | ----                |
|0          |     上午12点         |
|1          |     上午1点         |
|2          |     上午2点         |
|3          |     上午3点         |
|4          |     上午4点         |
|5          |     上午5点         |
|6          |     上午6点         |
|7          |     上午7点         |
|8          |     上午8点         |
|9          |     上午9点         |
|10         |     上午10点         |
|11         |     上午11点         |
|12         |     下午12点         |
|13         |     下午1点         |
|14         |     下午2点         |
|15         |     下午3点         |
|16         |     下午4点         |
|17         |     下午5点         |
|18         |     下午6点         |
|19         |     下午7点         |
|20         |     下午8点         |
|21         |     下午9点         |
|22         |     下午10点         |
|23         |     下午11点         |





## 死机分析技巧



将机器的死机dump进行保存，一般会被存为Assic码，分析时候将Assic转为hex进行分析，将hex转为bin二进制进行加载到机器里。



- 反编译

keil编译的文件`.axf`进行反汇编分析。

```c
objdump -d xxx.axf > xxx.s
```



**分析死机dumps**

dumps可以理解为内存快照。分析死机借助的Ozone工具。

流程为：

1. 加载死机dumps

```c
Target.LoadMemory("D:\path_of_axf\st_crash_dump.bin", psram_start_add)
```

2. 在`Tasks.c`文件中维护

```c

```

3. 防止被狗咬

Ozone --> Debug --> save snapshot 保存内存镜像

然后Load snapshot在加载内存镜像



**小课堂**

- PC指针

`Program Counter` 程序计数器

指向下一个要运行的指令地址，因为arm系列是三级流水线，每一个指令4个字节。

1. 取指令： pc指针指向的地址
2. 译指
3. 执行： cpu运行根基

CPU运行地址= 当前PC值 = 当前程序执行位置 + 8

- SP指针

`Stack Pointer`堆栈指针





## Ozone使用笔记

1. 新建工程

<img src="https://tu-chuang-1253216127.cos.ap-beijing.myqcloud.com/20210922233207.png" alt="image-20210922233207045" style="zoom: 80%;" />

2. 选择Debug

![image-20210922233318905](https://tu-chuang-1253216127.cos.ap-beijing.myqcloud.com/20210922233318.png)

3. 选择调试地方

![image-20210922234259927](https://tu-chuang-1253216127.cos.ap-beijing.myqcloud.com/20210922234259.png)

4. 选择初始化指针位置

![image-20210922234346921](https://tu-chuang-1253216127.cos.ap-beijing.myqcloud.com/20210922234346.png)

5. 完成设置，加载主界面

![image-20210922234424168](https://tu-chuang-1253216127.cos.ap-beijing.myqcloud.com/20210922234424.png)

