from fastapi import APIRouter

from backend.app.core.config import settings


router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
def health_check():
    return {
        "status": "ok",
        "application": settings.app_name,
        "version": settings.app_version,
    }