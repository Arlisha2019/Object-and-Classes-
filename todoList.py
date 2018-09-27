import json

tasks = []

def display_all_tasks():
    for t in tasks:
        print(t["task_id"], ".", t["title"], " ", t["priority"])

class Task:
    def __init__(self,title, priority):
        self.title = title
        self.isCompleted = False
        self.priority = priority
        self.task_id = len(tasks) + 1

    def jsonDictionary(self):
        return self.__dict__

while True:

    title = input("Enter a task to complete, 'N' to quit or 'R' to remove a task: ")

    if(title == "n"):
        print("Your current Task List consist of the following:")
        display_all_tasks()
        print("Thank you for using our application!!")
        break
    elif(title == "r"):
        display_all_tasks()
        remove_id = (input("Please enter the number of th task you want to remove or 'N' to quit: "))
        if remove_id == "n":
            print("Thank you for you time please review your task list below:")
            display_all_tasks()
            break
        else:
            print("Deleting a task .....")
            del tasks[int(remove_id) - 1]
            display_all_tasks()
    else:
        priority = input("Please enter 'L' for Low, 'M for Medium, 'H' for High: ")


    task = Task(title,priority)
    # adding a dictionary to tasks array

    tasks.append(task.jsonDictionary())

with open("task.json", "w") as task_file_data:
    json.dump(tasks,task_file_data)

with open("task.json", "r") as task_file_data:
    task_info = json.load(task_file_data)
    print(task_info)

















#tasks.append(task)
