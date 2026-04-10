from fastapi import FastAPI
from typing import List
from models import Task

app = FastAPI()

# In-memory DB (for now)
tasks = []

@app.get("/")
def home():
    return {"message": "TaskFlow API running"}

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task


@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task
            return updated_task
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return {"message": "Task deleted successfully"}
    return {"error": "Task not found"}