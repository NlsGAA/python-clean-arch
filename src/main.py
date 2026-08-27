from fastapi import FastAPI
from src.presentation.https.routes import router

app = FastAPI()

app.include_router(router)