tasks = []

def show_menu():
    """Display the menu options"""
    print("\n--- To-Do List Menu ---")
    print("1. Add task")
    print("2. Remove task")
    print("3. Edit task")
    print("4. View tasks")
    print("5. Exit")

def view_tasks():
    """Display all tasks in a numbered format"""
    if tasks:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")
    else:
        print("\nNo tasks yet. Add one to get started!")

def add_task():
    """Add a new task to the list"""
    task = input("Enter your task: ").strip()
    if task:
        tasks.append(task)
        print("✓ Task added successfully!")
    else:
        print("✗ Task cannot be empty")

def remove_task():
    """Remove a task by number"""
    view_tasks()
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to remove: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"✓ Task removed: {removed}")
        else:
            print("✗ Invalid task number")
    except ValueError:
        print("✗ Please enter a valid number")

def edit_task():
    """Edit an existing task by number"""
    view_tasks()
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to edit: ")) - 1
        if 0 <= idx < len(tasks):
            print(f"Current task: {tasks[idx]}")
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks[idx] = new_task
                print("✓ Task updated successfully!")
            else:
                print("✗ Task cannot be empty")
        else:
            print("✗ Invalid task number")
    except ValueError:
        print("✗ Please enter a valid number")

def ToDoList():
    """Main function to run the to-do list application"""
    print("Welcome to your To-Do List!")
    
    while True:
        show_menu()
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("✗ Please enter a valid number (1-5)")
            continue

        if choice == 1:
            add_task()
        elif choice == 2:
            remove_task()
        elif choice == 3:
            edit_task()
        elif choice == 4:
            view_tasks()
        elif choice == 5:
            print("\nGoodbye! Your tasks have not been saved.")
            break
        else:
            print("✗ Invalid choice. Please enter a number between 1-5")

ToDoList()
