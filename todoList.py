user_task_title = input("Enter a task to complete: ")
user_priority = input("Each task enter will have a priority level. Ranking from Low, Medium or High. Please enter 'L' for Low, 'M for Medium or 'H' for High: ")

class ToDo:
    def __init__(self,user_task_title, user_priority, to_do_list, task_count):
        self.user_task_title = user_task_title
        self.user_priority = user_priority
        self.to_do_list = []
        self.task_count = 0

    def add_task(self):
        pass

    def view_task(self):
        self.task_count += 1
        pass

    def completed_task(self):
        pass

    def remove_task(self):
        pass
