#!/bin/bash

# 提示用户输入未来时间点
echo "请输入未来时间点（格式：日子-小时-分钟，例如：05-17-30）："
read input_str

# 解析用户输入的字符串为日、小时和分钟
IFS="-" read -r day hour minute <<< "$input_str"

# 使用当前年份和月份，以及用户输入的日、小时和分钟创建时间戳
current_year=$(date +"%Y")
current_month=$(date +"%m")
future_timestamp=$(date -d "$current_year-$current_month-$day $hour:$minute" +"%s")

while true; do
  # 获取当前的时间戳
  current_timestamp=$(date +"%s")

  # 计算距离未来时间点的时间差（秒）
  time_left=$((future_timestamp - current_timestamp))

  # 将时间差转换为小时、分钟和秒
  time_left_hour=$((time_left / 3600))
  time_left_minute=$(( (time_left % 3600) / 60 ))
  time_left_second=$((time_left % 60))

  # 格式化时间差为"小时-分钟-秒"
  formatted_time_left=$(printf "%02d-%02d-%02d" "$time_left_hour" "$time_left_minute" "$time_left_second")

  # 打印格式化后的时间差
  echo "距离未来时间点还有：$formatted_time_left"

  # 暂停程序执行，等待5秒钟
  sleep 5
done
