#include <stdio.h>
#include <stdlib.h>
#include <tchar.h>

#define MAX_COMMANDS 100

int main()
{
    FILE* fp;
    TCHAR commands[MAX_COMMANDS][1024];
    int n_commands = 0;
    int i;

    // 打开文件
    // fp = _tfopen(_T("cmd.txt"), _T("r"));   // fp = _tfopen(_T("D:\\software\\10_sft\\cmd.txt"), _T("r"));
    fp = _tfopen(_T("D:\\software\\10_sft\\cmd.txt"), _T("r"));
    if (fp == NULL) {
        _tprintf(_T("Failed to open file\n"));
        return 1;
    }

    // 读取命令
    while (n_commands < MAX_COMMANDS && _fgetts(commands[n_commands], 1024, fp)) {
        n_commands++;
    }

    // 关闭文件
    fclose(fp);

    // 显示命令列表
    for (i = 0; i < n_commands; i++) {
        _tprintf(_T("%d. %s"), i+1, commands[i]);
    }

    // 循环读取用户输入的命令编号，并执行对应的命令
    while (1) {
        TCHAR input[10];
        int index;

        _tprintf(_T("Enter command number: "));
        _fgetts(input, 10, stdin);

        index = _tstoi(input);
        if (index < 0 || index > n_commands) {
            _tprintf(_T("Invalid input\n"));
            continue;
        }
        if (index == 0) {
            break;
        }

        // 打印注释
        TCHAR* comment = _tcschr(commands[index-1], '#');
        if (comment != NULL) {
            _tprintf(_T("%s\n"), comment + 1);
        }

        system(commands[index-1]);
    }

    return 0;
}