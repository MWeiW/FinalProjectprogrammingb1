from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from file_operations import load_tasks, save_tasks

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

@app.get("/")
def root():
    return {"message": "Task Management API is running"}

@app.get("/tasks", response_model=List[Task])
def get_tasks(completed: bool | None = None):
    tasks = load_tasks()
    if completed is not None:
        tasks = [task for task in tasks if task["completed"] == completed]
    return tasks

@app.get("/tasks/stats")
def task_stats():
    tasks = load_tasks()
    total = len(tasks)
    completed = len([t for t in tasks if t["completed"]])
    pending = total - completed
    percentage = (completed / total * 100) if total > 0 else 0

    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending,
        "completion_percentage": percentage
    }

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    tasks = load_tasks()
    new_id = 1
    if tasks:
        new_id = max(t["id"] for t in tasks) + 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "description": task.description,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    tasks = load_tasks()
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[index] = updated_task.dict()
            save_tasks(tasks)
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks")
def delete_all_tasks():
    save_tasks([])
    return {"message": "All tasks deleted"}
