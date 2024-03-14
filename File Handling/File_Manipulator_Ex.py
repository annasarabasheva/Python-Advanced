import os
root_path = os.path.dirname(os.path.abspath(__file__))
while True:
    line = input()
    if line == "End":
        break
    command_arg = line.split('-')
    command = command_arg[0]
    file_name = command_arg[1]
    if command == "Create":
        file_path = os.path.join(root_path, file_name)
        with open(file_path, "w") as file:
            pass
    elif command == "Add":
        content = command_arg[2]
        if os.path.exists(file_name):
            with open(file_name, "a") as file:
                file.write(f"{content}\n")
        else:
            file_path = os.path.join(root_path, file_name)
            with open(file_path, "a") as file:
                file.write(f"{content}\n")
    elif command == "Replace":
        old_string = command_arg[2]
        new_string = command_arg[3]
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                file_data = file.read()
                file_data = file_data.replace(old_string, new_string)
            with open(file_name, 'w') as file:
                file.write(file_data)
        else:
            print("An error occurred")
            continue
    elif command == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")