from fastapi import APIRouter

router = APIRouter(prefix='/other')


@router.get('/')
async def get_other():
    return {'Hello from other API!': 'This is the other API endpoint. It is located at /api/other'}