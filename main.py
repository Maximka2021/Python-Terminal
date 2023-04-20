import os
from methods import *
user_input: str = ""
command = []
valid_commands = ["s", "stop", "gi", "go_inside", "go", "go_outside", "gl", "give_list", "h", "help", "c", "clear", "o", "open", "new_file", "nf", "d", "delete"]
print("Type h or help to see list of console commands")

while user_input != "s" or user_input != "stop":
    user_input = input(f"{os.getcwd()} => ")
    command = user_input.split()
    if len(command) == 0:
        continue
    if user_input == "s" or user_input == "stop":
        break
    if command[0] not in valid_commands:
        print(f"{command[0]} was not found")
        print("Type h or help to see list of console commands")
    if command[0] == "go_inside" or command[0] == "gi":
        go_inside(command)
    if command[0] == "go_outside" or command[0] == "go":
        if len(command) == 1:
            go_outside()
        else:
            print(f"{' '.join(command)} was not found")
    if command[0] == "give_list" or command[0] == "gl":
        give_list()
    if command[0] == "open" or command[0] == "o":
        open_file(command[1])
    if command[0] == "help" or command[0] == "h":
        show_commands()
    if command[0] == "clear" or command[0] == "c":
        if len(command) == 1:
            clear_console()
        else:
            print(f"{' '.join(command)} was not found")
    if command[0] == "new_file" or command[0] == "nf":
        if len(command) == 1:
            print("Please specify name of the file")
        else:
            create_file(command)
    if command[0] == "d" or command[0] == "delete":
        if len(command) == 1:
            print("Please specify name of the file")
        else:
            delete_file(command)





