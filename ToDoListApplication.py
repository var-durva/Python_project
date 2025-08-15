def task():
    tasks = [] #Empty list
    print("--WELCOME TO THE TASK MANAGEMENT APP----")

    total_task = int(input("Enter how many task you want to add = "))
    for i in range(1, total_task +1):
        task_name = input(f"Enter task {i} = ").strip().capitalize()
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit/Stop\n: "))
        if operation == 1: #Add
            add = input("Enter task you want to add = ").strip().capitalize()
            tasks.append(add)
            print(f"Task {add} has been successfully added.")
        elif operation == 2: #Update
            updated_val = input("Enter the task name you want to update= ").strip().capitalize()
            if updated_val in tasks:
                up = input("Enter new task = ").capitalize()
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task {updated_val} to {up}")
        elif operation == 3: #delete
            del_value = input("Enter which value you want to delete= ").strip().capitalize()
            if del_value in tasks:
                tasks.remove(del_value)
                print(f"Task {del_value} has been deleted.")
            else:
                print("Task not found.")
        elif operation == 4: #view
            if tasks:
                print(f"Total tasks: {tasks}")
            else:
                print("No taska available.")
        elif operation == 5: #close
            print("Close the program.")
            break
        else:
            print("Invalid input. please enter 1-5")

task()
