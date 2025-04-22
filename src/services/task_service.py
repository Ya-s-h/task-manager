from mongoengine.errors import DoesNotExist
from src.models import Task

VALID_STATUSES = ['pending', 'running', 'success', 'failure']
ALLOWED_TRANSITIONS = {
    'pending': ['running'],
    'running': ['success', 'failure'],
    'success': [],
    'failure': [],
}


class TaskService:
    @staticmethod
    def create_task(name: str) -> Task:
        task = Task(name=name)
        task.save()
        return task

    @staticmethod
    def get_task(task_id: str) -> Task:
        try:
            return Task.objects.get(id=task_id)
        except DoesNotExist:
            raise ValueError("Task not found")

    @staticmethod
    def list_tasks() -> list:
        return list(Task.objects.all())

    @staticmethod
    def update_status(task_id: str, new_status: str) -> Task:
        task = TaskService.get_task(task_id)

        if new_status not in VALID_STATUSES:
            raise ValueError(f"Invalid status: {new_status}")

        allowed = ALLOWED_TRANSITIONS.get(task.status, [])
        if new_status not in allowed:
            raise ValueError(f"Cannot change status from '{task.status}' to '{new_status}'")

        task.status = new_status
        task.save()
        return task

    @staticmethod
    def reset_task(task_id: str) -> Task:
        task = TaskService.get_task(task_id)
        task.status = 'pending'
        task.save()
        return task

    @staticmethod
    def delete_task(task_id: str) -> None:
        task = TaskService.get_task(task_id)
        task.delete()
