# 项目功能

- 使用本地socks5代理下载指定python模块
- 使用pytube模块下载youtube视频


# 环境配置

- 使用本地socks5代理的1080端口下载python模块

```python
import socks
import socket
import subprocess

# 设置SOCKS5代理
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
socket.socket = socks.socksocket

# 定义要运行的命令
command = "pip install mp-api"

# 使用subprocess运行命令
try:
    subprocess.check_call(command, shell=True)
    print("安装成功")
except subprocess.CalledProcessError as e:
    print("安装失败:", e)
```

- 下载pytube模块

pytube：这是一个功能强大且易于使用的库，专门用于从YouTube下载视频。它提供了各种选项和功能，如选择视频质量、下载视频和音频等。你可以使用pip来安装pytube库。

```
pip install pytube
```


