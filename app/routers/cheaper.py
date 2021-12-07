
from fastapi import APIRouter

import httpx

from app.routers import kraken


router = APIRouter(prefix='/cheaper',
                   tags=['Cheaper'])


@router.get('/cheaper/BTC')
async def cheaper_BTC():
    pass
