
# Async requests
import httpx


# GETTTERS


# Kraken's orderbook API last
# cryptocoins asks
def get_orderbook():

    # Get cryptocoins in USD
    order_book = httpx.get('https://api.kraken.com/0/public/Depth?pair=XBTUSD&count=1')
    bitcoin_ask = float(order_book.json()['result']['XXBTZUSD']['asks'][0][0])
    order_book = httpx.get('https://api.kraken.com/0/public/Depth?pair=XETHZUSD&count=1')
    ethereum_ask = float(order_book.json()['result']['XETHZUSD']['asks'][0][0])

    # Convert to BRL
    exchange_usd_brl = httpx.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
    usd_brl = float(exchange_usd_brl.json()['USDBRL']['ask'])

    return {
        'BTC': {
            'Price(USD)': round(bitcoin_ask, 2),
            'Price(BRL)': round(bitcoin_ask*usd_brl, 2)
        },
        'ETH': {
            'Price(USD)': round(ethereum_ask, 2),
            'Price(BRL)': round(ethereum_ask*usd_brl, 2)
        }
    }
