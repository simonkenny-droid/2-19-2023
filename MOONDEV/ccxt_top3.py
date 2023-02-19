# TOP 3 THINGS TO DO WITH CCXT

import ccxt
import config

binance = ccxt.binance({
    'apiKey': config.BINANCE_API_KEY, 
    'secret': config.BINANCE_SECRET_KEY 
})

print (binance.fetch_balance())

# GET BID AND ASK
def get_bid_ask():
    
    btc_phe_book = binance.fetch_order_book('BTC/USDT')
    
# HOW TO MAKE ORDERS
