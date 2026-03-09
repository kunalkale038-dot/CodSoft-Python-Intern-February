# TO-DO LIST APPLICATION (CODSOFT TASK 1)

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def update_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to update: "))
        if 1 <= task_no <= len(tasks):
            new_task = input("Enter new task: ")
            tasks[task_no - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

def delete_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

while True:
    print("\n----- TO-DO LIST MENU -----")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List App.")
        break
    else:
        print("Invalid choice. Try again.")
