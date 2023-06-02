#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_COMMANDS 100
#define MAX_COMMAND_LENGTH 256

int main(int argc, char *argv[]) {
    // char *filename = "v2ray_commands.txt";
    char *filename = "D:\\software\\09_v2ray\\v2ray-windows-64-v5.4\\v2ray_commands.txt";
    char commands[MAX_COMMANDS][MAX_COMMAND_LENGTH];
    int line_numbers[MAX_COMMANDS];
    int num_commands = 0;
    int i, selected_line;
    FILE *fp;
    
    // Open the commands file for reading
    fp = fopen(filename, "r");
    if (fp == NULL) {
        fprintf(stderr, "Error: could not open file %s\n", filename);
        exit(1);
    }
    
    // Read the commands into the commands array
    while (fgets(commands[num_commands], MAX_COMMAND_LENGTH, fp) != NULL) {
        // Remove newline character from the end of each command
        commands[num_commands][strcspn(commands[num_commands], "\n")] = '\0';
        line_numbers[num_commands] = num_commands + 1; // Store the line number
        num_commands++;
    }
    
    // Close the commands file
    fclose(fp);
    
    // Print the available commands and their line numbers
    printf("Available commands:\n");
    for (i = 0; i < num_commands; i++) {
        printf("%d. %s\n", line_numbers[i], commands[i]);
    }
    
    // Prompt the user to select a command
    printf("Enter the line number of the command you want to run: ");
    scanf("%d", &selected_line);
    
    // Check if the selected line number is valid
    if (selected_line < 1 || selected_line > num_commands) {
        fprintf(stderr, "Error: invalid line number\n");
        exit(1);
    }
    
    // Execute the selected command
    printf("Running command: %s\n", commands[selected_line - 1]);
    system(commands[selected_line - 1]);
    
    return 0;
}
