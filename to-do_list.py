tasks = []

def ToDoList():

    while True:
      
      print("Press 1 to add task")
      print("Press 2 to remove task")
      print("press 3 to edit task")
      print("Press 4 to view tasks")
      print("Press 5 to exit")

      choice = int(input("Enter your choice:"))

      if choice == 1:
          to_do = str(input("Enter your task:"))
          tasks.append(to_do)
          print("Task added")

      elif choice == 2:
          task_to_remove = str(input("Enter task to remove:"))
          if task_to_remove in tasks:
              tasks.remove(task_to_remove)
              print("Task removed")
          else:
              print("Task not found")

      elif choice == 3:
          task_to_edit = str(input("Enter task to edit:"))
          if task_to_edit in tasks:
              idx = tasks.index(task_to_edit)
              edited_task = str(input("Enter new task:"))
              tasks[idx] = edited_task
          else:
              print("Task not found")

      elif choice == 4:
          print("To-do List:", tasks)
          
      elif choice == 5:
          print ("Exited:")
          break
      
      else:
          print("Invalid choice")

ToDoList()
