from fastapi import APIRouter
from scheduler.tasks import run_job

router = APIRouter()

@router.post("/")
def manual_generate():
    run_job()
    return {"status": "success", "message": "Job executed manually"}

