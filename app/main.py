from fastapi import FastAPI
from app.api.router import api_router
from app.core.database import Base, engine

# IMPORTANT: import models
from app.models import product_model, user_model

app = FastAPI(title="Ecommerce API")

# create tables
Base.metadata.create_all(bind=engine)

app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "Ecommerce API running"}
