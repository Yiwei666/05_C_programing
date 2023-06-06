# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 12:56:03 2023

@author: sun78
"""

import youtube_dl

import socks
import socket


# 设置SOCKS5代理
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
socket.socket = socks.socksocket


def download_video(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# 提供要下载的YouTube视频的URL
video_url = "https://youtu.be/a0AyNzV3yk8"

# 调用下载函数
download_video(video_url)
