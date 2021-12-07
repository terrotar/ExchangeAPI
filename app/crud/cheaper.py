
# Access cryptocoin's API
from app.crud import kraken
from app.crud import mercado_bitcoin


# GETTTERS


# Get cryptocoins cheaper exchange
def get_cheaper():
    kraken_OH = kraken.get_orderbook()
    mercado_bitcoin_OH = mercado_bitcoin.get_orderbook()
    if (kraken_OH and mercado_bitcoin_OH):

        if (kraken_OH["Kraken"]["BTC"]["Price(USD)"] < mercado_bitcoin_OH["Mercado Bitcoin"]["BTC"]["Price(USD)"]):
            cheaper = "kraken"
        elif (kraken_OH["Kraken"]["BTC"]["Price(USD)"] > mercado_bitcoin_OH["Mercado Bitcoin"]["BTC"]["Price(USD)"]):
            cheaper = "Mercado Bitcoin"
        else:
            cheaper = "Same value"

        return {
            'BTC': {
                'USD': {
                    'Kraken': kraken_OH["Kraken"]["BTC"]["Price(USD)"],
                    'Mercado Bitcoin': mercado_bitcoin_OH["Mercado Bitcoin"]["BTC"]["Price(USD)"],
                    'Cheaper': cheaper
                },
                'BRL': {
                    'Kraken': kraken_OH["Kraken"]["BTC"]["Price(BRL)"],
                    'Mercado Bitcoin': mercado_bitcoin_OH["Mercado Bitcoin"]["BTC"]["Price(BRL)"],
                    'Cheaper': cheaper
                }
            },
            'ETH': {
                'USD': {
                    'Kraken': kraken_OH["Kraken"]["ETH"]["Price(USD)"],
                    'Mercado Bitcoin': mercado_bitcoin_OH["Mercado Bitcoin"]["ETH"]["Price(USD)"],
                    'Cheaper': cheaper
                },
                'BRL': {
                    'Kraken': kraken_OH["Kraken"]["ETH"]["Price(BRL)"],
                    'Mercado Bitcoin': mercado_bitcoin_OH["Mercado Bitcoin"]["ETH"]["Price(BRL)"],
                    'Cheaper': cheaper
                }
            }
        }
