from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend.app.database.connection import engine
from backend.app.models.chat import Base
from backend.app.api.chat_api import router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Conversational BI",
    version="1.0"
)

# Include API routes
app.include_router(router)

# Mount static folder
app.mount(
    "/static",
    StaticFiles(directory="backend/app/static"),
    name="static"
)

# Templates folder
templates = Jinja2Templates(
    directory="backend/app/templates"
)


@app.get("/")
def home():

    return {
        "status": "Home is working"
    }