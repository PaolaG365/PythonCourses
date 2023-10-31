from typing import List
from task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task_instance in self.tasks:
            if task_name == task_instance.name:
                task_instance.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        cleared_tasks = 0
        for task_instance in self.tasks:
            if task_instance.completed:
                self.tasks.remove(task_instance)
                cleared_tasks += 1
        return f"Cleared {cleared_tasks} tasks."

    def view_section(self):
        info_section = [f"Section {self.name}:"]
        [info_section.append(f"{task_obj.details()}") for task_obj in self.tasks]
        return "\n".join(info_section)


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
