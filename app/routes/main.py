from fastapi import FastAPI
from app.models.user import router as user_router
from app.models.task import router as task_router


app = FastAPI()


app.include_router(user_router)
app.include_router(task_router)


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}
