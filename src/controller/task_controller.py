from fastapi import HTTPException
from src.services import TaskService
from bson import ObjectId

def serialize_task(task):
    return {
        "id": str(task.id),
        "name": task.name,
        "status": task.status,
        "created_at": task.created_at,
        "updated_at": task.updated_at,
    }


class TaskController:
    @staticmethod
    def create_task(data: dict):
        name = data.get("name")
        if not name:
            raise HTTPException(status_code=400, detail="Task name is required")
        task = TaskService.create_task(name)
        return serialize_task(task)

    @staticmethod
    def get_task(task_id: str):
        try:
            task = TaskService.get_task(task_id)
            return serialize_task(task)
        except ValueError:
            raise HTTPException(status_code=404, detail="Task not found")

    @staticmethod
    def list_tasks():
        tasks = TaskService.list_tasks()
        return [serialize_task(task) for task in tasks]

    @staticmethod
    def update_status(task_id: str, data: dict):
        new_status = data.get("status")
        if not new_status:
            raise HTTPException(status_code=400, detail="Status is required")
        try:
            task = TaskService.update_status(task_id, new_status)
            return serialize_task(task)
        except ValueError as ve:
            raise HTTPException(status_code=400, detail=str(ve))

    @staticmethod
    def reset_task(task_id: str):
        try:
            task = TaskService.reset_task(task_id)
            return serialize_task(task)
        except ValueError:
            raise HTTPException(status_code=404, detail="Task not found")

    @staticmethod
    def delete_task(task_id: str):
        try:
            TaskService.delete_task(task_id)
            return {"message": "Task deleted successfully"}
        except ValueError:
            raise HTTPException(status_code=404, detail="Task not found")
