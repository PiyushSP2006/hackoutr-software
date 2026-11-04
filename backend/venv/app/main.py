from fastapi import FastAPI

from .database import engine, Base
from . import models

from .routers.submit_issue import router as submit_issue
from .routers.user_add import router as user_create

app = FastAPI()

# Create all database tables
Base.metadata.create_all(bind=engine)

app.include_router(submit_issue)
app.include_router(user_create)

@app.get("/")
async def root():
    return {"message": "Hello World"}