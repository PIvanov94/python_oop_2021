class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        try:
            task = [t for t in self.tasks if t.name == task_name][0]
            task.completed = True
            return f"Completed task {task_name}"
        except IndexError:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        not_completed_tasks = [t for t in self.tasks if not t.completed]
        n_removed_tasks = len(self.tasks) - len(not_completed_tasks)
        self.tasks = not_completed_tasks
        return f"Cleared {n_removed_tasks} tasks."

    def view_section(self):
        data = f"Section {self.name}:\n"
        for task in self.tasks:
            data += task.details() + "\n"
        return data
