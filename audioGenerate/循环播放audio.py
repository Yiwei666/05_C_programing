# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 15:19:12 2023

@author: sun78
"""

import requests
import socks
import socket
from gtts import gTTS
import pygame
import time

# 设置SOCKS5代理
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
socket.socket = socks.socksocket

# 创建gtts对象，将文本转换为音频
# text = input("Enter some text: ")
# tts = gTTS(text="每天的时间都是有限的，珍惜时间。", lang="zh-cn")
# tts = gTTS(text, lang="zh-cn")
# tts.save("audio.mp3")

# 初始化pygame
pygame.mixer.init()

# 加载音频文件
pygame.mixer.music.load("D:/software/10_sft/03_audio_generate/audio.mp3")

# 循环播放音频
while True:
    # 播放音频
    pygame.mixer.music.play()

    # 等待音频播放结束
    while pygame.mixer.music.get_busy():
        time.sleep(1.5)

    # 延迟1秒
    time.sleep(1)
