from fastapi import APIRouter

from .other.views import router as other_router

router = APIRouter()
router.include_router(other_router)