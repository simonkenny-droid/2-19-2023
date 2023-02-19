# import ccxt

import ccxt
#print(ccxt.exchanges) # print a list of all available exchange classes 
import config

exchange = ccxt.binance()
print(exchange.requiredCredentials)

#print(dir(ccxt))

#for exchange in ccxt.exchanges:
 #   print(exchange)

#exchange = ccxt.binance()
#print(exchange)

#exchange_id = 'binance'
#exchange_class = getattr(ccxt, exchange_id)
#exchange = exchange_class({
#    'apiKey': 'YOUR_API_KEY',
#    'secret': 'YOUR_SECRET',
#})


exchange = ccxt.binance({
    'apiKey': config.BINANCE_API_KEY, 
    'secret': config.BINANCE_SECRET_KEY
})


balance = exchange.fetch_balance()
##print(balance)

print(balance['total']['USDT'])

#markets = exchange.load_markets()

#for market in markets:
    #print(market)

#ticker = exchange.fetch_ticker('AVA/USDT')
#print(ticker)

#ohlc = exchange.fetch_ohlcv('AVA/USDT', timeframe='15m', limit=5)
#print(ohlc)
##for candle in ohlc:
#    print(candle)
    
#order_book = exchange.fetch_order_book('AVA/USDT')
#print(order_book)



