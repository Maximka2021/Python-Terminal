import os

list_of_commands = ["s or stop", "gi or go_inside", "go or go_outside", "gl or give_list", "h or help", "c or clear", "nf or new_file"]


def clear_console():
    print("\n" * 50)


def give_list():
    for file in os.scandir(os.getcwd()):
        print(file.name)


def show_commands():
    print(f"{list_of_commands[0]} => exit console \n"
          f"{list_of_commands[1]} => go inside of a folder \n"
          f"{list_of_commands[2]} => go outside of a folder \n"
          f"{list_of_commands[3]} => show list of files in folder \n"
          f"{list_of_commands[4]} => show list of console commands \n"
          f"{list_of_commands[5]} => clear console \n"
          f"{list_of_commands[6]} => create new txt file \n"
          )


def go_inside(command):
    try:
        if os.path.exists(command[1]):
            os.chdir(f"{os.getcwd()}/{command[1]}")
        else:
            print(f"Folder \"{command[1]}\" not found in {os.getcwd()}")
    except IndexError:
        print("You need to specify the folder you want to go in")


def go_outside():
    cur_dir = os.path.abspath('.')
    parent_dir = os.path.dirname(cur_dir)
    os.chdir(parent_dir)


def open_file(file):
    try:
        with open(file, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"{file} was not found")


def create_file(command):
    new_list = command[1:len(command)]
    file_name = '_'.join(new_list)
    try:
        file = open(f"{file_name}.txt", 'x')
        file.close()
    except FileExistsError:
        print(f"File {file_name} is already exists in this directory")


def delete_file(command):
    new_list = command[1:len(command)]
    file_name = '_'.join(new_list)
    if os.path.isfile(f"{os.getcwd()}/{file_name}.txt"):
        os.remove(f"{os.getcwd()}/{file_name}.txt")
    else:
        print(f"File {file_name} does not exists")


