package main

import (
    "fmt"
    "strings"
    "strconv"
    "time"
)

func main() {
    // 提示用户输入未来时间点
    fmt.Println("请输入未来时间点（格式：日子-小时-分钟，例如：05-17-30）：")
    var inputStr string
    fmt.Scanln(&inputStr)

    // 解析用户输入的字符串为日、小时和分钟
    input := strings.Split(inputStr, "-")
    day, _ := strconv.Atoi(input[0])
    hour, _ := strconv.Atoi(input[1])
    minute, _ := strconv.Atoi(input[2])

    // 使用当前日期和时间，以及用户输入的日、小时和分钟创建时间对象
    currentTime := time.Now()
    futureTime := time.Date(currentTime.Year(), currentTime.Month(), day, hour, minute, 0, 0, currentTime.Location())

    for {
        // 获取当前日期和时间
        currentTime = time.Now()

        // 计算距离未来时间点的时间差
        timeLeft := futureTime.Sub(currentTime)

        // 格式化时间差为时:分:秒
        hours := int(timeLeft.Hours())
        minutes := int(timeLeft.Minutes()) % 60
        seconds := int(timeLeft.Seconds()) % 60
        timeLeftStr := fmt.Sprintf("%02d:%02d:%02d", hours, minutes, seconds)

        // 打印时间差
        fmt.Println("Time left until the future time point:", timeLeftStr)

        // 每隔5秒钟更新一次时间差
        time.Sleep(5 * time.Second)
    }
}
