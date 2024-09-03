import datetime
import time
import threading

class Task:
    def __init__(self, name: str, due_date: str = None, reminder: str = None):
        self.name = name
        self.due_date = due_date
        self.reminder = reminder
        self.completed = False

class TodoApp:
    def __init__(self):
        self.tasks = []

    def create_task(self, task_name: str, due_date: str = None, reminder: str = None):
        task = Task(task_name, due_date, reminder)
        self.tasks.append(task)
        print(f"Task '{task_name}' created successfully!")

    def update_task(self, task_index: int, new_task_name: str = None, due_date: str = None, reminder: str = None):
        if task_index < len(self.tasks):
            task = self.tasks[task_index]
            if new_task_name:
                task.name = new_task_name
            if due_date:
                task.due_date = due_date
            if reminder:
                task.reminder = reminder
            print(f"Task '{task.name}' updated successfully!")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index: int):
        if task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully!")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        print("\nYour To-do List:")
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Not Completed"
            due_date = task.due_date if task.due_date else "No Due Date"
            reminder = task.reminder if task.reminder else "No Reminder"
            print(f"{i}. {task.name} - {status} - Due Date: {due_date} - Reminder: {reminder}")

class ReminderService:
    def __init__(self, todo_app: TodoApp):
        self.todo_app = todo_app
        self.reminders = []

    def set_reminder(self, task_index: int, reminder_time: str):
        if task_index < len(self.todo_app.tasks):
            task = self.todo_app.tasks[task_index]
            task.reminder = reminder_time
            self.reminders.append((task_index, reminder_time))
            print(f"Reminder set for task '{task.name}' at {reminder_time}!")
        else:
            print("Invalid task index.")

    def check_reminders(self):
        while True:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            for task_index, reminder_time in list(self.reminders):  # Use list() to avoid runtime errors due to removal
                if current_time >= reminder_time:
                    task = self.todo_app.tasks[task_index]
                    print(f"Reminder: Task '{task.name}' is due!")
                    self.reminders.remove((task_index, reminder_time))
            time.sleep(60)

class CommandLineInterface:
    def __init__(self, todo_app: TodoApp, reminder_service: ReminderService):
        self.todo_app = todo_app
        self.reminder_service = reminder_service

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Create Task")
            print("2. Update Task")
            print("3. Delete Task")
            print("4. Display Tasks")
            print("5. Complete Task")
            print("6. Set Reminder")
            print("7. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                task_name = input("Enter task name: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
                reminder = input("Enter reminder time (YYYY-MM-DD HH:MM): ")
                self.todo_app.create_task(task_name, due_date, reminder)
            elif choice == "2":
                task_index = int(input("Enter task index to update: ")) - 1
                new_task_name = input("Enter new task name: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
                reminder = input("Enter reminder time (YYYY-MM-DD HH:MM): ")
                self.todo_app.update_task(task_index, new_task_name, due_date, reminder)
            elif choice == "3":
                task_index = int(input("Enter task index to delete: ")) - 1
                self.todo_app.delete_task(task_index)
            elif choice == "4":
                self.todo_app.display_tasks()
            elif choice == "5":
                task_index = int(input("Enter task index to complete: ")) - 1
                if 0 <= task_index < len(self.todo_app.tasks):
                    self.todo_app.tasks[task_index].completed = True
                    print(f"Task '{self.todo_app.tasks[task_index].name}' marked as completed!")
                else:
                    print("Invalid task index.")
            elif choice == "6":
                task_index = int(input("Enter task index to set reminder: ")) - 1
                reminder_time = input("Enter reminder time (YYYY-MM-DD HH:MM): ")
                self.reminder_service.set_reminder(task_index, reminder_time)
            elif choice == "7":
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_app = TodoApp()
    reminder_service = ReminderService(todo_app)

    # Start the reminder check in a separate thread
    reminder_thread = threading.Thread(target=reminder_service.check_reminders, daemon=True)
    reminder_thread.start()

    cli = CommandLineInterface(todo_app, reminder_service)
    cli.run()
