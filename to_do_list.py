import datetime

# Coded by Gönenç Barış Bezik 

def write(task, category):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_task = f"[{category}] {task} (added on {timestamp})"

    with open("to_do_list.txt", "a") as file:
        file.write(formatted_task + "\n")

def read():
    with open("to_do_list.txt", "r") as file:
        return [line.strip() for line in file.readlines()]

def delete(task_keyword):
    tasks = read()
    matching_tasks = [t for t in tasks if task_keyword.lower() in t.lower()]

    if not matching_tasks:
        print(f"No task found containing '{task_keyword}'.")
        return

    print("\nMatching tasks:")

    for i, t in enumerate(matching_tasks, start=1):
        print(f"{i}. {t}")

    try:
        choice = int(input("Enter the number of the task to delete: "))
        selected_task = matching_tasks[choice - 1]
        tasks.remove(selected_task)

        with open("to_do_list.txt", "w") as file:
            for t in tasks:
                file.write(t + "\n")
        print(f"Task '{selected_task}' has been deleted.")

    except (ValueError, IndexError):
        print("Invalid choice. Deletion cancelled.")

def clear_all_tasks():
    with open("to_do_list.txt", "w") as file:
        file.write("")

    print("All tasks have been cleared.")

def view_tasks():
    tasks = read()

    if tasks:
        print("\nTo-Do List:")

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the list.")

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task (with keyword match)")
    print("4. Clear All Tasks")
    print("5. Show Menu")
    print("6. Exit")

def main():
    show_menu()

    while True:

        try:
            operation = int(input("\nEnter your operation number (1-6): "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        if operation == 1:
            task = input("Enter the task: ")
            category = input("Enter category or priority (e.g., Work, Urgent, Low): ")
            write(task, category)
            print(f"Task '{task}' added under '{category}' category.")

        elif operation == 2:
            view_tasks()

        elif operation == 3:
            keyword = input("Enter keyword to find the task to delete: ")
            delete(keyword)

        elif operation == 4:
            confirm = input("Are you sure you want to delete all tasks? (yes/no): ").lower()

            if confirm == "yes":
                clear_all_tasks()
            else:
                print("Operation cancelled.")

        elif operation == 5:
            show_menu()

        elif operation == 6:
            print("Have a great time completing your tasks!")
            break

        else:
            print("The entered operation number is out of range. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
