from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

# Setup templates directory
templates = Jinja2Templates(directory="app/templates")

# Mock Database
tasks_db = [{"id": 1, "task": "Setup CI/CD", "status": "Pending"}]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks_db})

@app.post("/add")
async def add_task(request: Request, task: str = Form(...)):
    new_id = len(tasks_db) + 1
    tasks_db.append({"id": new_id, "task": task, "status": "Pending"})
    # Re-render the page with the new task
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks_db})

@app.get("/health")
def health_check():
    return {"status": "healthy"}