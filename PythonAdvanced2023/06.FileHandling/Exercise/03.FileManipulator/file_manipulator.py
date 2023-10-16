import os


def file_creator(file_name):
    with open(file_name, "w"):
        pass


def add_content(file_name, new_content):
    with open(file_name, "a") as work_file:
        work_file.writelines(new_content + "\n")


def replace_content(file_name, *info):
    try:
        with open(file_name, "r+") as work_file:
            content_file = work_file.read()
            work_file.seek(0)
            work_file.writelines(content_file.replace(info[0], info[1]))

    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


commands_map = {
    "Create": file_creator,
    "Add": add_content,
    "Replace": replace_content,
    "Delete": delete_file,
}

command = input()
while command != "End":
    command = command.split("-")
    try:
        commands_map[command[0]](*command[1:])
    except KeyError:
        print("Invalid input. Try another command!")
    command = input()
