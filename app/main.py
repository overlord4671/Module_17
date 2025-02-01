from fastapi import FastAPI
from app.routes.user import router as user_router
from app.routes.task import router as task_router


app = FastAPI()


app.include_router(user_router)
app.include_router(task_router)


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}
