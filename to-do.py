import datetime  # manipulate date and time
import threading # to run statements simultaneously
 
# define parameters of a task
class Task:
    def __init__(self, name: str, due_date: str = None):
        self.name = name
        self.due_date = due_date
        self.completed = False

# design a to-do application
class TodoApp:
    def __init__(self):
        self.tasks = []

# create task
    def create_task(self, task_name: str, due_date: str = None):
        task = Task(task_name, due_date)
        self.tasks.append(task)
        print(f"Task '{task_name}' created successfully! Don't forget to complete it ")

# update the status of the tasks
    def update_task(self, task_index: int, new_task_name: str = None, due_date: str = None):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            if new_task_name:
                task.name = new_task_name
            if due_date:
                task.due_date = due_date
            print(f"Task '{task.name}' updated successfully!")
        else:
            print("Invalid task index.")

# delete completed tasks
    def delete_task(self, task_index: int):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully!")
        else:
            print("Invalid task index.")

# display on due tasks
    def display_tasks(self):
        print("\nYour To-do List:")
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Not Completed"
            due_date = task.due_date if task.due_date else "No Due Date"
            print(f"{i}. {task.name} - {status} - Due Date: {due_date}")

class CommandLineInterface:
    def __init__(self, todo_app: TodoApp):
        self.todo_app = todo_app

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Create Task")
            print("2. Update Task")
            print("3. Delete Task")
            print("4. Display Tasks")
            print("5. Complete Task")
            print("6. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                task_name = input("Enter task name: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
                self.todo_app.create_task(task_name, due_date)
            elif choice == "2":
                try:
                    task_index = int(input("Enter task index to update: ")) - 1
                    new_task_name = input("Enter new task name: ")
                    due_date = input("Enter due date (YYYY-MM-DD): ")
                    self.todo_app.update_task(task_index, new_task_name, due_date)
                except ValueError:
                    print("Invalid input. Please enter a valid task index.")
            elif choice == "3":
                try:
                    task_index = int(input("Enter task index to delete: ")) - 1
                    self.todo_app.delete_task(task_index)
                except ValueError:
                    print("Invalid input. Please enter a valid task index.")
            elif choice == "4":
                self.todo_app.display_tasks()
            elif choice == "5":
                try:
                    task_index = int(input("Enter task index to complete: ")) - 1
                    if 0 <= task_index < len(self.todo_app.tasks):
                        self.todo_app.tasks[task_index].completed = True
                        print(f"Task '{self.todo_app.tasks[task_index].name}' marked as completed!")
                    else:
                        print("Invalid task index.")
                except ValueError:
                    print("Invalid input. Please enter a valid task index.")
            elif choice == "6":
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_app = TodoApp()
    cli = CommandLineInterface(todo_app)
    cli.run()

