# to do list
import json
# RESET = "\033[0m"
# BOLD = "\033[1m"
# ITALIC = "\033[3m"
# GREEN = "\033[92m"
# RED = "\033[91m"
# CYAN = "\033[96m"
# YELLOW = "\033[93m"
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()
while True:
    print("\n1. View Tasks")
    print("2. Add Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = int(input("Choose any one "))
    if choice == 1:
            if not tasks:
                print("\n No Task Founded")
            else:
                print(f"\n---- YOUR TASKS ----")
                for task in tasks:
                    status_symbol = "[Finished]" if task["Status"] else "[Unfinished]"
                    print(f"{task['id']}. {status_symbol} {task['title']}")            
    elif choice == 2:
            title = input("Add task Name ")
            new_id = len(tasks) + 1
            new_task = {
                "id": new_id,
                "title": title,
                "Status": False
            }
            tasks.append(new_task)
            save_tasks(tasks)
            print(f"Task '{title}' has been added")
    elif choice == 3:
        if not tasks:
            print("No tasks Avaialble to Complete!")
        else:
            target_id = int(input("Enter Task ID to Complete "))
            found = False
            for task in tasks:
                if task['id'] == target_id:
                    task['Status'] = True
                    save_tasks(tasks)
                    print(f"task {task['title']} has been marked Completed")
                    found = True
                    break
            if not found:
                print("task not found")    
    elif choice == 4:
        if not tasks:
            print("No tasks available to delete!")
        else:
            try:
                target_id = int(input("Enter Task ID to Delete: "))
                updated_tasks = []
                found = False

                for task in tasks:
                    if task['id'] == target_id:
                        found = True
                    else:
                        updated_tasks.append(task)

                if found:
                    # RENUMBER ALL REMAINING TASKS (1, 2, 3...)
                    for index, task in enumerate(updated_tasks, start=1):
                        task['id'] = index

                    tasks = updated_tasks
                    save_tasks(tasks)
                    print("Task deleted successfully!")
                else:
                    print("Task ID not found!")
            except ValueError:
                print("Please enter a valid number ID.")




    elif choice == 5:
        print("Exiting Program....")
        break
    else: 
        print("Only Select a Number from 1 to 5")