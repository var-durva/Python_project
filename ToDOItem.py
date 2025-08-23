from datetime import datetime

class ToDoItem:
    def __init__(self, id: int, task_title: str, task_description: str,
                 created_at:datetime=None, updated_at:datetime=None):
        self.id = id
        self.task_title = task_title
        self.task_description = task_description
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def __repr__(self):
        return(f"ToDoItem(id: {self.id}\n"
               f", task_title: {self.task_title}\n"
               f" task_description: {self.task_description}\n"
               f"created_time: {self.created_at}\n"
               f"updated_time : {self.updated_at}\n")

ToDoList = []

num_task = int(input("Enter number of task you want to enter: "))

for i in range(1, num_task+1):
    print(f"\n --- Task {i} ---")
    task_title = input("Enter task title you want to do: ")
    task_description = input("Enter task description you want to mention: ")
    ToDo= ToDoItem(i, task_title, task_description)
    ToDoList.append(ToDo)

print("\nYour To-Do List:")
for task in ToDoList:
    print(task)
    print("-" * 40)  # Separator line



