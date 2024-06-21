from fastapi import FastAPI
from workoutapi.routers import api_router

app = FastAPI(title = "WORKOUTAPI")

app.include_router(api_router)



