from fastapi import FastAPI
from mongoengine import connect
from src.router import task_routes
from src.middleware import CustomErrorHandlerMiddleware

app = FastAPI()
app.add_middleware(CustomErrorHandlerMiddleware)

# MongoDB setup
connect(db="taskdb", host="mongodb://localhost:27017/taskdb")

# Register routes
app.include_router(task_routes)
