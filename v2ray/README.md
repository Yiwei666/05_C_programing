# 1. 项目功能

切换v2ray代理路线

# 2. 切换v2ray代理路线命令行程序

### 1. `run_random_v2ray.c`
 
1. 上述代码的功能是读取一个文本文件`v2ray_commands.txt`中的命令，将其存储在一个数组中，
2. 然后将这些命令打印出来并提示用户选择一个命令。程序会检查用户输入的命令是否有效，如果有效，则执行该命令


### 2. `run_random_v2ray.cpp`

上述代码的c++实现


### 3. `v2ray_commands.txt`

```cmd
// 在v2ray.exe和config.json所在目录运行 v2ray.exe 的cmd命令
v2ray.exe run -c config_0311_do3-1.json         

// 在windows的任意目录下运行 v2ray.exe 的cmd命令
D:\software\09_v2ray\v2ray-windows-64-v5.4\v2ray.exe run -c D:\software\09_v2ray\v2ray-windows-64-v5.4\config_0311_do3-1.json

// 在windows的任意目录下，在新的cmd窗口中运行 v2ray.exe 的cmd命令
start cmd /k "D:\software\09_v2ray\v2ray-windows-64-v5.4\v2ray.exe run -c D:\software\09_v2ray\v2ray-windows-64-v5.4\config_0311_do3-1.json"
```


### 4. 添加`ico`图标到`exe`文件

在MinGW-W64编译器中，可以使用windres命令将ICO文件嵌入到可执行文件中（基于c++代码实现的可执行文件）。下面是使用windres的具体步骤：


**1. 准备ICO文件**

首先，确保你有一个ICO格式的图标文件，该文件将用作程序的图标。确保ICO文件的大小为16x16像素或32x32像素，并记下ICO文件的路径。


**2. 创建资源文件**

创建一个文本文件，例如`resources.rc`，用于定义资源，包括ICO图标。在文件中，添加以下内容：


```
1 ICON "path/to/your_icon.ico"
```

其中，`1`是资源ID，`ICON`是资源类型。


- 同级目录下ico文件的例子

```
1 ICON "myicon.ico"   
```

将`path/to/your_icon.ico`替换为ICO文件的实际路径。


**3. 生成对象文件**

使用windres命令将资源文件编译为对象文件。运行以下命令：

```
windres resources.rc -o resources.o
```
这将生成一个名为`resources.o`的对象文件，其中包含ICO图标的资源。


**4. 编译代码**

使用 `g++` 编译你的 `C++` 代码，并将之前生成的对象文件链接到可执行文件中。运行以下命令：

```
g++ -o your_executable.exe your_code.cpp resources.o
```

这将编译你的代码，并将ICO图标资源嵌入到生成的可执行文件中。


**5. 重新启动程序**

请注意，以上步骤是基于MinGW-W64编译器和Windows环境下的操作。在其他操作系统或编译器上，命令可能会有所不同，请查阅相应的文档或参考特定编译器的使用说明。


- PNG转ico在线网站：[https://png2icojs.com/zh/](https://png2icojs.com/zh/)   
- ico图像在线下载网站：[https://www.iconfinder.com/](https://www.iconfinder.com/)

- ico在线下载网址：[https://www.iconfinder.com/](https://www.iconfinder.com/)



# 3. v2ray路线切换GUI界面

参考项目：https://github.com/Yiwei666/06_java/blob/main/01_smallTools/README.md




# 参考资料

- [使用windres命令将ICO文件嵌入到可执行文件中](https://github.com/Yiwei666/05_C_programing/wiki/02_%E4%BD%BF%E7%94%A8windres%E5%91%BD%E4%BB%A4%E5%B0%86ICO%E6%96%87%E4%BB%B6%E5%B5%8C%E5%85%A5%E5%88%B0%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%96%87%E4%BB%B6%E4%B8%AD)   


