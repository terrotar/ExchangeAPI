
# FastAPI Router
from fastapi import APIRouter

import httpx


# Router mercado_bitcoin instance
router = APIRouter(prefix='/mercado_bitcoin',
                   tags=['MercadoBitcoin'])


# Get Order Book
@router.get('/orderbook')
async def mercado_bitcoin_order_book():
    order_book = httpx.get('https://www.mercadobitcoin.net/api/BTC/orderbook/')
    bitcoin_ask = round(order_book.json()['asks'][0][0], 2)
    order_book = httpx.get('https://www.mercadobitcoin.net/api/ETH/orderbook/')
    ethereum_ask = round(order_book.json()['asks'][0][0], 2)

    # Get USD/BRL
    exchange_usd_brl = httpx.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
    usd_brl = float(exchange_usd_brl.json()['USDBRL']['ask'])

    return {
        'BTC': {
            'Price(USD)': round(bitcoin_ask/usd_brl, 2)
        },
        'ETH': {
            'Price(USD)': round(ethereum_ask/usd_brl, 2)
        }
    }
