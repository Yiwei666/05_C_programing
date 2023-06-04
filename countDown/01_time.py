import datetime
import time

# 提示用户输入未来时间点
print("请输入未来时间点（格式：日子-小时-分钟，例如：05-17-30）：")
input_str = input()

# 解析用户输入的字符串为日、小时和分钟
day, hour, minute = input_str.split("-")

# 使用当前年份和月份，以及用户输入的日、小时和分钟创建datetime对象
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
future_date = datetime.datetime(current_year, current_month, int(day), int(hour), int(minute))

while True:
    # 获取当前的日期和时间
    current_date = datetime.datetime.now()

    # 计算距离未来时间点的时间差
    time_left = future_date - current_date

    # 打印时间差
    print("距离未来时间点还有：", time_left)

    # 每隔5秒钟更新一次时间差
    time.sleep(30)