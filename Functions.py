FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):      # filepath is an argument  # custom function to avoid repetition
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()  # local variable as there is already a global variable
    return todos_local


def write_todos(todos_arg, filepath = FILEPATH):
    with open(filepath, 'w') as file:
            file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())