
from fastapi import APIRouter, HTTPException

from app.crud import cheaper


# Router cheaper instance
router = APIRouter(prefix='/cheaper',
                   tags=['Cheaper'])


# Get cryptocoins cheaper exchange
@router.get('/cheaper/BTC')
async def cheaper_BTC():

    cheaper_exchange = cheaper.get_cheaper()
    if cheaper_exchange:
        return cheaper_exchange

    raise HTTPException(status=502,
                        detail="Couldn't access cryptocoin's API")
