from Excercises.P05_to_do_list.task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for section_task in self.tasks:
            if section_task.name == new_task.name:
                return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        cleaned_tasks = 0
        for task in self.tasks:
            if task.completed:
                cleaned_tasks += 1
                self.tasks.pop(task)
        return f"Cleared {cleaned_tasks} tasks."

    def view_section(self):
        result = [f'{x.details()}' for x in self.tasks]
        result = '\n'.join(result)
        result = f"Section {self.name}:" + "\n" + f"{result}"
        return result


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
