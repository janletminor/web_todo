def get_todos(filepath="files/todos.txt", mode='r'):
    """ Read a text file and return the list of to-do items.
    Default values for filepath="default.txt" and mode="r" for read
    read_file function returns the to-do lines
    """
    with open(filepath, mode) as text_file:
        return text_file.readlines()


def write_todos(todos_arg, filepath="files/todos.txt", mode='w'):
    """ Read a text file and return the list of to-do items.
    Default values for filepath="default.txt" and mode="w" for write
    write_file function does not return any values
    """
    with open(filepath, mode) as text_file:
        text_file.writelines(todos_arg)
