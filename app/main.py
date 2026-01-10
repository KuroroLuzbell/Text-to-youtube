
from fastapi import FastAPI
from app.routes import example, guion


app = FastAPI()

app.include_router(example.router)
app.include_router(guion.router)
