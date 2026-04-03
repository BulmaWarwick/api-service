import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api_service.models import Base
from api_service.database import get_db
from api_service.routes import user_router

app = FastAPI(title="API Service")

@app.on_event("startup")
async def startup_event():
    engine = create_engine("postgresql://user:password@localhost/dbname")
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()

@app.get("/")
async def read_root():
    return {"message": "API Service"}

app.include_router(user_router, prefix="/users", tags=["users"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)