to_do_list = []
def add_task():
    task = input("Enter the task: ")
    to_do_list.append(task)
def remove_task():
    task = input("Enter task to remove: ")
    to_do_list.remove(task)
def show_all_tasks():
    print("Your tasks: ")
    for task in to_do_list:
        print(f" * {task}")  
while True:
    action = input("choose action: add, remove, show, exit: ").lower()
    if action == 'add':
        add_task()
    elif action == 'remove':
        remove_task()
    elif action == 'show':
        show_all_tasks()
    elif action  == 'exit':
        break
    else:
        print("invalid action")