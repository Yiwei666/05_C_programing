#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <ctime>

#define MAX_COMMANDS 100
#define MAX_COMMAND_LENGTH 256

int main(int argc, char *argv[]) {
    // std::string filename = "v2ray_commands.txt";
    std::string filename = "D:\\software\\09_v2ray\\v2ray-windows-64-v5.4\\v2ray_commands.txt";
    std::vector<std::string> commands(MAX_COMMANDS);
    std::vector<int> line_numbers(MAX_COMMANDS);
    int num_commands = 0;
    int i, selected_line;
    std::ifstream fp;
    
    // Open the commands file for reading
    fp.open(filename);
    if (!fp.is_open()) {
        std::cerr << "Error: could not open file " << filename << std::endl;
        exit(1);
    }
    
    // Read the commands into the commands vector
    std::string line;
    while (std::getline(fp, line)) {
        commands[num_commands] = line;
        line_numbers[num_commands] = num_commands + 1; // Store the line number
        num_commands++;
    }
    
    // Close the commands file
    fp.close();
    
    // Print the available commands and their line numbers
    std::cout << "Available commands:" << std::endl;
    for (i = 0; i < num_commands; i++) {
        std::cout << line_numbers[i] << ". " << commands[i] << std::endl;
    }
    
    // Prompt the user to select a command
    std::cout << "Enter the line number of the command you want to run: ";
    std::cin >> selected_line;
    
    // Check if the selected line number is valid
    if (selected_line < 1 || selected_line > num_commands) {
        std::cerr << "Error: invalid line number" << std::endl;
        exit(1);
    }
    
    // Execute the selected command
    std::cout << "Running command: " << commands[selected_line - 1] << std::endl;
    system(commands[selected_line - 1].c_str());
    
    return 0;
}
