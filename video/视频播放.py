import cv2

# 打开视频文件
video_file = "20230606-160719.mp4"
video = cv2.VideoCapture(video_file)

# 检查视频文件是否成功打开
if not video.isOpened():
    print("无法打开视频文件:", video_file)
    exit()

# 循环播放视频帧
while True:
    # 读取当前帧
    ret, frame = video.read()

    # 如果视频帧读取失败，退出循环
    if not ret:
        break

    # 在窗口中显示当前帧
    cv2.imshow("Video Player", frame)

    # 等待用户按下 'q' 键退出播放
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 关闭窗口和释放资源
video.release()
cv2.destroyAllWindows()
