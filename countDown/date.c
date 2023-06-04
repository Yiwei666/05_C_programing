#include <stdio.h>
#include <time.h>
#include <windows.h>

int main() {
    int day, hour, minute;
    time_t current_time, future_time;
    struct tm *future_tm;
    char input_str[10];

    // Prompt the user to input a future time point
    printf("Please enter a future time point (format: day-hour-minute, e.g. 05-17-30): ");
    scanf("%d-%d-%d", &day, &hour, &minute);

    // Use the current date and time to create a time_t object
    current_time = time(NULL);

    // Use the current date and time and the user input to calculate the future time point as a time_t object
    future_tm = localtime(&current_time);
    future_tm->tm_mday = day;
    future_tm->tm_hour = hour;
    future_tm->tm_min = minute;
    future_time = mktime(future_tm);

    while (1) {
        // Get the current date and time
        current_time = time(NULL);

        // Calculate the time difference between the current time and the future time point
        double time_left = difftime(future_time, current_time);

        // Convert the time difference to hours, minutes, and seconds
        int hours = (int) time_left / 3600;
        int minutes = (int) (time_left - hours * 3600) / 60;
        int seconds = (int) time_left % 60;

        // Print the time difference in the format of hours:minutes:seconds
        printf("Time left until the future time point: %02d:%02d:%02d\n", hours, minutes, seconds);

        // Wait for 5 seconds before updating the time difference again
        Sleep(5000);
    }

    return 0;
}
