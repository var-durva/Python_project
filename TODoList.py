from datetime import datetime

class ToDoList:
    def __init__(self, id: int, title: str, description: str, created_at: datetime = None,
                 updated_at:datetime = None):
        self.id = id
        self.title = title
        self.description = description
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def __repr__(self):
        return (f"\nToDoList(\n"
         f"  id: {self.id}\n"
         f"  title: {self.title}\n"
         f"  description: {self.description}\n"
         f"  created_at: {self.created_at}\n"
         f"  updated_at: {self.updated_at}\n)")


def testingtask():
        ToDoTest = []
        num = int(input("Enter number of task you want to add: "))
        for i in range(1, num+1):
            title = input(f"Enter title for task {i}: ").strip().capitalize()
            description = input(f"Enter description for task {i}: ").strip().capitalize()
            todo = ToDoList(i, title, description)
            ToDoTest.append(todo)

        try:
            counter = num + 1
            while True:
                choice = int(input("Do you want to be 1 - Add\n2 - Update\n3 - Delete\n4 - Search\n5 - exit/close: "))
                if choice == 1:
                    add_title = input(f"Enter title for task {counter}: ").strip().capitalize()
                    add_description = input(f"Enter description for task {counter}: ").strip().capitalize()
                    todoAdd = ToDoList(counter, add_title, add_description)
                    ToDoTest.append(todoAdd)
                    counter+=1
                    print(f"Task {add_title} with {add_description} description added successfully.")
                    # print(ToDoTest)
                elif choice == 2:
                    task_update_id = int(input("Enter the task id: "))
                    for task in ToDoTest:
                        if task.id == task_update_id:
                            task.title = input(f"Enter updated title for task {task_update_id}: ").strip().capitalize()
                            task.description = input(f"Enter updated description for task {task_update_id}: ").strip().capitalize()
                            task.updated_at = datetime.now()
                            print(f"The task {task_update_id} updated successfully.")
                            # print(ToDoTest)
                            break
                    else:
                        print(f"The task {task_update_id} is not found.")
                elif choice == 3:
                    task_delete_id = int(input("Enter task id to delete: "))
                    for task in ToDoTest:
                        if task.id == task_delete_id:
                            ToDoTest.remove(task)
                            print(f"The task {task_delete_id} deleted successfully.")
                            break
                    else:
                        print(f"The task {task_delete_id} is not found.")
                elif choice == 4:
                    keyword = input("Enter the keyword, you want to search: ").strip().lower()
                    found = False
                    for task in ToDoTest:
                        if keyword in task.title.lower() or keyword in task.description.lower():
                            print(f"Found {keyword} is in the {task}.")
                            found = True
                    if not found:
                        print(f"The {keyword} is not found in the task(s).")
                elif choice == 5:
                    print("Please close the program, I made todo list.")
                    break
                else:
                    print(f"You have entered the invalid choice {choice}, please enter the between 1 to 5.")
        except (ValueError,TypeError) as e:
                print(f"Error: {e}")

        for idx, task in enumerate(ToDoTest, start=1):
            print(f"----The task{idx}----")
            print(task)

testingtask()


