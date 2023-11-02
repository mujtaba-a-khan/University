import json

# Function to load tasks from a file
def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks

# Function to save tasks to a file
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(tasks, title, description):
    task = {'title': title, 'description': description, 'completed': False}
    tasks.append(task)

# Function to view tasks
def view_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{i}. Title: {task['title']} (Status: {status})")
        print(f"   Description: {task['description']}")

# Function to mark a task as completed
def mark_completed(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True

# Function to edit a task
def edit_task(tasks, task_number, new_title, new_description):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['title'] = new_title
        tasks[task_number - 1]['description'] = new_description

# Function to remove a task
def remove_task(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]

def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)

    while True:
        print("\nWelcome to the To-Do List Application!\n")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as completed")
        print("4. Edit a task")
        print("5. Remove a task")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Title: ")
            description = input("Description: ")
            add_task(tasks, title, description)
        elif choice == '2':
            print("Tasks:")
            view_tasks(tasks)
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_completed(tasks, task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to edit: "))
            new_title = input("New Title: ")
            new_description = input("New Description: ")
            edit_task(tasks, task_number, new_title, new_description)
        elif choice == '5':
            task_number = int(input("Enter the task number to remove: "))
            remove_task(tasks, task_number)
        elif choice == '6':
            print("Goodbye!")
            save_tasks(filename, tasks)
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()