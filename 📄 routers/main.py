from fastapi import FastAPI
from routers import optimize

app = FastAPI(title="Factory Optimization API")

app.include_router(optimize.router)
