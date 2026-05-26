from models import Task


class TaskService:
    VALID_PRIORITIES = {"low", "medium", "high"}

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title: str, priority: str = "medium", due_date: str | None = None) -> Task:
        if priority not in self.VALID_PRIORITIES:
            raise ValueError(f"Invalid priority: {priority}")

        task = Task(
            id=self.next_id,
            title=title,
            priority=priority,
            completed=False,
            due_date=due_date,
        )
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self, status: str = "all"):
        if status == "completed":
            return [task for task in self.tasks if task.completed]
        if status == "pending":
            return [task for task in self.tasks if not task.completed]
        return self.tasks

    def search_tasks(self, keyword: str):
        keyword = keyword.lower().strip()
        return [task for task in self.tasks if keyword in task.title.lower()]

    def complete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return True
        return False

    # Intentional bug retained for Day 1 debugging demo
    def delete_task(self, task_id: int) -> bool:
        for index, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[index]
        return False

    def summary(self) -> dict:
        completed = sum(1 for task in self.tasks if task.completed)
        pending = sum(1 for task in self.tasks if not task.completed)
        return {
            "total": len(self.tasks),
            "completed": completed,
            "pending": pending,
        }