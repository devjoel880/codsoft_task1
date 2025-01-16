print('Welcome to the Todo List App')
print('All rights reserved, DevJoel 2024')

task_id = 0
tasks = {}

def start():
    while True:
        choice = input('Select an option (create, view, update, exit)').strip().lower()
        if choice == 'create':
            create()
        elif choice == 'view':
            view()
        elif choice == 'update':
            update()
        elif choice == 'exit':
            print('Goodbye!')
            break
        else:
            print('Invalid option')
def create():
    """create new task"""
    global task_id
    task_name = input("Enter task name: ")
    status = input('Enter status: ')
    priority = input('Set priority: ')

    task_id += 1
    tasks[task_id] = {
        "name": task_name,
        "status": status,
        "priority": priority
    }

    print(f'Task created with ID: {task_id}')

def view():
    """view all tasks"""
    if not tasks:
        print('No tasks available')
    else:
        for task_id, task_details in tasks.items():
            print(
                    f"ID: {task_id}, "
                    f"Name: {task_details['name']}, "
                    f"Status: {task_details['status']}, "
                    f"Priority: {task_details['priority']}"
                )
def update():
    """update an existing task"""
    task_id = int(input('Enter the task ID you wish to update: '))
    if task_id in tasks:
        print("Current details:", tasks[task_id])
        task_name = input("Enter new task name (press Enter to skip): ")
        priority = input("Enter new priority (press Enter to skip): ")
        status = input("Enter new status (press Enter to skip): ")

        # Update only if a value is provided
        if task_name:
            tasks[task_id]["name"] = task_name
        if priority:
            tasks[task_id]["priority"] = priority
        if status:
            tasks[task_id]["status"] = status
        print("Task updated successfully.")
    else:
        print("Task ID not found.")

start()
