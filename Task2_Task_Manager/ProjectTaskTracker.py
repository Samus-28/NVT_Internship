from datetime import datetime

tasks = []

def add_task():
    print("\n-- Add a New Task --")
    project = input("Enter project name: ")
    desc = input("Enter task details: ")
    while True:
        deadline_input = input("Set deadline (DD-MM-YYYY): ")
        try:
            deadline = datetime.strptime(deadline_input, "%d-%m-%Y")
            if deadline <= datetime.now():
                print("Deadline must be a future date.")
            else:
                break
        except ValueError:
            print("Invalid format. Use DD-MM-YYYY.")
    
    tasks.append({
        "project": project,
        "desc": desc,
        "deadline": deadline.strftime("%d-%m-%Y"),
        "status": "Pending",
        "created": datetime.now().strftime("%d-%m-%Y")
    })
    print("✔ Task successfully added!\n")

def view_tasks(status_filter=None):
    print("\n-- Task List --")
    listed = [t for t in tasks if not status_filter or t['status'] == status_filter]
    if not listed:
        print("No tasks match your criteria.\n")
        return
    for i, t in enumerate(listed, 1):
        print(f"{i}) {t['project']} - {t['desc']} [{t['status']}]")
        print(f"   ➤ Deadline: {t['deadline']} | Created on: {t['created']}")
    print()

def complete_task():
    pending = [i for i, t in enumerate(tasks) if t['status'] == "Pending"]
    if not pending:
        print("All tasks are already completed!\n")
        return
    view_tasks("Pending")
    try:
        choice = int(input("Enter task number to complete: ")) - 1
        tasks[pending[choice]]['status'] = "Completed"
        print("✔ Task marked as completed.\n")
    except:
        print("Invalid selection.\n")

def delete_task():
    if not tasks:
        print("Task list is empty.\n")
        return
    view_tasks()
    try:
        choice = int(input("Choose task number to delete: ")) - 1
        removed = tasks.pop(choice)
        print(f"Deleted task: {removed['desc']}\n")
    except:
        print("Invalid input.\n")

def edit_task():
    if not tasks:
        print("No tasks available to edit.\n")
        return
    view_tasks()
    try:
        idx = int(input("Task number to edit: ")) - 1
        task = tasks[idx]
        task['project'] = input(f"New project name ({task['project']}): ") or task['project']
        task['desc'] = input(f"New description ({task['desc']}): ") or task['desc']
        print("✔ Task updated.\n")
    except:
        print("Invalid selection.\n")

def sort_by_deadline():
    if not tasks:
        print("No tasks to sort.\n")
        return
    tasks.sort(key=lambda t: datetime.strptime(t['deadline'], "%d-%m-%Y"))
    print("Tasks sorted by deadline.\n")
    view_tasks()

def main():
    while True:
        print("\n====== Simple Task Manager ======")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. View Pending Only")
        print("4. View Completed Only")
        print("5. Mark as Completed")
        print("6. Delete Task")
        print("7. Edit Task")
        print("8. Sort by Deadline")
        print("9. Exit")
        print("=" * 35)

        choice = input("Choose an option (1-9): ").strip()
        if choice == '1': add_task()
        elif choice == '2': view_tasks()
        elif choice == '3': view_tasks("Pending")
        elif choice == '4': view_tasks("Completed")
        elif choice == '5': complete_task()
        elif choice == '6': delete_task()
        elif choice == '7': edit_task()
        elif choice == '8': sort_by_deadline()
        elif choice == '9':
            print("Exiting... Goodbye!\n")
            break
        else:
            print("Invalid option. Try again.\n")

main()
