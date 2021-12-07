
# Access cryptocoin's API
from app.crud import kraken
from app.crud import mercado_bitcoin


# GETTTERS


# Get cryptocoins cheaper exchange
def get_cheaper():
    kraken_OH = kraken.get_orderbook()
    mercado_bitcoin_OH = mercado_bitcoin.get_orderbook()
    if (kraken_OH and mercado_bitcoin_OH):

        if (kraken_OH["BTC"]["Price(USD)"] < mercado_bitcoin_OH["BTC"]["Price(USD)"]):
            cheaper = "kraken"
        elif (kraken_OH["BTC"]["Price(USD)"] > mercado_bitcoin_OH["BTC"]["Price(USD)"]):
            cheaper = "Mercado Bitcoin"
        else:
            cheaper = "Same value"

        return {
            'BTC': {
                'USD': {
                    'Kraken': kraken_OH["BTC"]["Price(USD)"],
                    'Mercado Bitcoin': mercado_bitcoin_OH["BTC"]["Price(USD)"],
                    'Cheaper': cheaper
                },
                'BRL': {
                    'Kraken': kraken_OH["BTC"]["Price(BRL)"],
                    'Mercado Bitcoin': mercado_bitcoin_OH["BTC"]["Price(BRL)"],
                    'Cheaper': cheaper
                }
            },
            'ETH': {
                'USD': {
                    'Kraken': kraken_OH["ETH"]["Price(USD)"],
                    'Mercado Bitcoin': mercado_bitcoin_OH["ETH"]["Price(USD)"],
                    'Cheaper': cheaper
                },
                'BRL': {
                    'Kraken': kraken_OH["ETH"]["Price(BRL)"],
                    'Mercado Bitcoin': mercado_bitcoin_OH["ETH"]["Price(BRL)"],
                    'Cheaper': cheaper
                }
            }
        }
