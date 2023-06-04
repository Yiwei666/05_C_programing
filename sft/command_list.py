import os

MAX_COMMANDS = 100
commands = []

# 打开文件
with open('D:\\software\\10_sft\\python.txt', 'r', encoding="utf-8") as fp:
    # 读取命令
    for i in range(MAX_COMMANDS):
        command = fp.readline().strip()
        if not command:
            break
        commands.append(command)

# 显示命令列表
for i, command in enumerate(commands):
    print(f"{i+1}. {command}")

# 循环读取用户输入的命令编号，并执行对应的命令
while True:
    input_str = input("Enter command number: ")
    try:
        index = int(input_str)
    except ValueError:
        print("Invalid input")
        continue
    if index < 0 or index > len(commands):
        print("Invalid input")
        continue
    if index == 0:
        break

    # 打印注释
    comment = commands[index-1].find('#')
    if comment != -1:
        print(commands[index-1][comment+1:])

    os.system(commands[index-1])
    