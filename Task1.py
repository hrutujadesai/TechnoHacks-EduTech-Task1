todo_list = []


def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")


def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed from the to-do list.")
    else:
        print(f"Task '{task}' not found in the to-do list.")


def display_tasks():
    if todo_list:
        print("\nCurrent To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    else:
        print("\nYour to-do list is empty.")


while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Quit")


    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter the task to add: ")
        add_task(task)
        
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
        
    elif choice == "3":
        display_tasks()
        
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")
