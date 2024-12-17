import os

def list_directory_tree(root_dir, depth, current_level=1):
    """
    打印目录树结构到指定深度，模拟 Linux 样式。

    :param root_dir: 要查看的根目录。
    :param depth: 查看目录的深度。
    :param current_level: 当前层级。
    """
    try:
        entries = os.listdir(root_dir)
        entries.sort()  # 排序以更美观地显示目录
        total_entries = len(entries)

        for idx, entry in enumerate(entries):
            entry_path = os.path.join(root_dir, entry)
            is_last = idx == total_entries - 1

            # 根据是否为最后一项选择连接符号
            prefix = "└── " if is_last else "├── "
            connector = "    " if is_last else "│   "

            print("" + "    " * (current_level - 1) + prefix + entry)

            # 如果是目录且未超出深度限制，则递归
            if os.path.isdir(entry_path) and current_level < depth:
                list_directory_tree(entry_path, depth, current_level + 1)
    except PermissionError:
        print("    " * (current_level - 1) + "└── [Permission Denied]")
    except FileNotFoundError:
        print("    " * (current_level - 1) + "└── [Directory Not Found]")

if __name__ == "__main__":
    # 提示用户输入
    directory = input("请输入要查看的目录路径: ").strip()
    try:
        max_depth = int(input("请输入查看的目录深度（正整数）: ").strip())
        if max_depth < 1:
            raise ValueError("深度必须为正整数！")
    except ValueError as e:
        print(f"输入无效: {e}")
        exit(1)

    # 检查输入的目录是否存在
    if not os.path.exists(directory):
        print("目录不存在，请检查路径后重试。")
    else:
        print(f"\n目录树结构 ({directory}) 深度 {max_depth}：\n")
        list_directory_tree(directory, max_depth)
