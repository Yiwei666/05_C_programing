### characterToAudio.py
- 左侧代码的功能是使用Python的requests库和socks库设置SOCKS5代理。
- 然后使用gTTS库将文本转换为音频，并使用pygame库播放音频文件。代码会循环播放音频文件，直到程序被手动停止。  
<br>
以下是代码中使用的库以及安装命令： 

requests库：用于发送HTTP请求。如果你尚未安装该库，可以使用以下命令进行安装： 
```
pip install requests 
```
socks库：用于设置代理。如果你尚未安装该库，可以使用以下命令进行安装：
```
pip install PySocks
```
gtts库：用于将文本转换为音频。如果你尚未安装该库，可以使用以下命令进行安装：
```
pip install gtts
```
pygame库：用于音频播放和控制。如果你尚未安装该库，可以使用以下命令进行安装：
```
pip install pygame
```
请注意，某些库可能需要额外的依赖项。如果安装过程中出现错误，请根据错误信息进行相应的调查和处理。

安装上述库后，你可以执行代码。确保在执行代码之前，本地的SOCKS5代理服务器正在运行，并且代理配置（主机和端口）正确。