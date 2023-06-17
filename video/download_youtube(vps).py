
# import socks
# import socket
from pytube import YouTube

# 设置SOCKS5代理
# socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
# socket.socket = socks.socksocket

def download_video(url):
    try:
        # 创建YouTube对象
        yt = YouTube(url)
        
        # 获取视频的所有可用格式
        available_streams = yt.streams.filter(progressive=True).all()
        
        # 选择最高质量的视频格式
        video = available_streams[-1]
        
        # 下载视频
        video.download()
        
        print("视频下载完成！")
        
    except Exception as e:
        print("下载失败:", str(e))

# 提供要下载的YouTube视频的URL

# video_url = "https://www.youtube.com/watch?v=bu7nU9Mhpyo"
video_url = input("please input youtube video url")

# 调用下载函数
download_video(video_url)
