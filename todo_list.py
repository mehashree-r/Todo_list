todo_list = []

def show_menu():
    print("\n TO-DO List OPtions:")
    print("1.View Tasks")
    print("2.Add Tasks")
    print("3.Remove Tasks")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks yet")
    else:
        print("\n Your tasks:")
        for idx,task in enumerate(todo_list,start=1):
            print(f"{idx}.{task}")
                  
def add_task():
   task = input("Enter the task:")
   todo-list.append(task)
   print("task added")

def remove_task():
    view_task()
    try:
        index = int(input("Enter task number to remove:")) - 1
        removed = todo_list.pop(index)
        print(f"Removed:{removed}")
    except (valueError,IndexError):
        print("Invalid task number.")

    while True:
        show_menu()
        choice = input("choose an option (1-4):" )
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye")
            break
        else:
           print("Invalid option.please choose 1-4.")