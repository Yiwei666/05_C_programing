# C_programing

### run_random_v2ray.c
 
```
1. 上述代码的功能是读取一个文本文件v2ray_commands.txt中的命令，将其存储在一个数组中，
2. 然后将这些命令打印出来并提示用户选择一个命令。程序会检查用户输入的命令是否有效，如果有效，则执行该命令
```

### run_random_v2ray.cpp
```
上述代码的c++实现
```

### v2ray_commands.txt

```
// 在v2ray.exe和config.json所在目录运行 v2ray.exe 的cmd命令
v2ray.exe run -c config_0311_do3-1.json         

// 在windows的任意目录下运行 v2ray.exe 的cmd命令
D:\software\09_v2ray\v2ray-windows-64-v5.4\v2ray.exe run -c D:\software\09_v2ray\v2ray-windows-64-v5.4\config_0311_do3-1.json

// 在windows的任意目录下，在新的cmd窗口中运行 v2ray.exe 的cmd命令
start cmd /k "D:\software\09_v2ray\v2ray-windows-64-v5.4\v2ray.exe run -c D:\software\09_v2ray\v2ray-windows-64-v5.4\config_0311_do3-1.json"
```
