from fastapi import FastAPI
from models.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from api.source import router as source_router
from scheduler.tasks import start_scheduler
from api.generate import router as generate_router

start_scheduler()


# Inside app declaration
app.include_router(source_router, prefix="/sources", tags=["sources"])


# Import and include your routers (later)
# from api.routes import router as api_router

app = FastAPI()

# CORS support for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create DB tables on startup
Base.metadata.create_all(bind=engine)

# app.include_router(api_router) - To be added

app.include_router(generate_router, prefix="/generate", tags=["generate"])


# This will launch your job scheduler when FastAPI starts

start_scheduler()

