# 1. 项目功能

windows配置脚本和程序的cmd快捷命令


# 2. 项目结构

```
# 读取显示cmd.txt中的命令列表，根据用户输入的命令序号执行相应命令
sft.c
sft.exe
cmd.txt

# 使用python脚本读取 python.txt 中的命令并列表显示，然后根据用户输入的命令序号执行相应命令
command_list.py
python.txt

# 该脚本已弃用
execute_commands.py
```


# 3. 环境配置


### 1. `gcc/g++` 安装

1. 命令提示符判断是否安装了 gcc 或 g++ 编译器

```cmd
gcc --version
g++ --version
```

2. 编译

```cmd
gcc sft.c -o sft
```

3. 添加环境变量

在“环境变量”窗口中，你会看到两个环境变量列表：用户变量和系统变量。根据你的需要，你可以选择修改用户变量（只对当前用户有效）或系统变量（对所有用户有效）。

在相应的列表中找到名为“Path”的变量，然后选择它。

1. 点击“编辑”（在一些Windows版本中可能是“修改”）。
2. 在“编辑环境变量”窗口，点击“新建”。
3. 输入或粘贴你的软件路径：`D:\software\10_sft\`（注意不包括 `sft.exe`，只需到文件所在的文件夹路径）。
4. 点击“确定”保存你的更改。




### 2. 文件说明

- `sft.c`

这段代码主要功能是从一个名为 `cmd.txt` 的文件中读取命令列表，显示给用户，并根据用户输入的命令编号执行相应的命令 
添加环境变量时只需要将 `‪D:\software\10_sft\sft.exe` 路径中 `‪D:\software\10_sft\` 这一部分写入到系统变量即可


- `cmd.txt`

存储命令列表的文件，命令中不可包含中文路径

```cmd
python D:\software\10_sft\command_list.py
multiwfn
python
gnuplot
packmol
D:\software\09_v2ray\v2ray-windows-64-v5.4\run_random_v2ray.exe
D:\software\10_sft\01_time-CountDown\update.exe
java -cp D:\software\10_sft\01_time-CountDown TimeDifference
node D:\software\10_sft\01_time-CountDown\future_time_counter.js
python D:\software\10_sft\execute_commands.py
start "" "C:\Program Files\Isaacs\isaacs.exe"
start "" "C:\Users\sun78\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Spyder (anaconda3)"
start "" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\WinSCP"
start "" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\EndNote\EndNote"
start "" "D:\software\18_phpStorm\installfile\PhpStorm 2023.1.3\bin\phpstorm64.exe"
start "" "C:\Users\sun78\AppData\Local\Programs\Microsoft VS Code\Code.exe"
start "" "D:\software\03_Dev-C++\installfile\Dev-Cpp\devcpp.exe"
start "" "D:\software\04_RStudio\installfile\RStudio\rstudio.exe"


// load "data.txt" || packmol < inputfile.inp || To quit using q
// cd D:\software\10_sft || dir || type file.txt || cd /d C: ||
//To compile C source code using gcc: gcc source_file.c -o output_file
To quit using q
```


- `command_list.py`

这段代码的功能是从一个名为`python.txt`的文件中读取命令，然后显示这些命令的列表。接着，程序会循环读取用户输入的命令编号，并执行对应的命令。如果用户输入的编号无效，程序会提示错误信息。当用户输入0时，程序结束。


- `python.txt`

存储命令列表的文件，命令中可包含中文路径


- `execute_commands.py`

这段Python代码打开一个名为`"python.txt"`的文件，该文件位于`"D:/software/10_sft/"`目录下。假设文件中的每一行都包含一个Shell命令。代码然后使用`subprocess.call()`函数执行每个命令。











