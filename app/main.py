def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp" or parts[1] == parts[2]:
        print("Data isn't correct,"
              " please enter other"
              " name command or other names files")
    else:
        content = []
        with open(parts[1], "r") as file_data:
            content = file_data.read()
        with open(parts[2], "w") as file_copy:
            file_copy.write(content)
