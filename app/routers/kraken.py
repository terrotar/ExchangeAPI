
# FastAPI Router
from fastapi import APIRouter

# Async requests
import httpx


# Router kraken instance
router = APIRouter(prefix='/kraken',
                   tags=['kraken'])


# Get Order Book
@router.get('/orderbook')
async def kraken_order_book():
    order_book = httpx.get('https://api.kraken.com/0/public/Depth?pair=XBTUSD&count=1')
    bitcoin_ask = order_book.json()['result']['XXBTZUSD']['asks'][0][0]
    order_book = httpx.get('https://api.kraken.com/0/public/Depth?pair=XETHZUSD&count=1')
    ethereum_ask = order_book.json()['result']['XETHZUSD']['asks'][0][0]
    return {
        'BTC': {
            'Price(USD)': float(bitcoin_ask)
        },
        'ETH': {
            'Price(USD)': float(ethereum_ask)
        }
    }
