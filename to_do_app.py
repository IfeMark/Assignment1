tasks =  [] 
print("Welcome to the to-do app")
def to_do_list():
    while True:
        print("Please select from the menu below")
        print("Menu: ")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. View tasks")
        print("4. Quit")
                    
        def Add_new_task():
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task '{task}' has been added successfully")
        
        def list_of_tasks():
            if not tasks :
                print("There is no current task")
            else:
                print("Tasks: ")
                for index, task in enumerate(tasks):
                    print(f"Task no {index}. {task} ")
                    
        def Delete_task():
            list_of_tasks()
            try:
                task_to_delete = int(input("Enter the task no. to delete: "))
                if task_to_delete >= 0 and task_to_delete < len(tasks):
                    tasks.pop(task_to_delete)
                    print(f'Task {task_to_delete} has been deleted')
                else:
                    print(f'Task {task_to_delete} was not included')
            except:
                print("Invalid input")
        
        choice = input("Enter your selection: ")
        if choice == "1":
            Add_new_task()
        elif choice == "2":
            Delete_task()
        elif choice == "3":
            list_of_tasks()
        elif choice == "4":
            print("To do app has ended")
            break
        else:
            print("Invalid input. Please try again")
        
to_do_list()

with open('full_list.txt','w') as f:
    print("Tasks: \n")
    for a in tasks:
        f.write(a + '\n')
        print(a)
        