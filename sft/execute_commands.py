import subprocess

# 打开文件
with open("D:/software/10_sft/python.txt", "r", encoding="utf-8") as file:
    # 逐行读取文件内容
    for line in file:
        # 删除行末的换行符
        command = line.rstrip("\n")
        
        # 执行命令
        subprocess.call(command, shell=True)
