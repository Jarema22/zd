def get_todos(filepath='/home/stranger/Documents/python/app1/Web App/.venv/todos.txt'):
    with open('/home/stranger/Documents/python/app1/Web App/.venv/todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
def write_todos(todose_arg, filepath='/home/stranger/Documents/python/app1/Web App/.venv/todos.txt',):
    with open(filepath, "w") as file:
        file.writelines(todose_arg)