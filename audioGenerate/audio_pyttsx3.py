# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 10:12:19 2023

@author: sun78
"""

import pyttsx3
import time

text = input("Enter some text: ")

# 循环播放语音
while True:
    sleptim = 1.3
    
    # 创建新的pyttsx3引擎
    engine = pyttsx3.init()

    # 设置语言为中文
    engine.setProperty("voice", "zh")

    # 设置语音播放速度
    engine.setProperty("rate", 150)  # 调整播放速度，可以尝试不同的值

    # 将文本转换为语音
    engine.say(text)

    # 开始转换文本到语音
    engine.runAndWait()

    # 停止引擎
    engine.stop()

    # 延迟1秒
    time.sleep(sleptim)
