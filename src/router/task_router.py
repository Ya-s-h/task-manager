from fastapi import APIRouter, Body
from src.controller import TaskController

task_routes = APIRouter(prefix="/tasks", tags=["Tasks"])


@task_routes.post("/")
def create_task(data: dict = Body(...)):
    return TaskController.create_task(data)


@task_routes.get("/")
def list_tasks():
    return TaskController.list_tasks()


@task_routes.get("/{task_id}")
def get_task(task_id: str):
    return TaskController.get_task(task_id)


@task_routes.put("/{task_id}/status")
def update_status(task_id: str, data: dict = Body(...)):
    return TaskController.update_status(task_id, data)


@task_routes.post("/{task_id}/reset")
def reset_task(task_id: str):
    return TaskController.reset_task(task_id)


@task_routes.delete("/{task_id}")
def delete_task(task_id: str):
    return TaskController.delete_task(task_id)
