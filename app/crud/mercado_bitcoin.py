
# Async requests
import httpx


# GETTTERS


# mercado bitcoin's orderbook API last
# cryptocoins asks
def get_orderbook():

    # Get cryptocoins in USD
    order_book = httpx.get('https://www.mercadobitcoin.net/api/BTC/orderbook/')
    bitcoin_ask = round(order_book.json()['asks'][0][0], 2)
    order_book = httpx.get('https://www.mercadobitcoin.net/api/ETH/orderbook/')
    ethereum_ask = round(order_book.json()['asks'][0][0], 2)

    # Convert to BRL
    exchange_usd_brl = httpx.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
    usd_brl = float(exchange_usd_brl.json()['USDBRL']['ask'])

    return {
        'BTC': {
            'Price(USD)': round(bitcoin_ask/usd_brl, 2),
            'Price(BRL)': round(bitcoin_ask, 2)
        },
        'ETH': {
            'Price(USD)': round(ethereum_ask/usd_brl, 2),
            'Price(BRL)': round(ethereum_ask, 2)
        }
    }
