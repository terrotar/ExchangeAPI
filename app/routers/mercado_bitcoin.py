
# FastAPI Router
from fastapi import APIRouter

from app.crud import mercado_bitcoin


# Router mercado_bitcoin instance
router = APIRouter(prefix='/mercado_bitcoin',
                   tags=['MercadoBitcoin'])


# Get Order Book
@router.get('/orderbook')
async def mercado_bitcoin_order_book():

    mercado_bitcoin_OH = mercado_bitcoin.get_orderbook()
    if mercado_bitcoin_OH:
        return mercado_bitcoin_OH

    raise HTTPException(status=502,
                        detail="Couldn't access mercado bitcoin's API")
