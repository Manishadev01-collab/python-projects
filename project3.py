# Load existing items 
# 1 . Create a new item 
# 2 . list items 
# 3. mark item as complete 
# 4 . save items 
# TO DO List Management app

# The central list to store our tasks. We'll use dictionaries for tasks
# so we can track both the description and if it's completed.
tasks = []

def load_tasks():
    """Placeholder: In a real app, this would load tasks from a file."""
    global tasks
    return tasks

def save_tasks():
    """Placeholder: In a real app, this would save tasks to a file."""
    pass

def view_tasks():
    """Displays all tasks with their index and completion status."""
    global tasks
    if not tasks:
        print("\nYour to-do list is empty! 🥳")
        return

    print("\n--- Current To-Do Tasks ---")
    for index, task in enumerate(tasks, 1):
        status = "[DONE]" if task.get("completed") else "[PENDING]"
        print(f"{index}. {status} {task['description']}")
    print("---------------------------")

def create_task():
    """Prompts for a new task and adds it to the list."""
    global tasks
    description = input("Enter the new task description: ").strip()
    if description:
        # Task dictionary format: {"description": "...", "completed": False}
        tasks.append({"description": description, "completed": False})
        print(f"✅ Task '{description}' added successfully.")
    else:
        print("❌ Task description cannot be empty.")

def mark_task_complete():
    """Allows the user to mark a task as complete by its number."""
    global tasks
    if not tasks:
        print("No tasks to mark complete.")
        return

    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to mark complete: ").strip())
        task_index = task_num - 1 # Convert to 0-based index

        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print(f"✅ Task '{tasks[task_index]['description']}' marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")


def main():
    """The main application loop."""
    global tasks
    tasks = load_tasks() # Initialize the tasks list

    while True:
        # The menu, input, and decision logic MUST be inside the loop
        print("\n=== To - Do List Manager ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Complete") # Corrected menu option
        print("4. Exit")
        print("============================")

        # The input prompt is now correctly indented inside the loop
        choice = input("Enter your choice:").strip()

        if choice == "1":
            view_tasks() # Used the corrected snake_case function name
        elif choice == "2":
            create_task()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            save_tasks()
            print("Goodbye! 👋")
            # The 'break' is now correctly indented inside the 'elif' block
            break
        else:
            print("Invalid choice. please try again.")


# Standard way to start the application
if __name__ == "__main__":
    main()