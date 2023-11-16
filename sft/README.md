# 项目功能

windows配置脚本和程序的cmd快捷命令


# 项目结构

```
sft.c
sft.exe
cmd.txt


command_list.py
python.txt

# 这段Python代码打开一个名为"python.txt"的文件，该文件位于"D:/software/10_sft/"目录下。假设文件中的每一行都包含一个Shell命令。代码然后使用subprocess.call()函数执行每个命令。
execute_commands.py       
```

- sft.c

这段代码主要功能是从一个名为cmd.txt的文件中读取命令列表，显示给用户，并根据用户输入的命令编号执行相应的命令 
添加环境变量时只需要将‪D:\software\10_sft\sft.exe路径中 ‪D:\software\10_sft\ 这一部分写入到系统变量即可

- cmd.txt

存储命令列表的文件，命令中不可包含中文路径
```
python D:\software\10_sft\command_list.py
multiwfn
python
gnuplot
packmol
D:\software\09_v2ray\v2ray-windows-64-v5.4\run_random_v2ray.exe
D:\software\10_sft\01_time-CountDown\update.exe
python D:\software\10_sft\execute_commands.py
"C:\Program Files\Isaacs\isaacs.exe"
start "" "C:\Users\sun78\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Spyder (anaconda3)"
start "" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WinSCP"
start "" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\EndNote\EndNote"

// load "data.txt" || packmol < inputfile.inp || To quit using q
// cd D:\software\10_sft || dir || type file.txt || cd /d C: ||
//To compile C source code using gcc: gcc source_file.c -o output_file
To quit using q
```

- command_list.py

这段代码的功能是从一个名为python.txt的文件中读取命令，然后显示这些命令的列表。接着，程序会循环读取用户输入的命令编号，并执行对应的命令。如果用户输入的编号无效，程序会提示错误信息。当用户输入0时，程序结束。

- python.txt

存储命令列表的文件，命令中可包含中文路径

