import java.time.LocalDateTime;
import java.time.Duration;
import java.util.Scanner;

public class TimeDifference {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 提示用户输入未来时间点
        System.out.println("请输入未来时间点（格式：日子-小时-分钟，例如：05-17-30）：");
        String inputStr = scanner.nextLine();

        // 解析用户输入的字符串为日、小时和分钟
        String[] parts = inputStr.split("-");
        int day = Integer.parseInt(parts[0]);
        int hour = Integer.parseInt(parts[1]);
        int minute = Integer.parseInt(parts[2]);

        // 使用当前年份和月份，以及用户输入的日、小时和分钟创建LocalDateTime对象
        LocalDateTime now = LocalDateTime.now();
        LocalDateTime futureDate = LocalDateTime.of(now.getYear(), now.getMonth(), day, hour, minute);

        while (true) {
            // 获取当前的日期和时间
            now = LocalDateTime.now();

            // 计算距离未来时间点的时间差
            Duration timeLeft = Duration.between(now, futureDate);

            // 打印时间差
            long hours = timeLeft.toHours();
            long minutes = timeLeft.toMinutes() % 60;
            long seconds = timeLeft.getSeconds() % 60;
            System.out.printf("距离未来时间点还有：%02d:%02d:%02d\n", hours, minutes, seconds);

            // 每隔30秒钟更新一次时间
            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}