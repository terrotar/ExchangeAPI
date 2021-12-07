
# FastAPI Router
from fastapi import APIRouter, HTTPException

# Access kraken's API
from app.crud import kraken


# Router kraken instance
router = APIRouter(prefix='/kraken',
                   tags=['Kraken'])


# Get Order Book
@router.get('/orderbook')
async def kraken_order_book():

    kraken_OH = kraken.get_orderbook()
    if kraken_OH:
        return kraken_OH

    raise HTTPException(status=502,
                        detail="Couldn't access kraken's API")
