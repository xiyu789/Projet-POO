import pandas as pd
from binance.client import Client

import requests
import json
import datetime

api_key='key'
api_secret='secret'
client = Client(api_key, api_secret)
tickers = client.get_all_tickers()
#print(tickers)  #price is a list

url = 'https://api.binance.com'
api_call = '/api/v3/ticker/price'
headers = {'content-type': 'application/json', 'X_MBX-APIKEY': api_key}

response= requests.get(url + api_call, headers=headers)
response = json.loads(response.text)
#print(response)

df = pd.DataFrame.from_records(response)
#print(df.head())

#get Binance Server Status
client.ping()
#get Binance Server Time
res=client.get_server_time()
ts=res['serverTime']/1000
your_dt=datetime.datetime.fromtimestamp(ts)
your_dt.strftime("%Y-%m-%d %H-%M-%S")

#exchange & symbol info
exchange_info=client.get_exchange_info()
exchange_info.keys()  # return a dictionary
df_exchange = pd.DataFrame(exchange_info['symbols'])

symbol_info = client.get_symbol_info('BTCBUSD')

#########################
#market data
market_depth=client.get_order_book(symbol='BTCBUSD')  #to get bid ask price
bids=pd.DataFrame(market_depth['bids'])
bids.columns = ['price','bids']
asks=pd.DataFrame(market_depth['asks'])
bids.columns = ['price','asks']
df_bidask=pd.concat([bids,asks]).fillna(0)
#print(df_bidask.head())

#get recent trades
recent_trades=client.get_recent_trades(symbol='BTCTUSD')
df_trades=pd.DataFrame(recent_trades)

#get historical trades
id =df_trades.loc[450,'id'] # id of 450th trade
historical_trades=client.get_historical_trades(symbol='BTCBUSD', limit = 1000, fromId = id)
df_his=pd.DataFrame(historical_trades)
#print(df_his.head())

#get average symbol Price
avg_price = client.get_avg_price(symbol = 'BTCBUSD')

#get all tickers prices
tickers = client.get_ticker()
df_tickers=pd.DataFrame(tickers) #including pricechange pricechange% weightedAvgPrice prevClosePrice lastPrice Lastqty etc...

#place orders

class Binance:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

    def get_tickers(self):
        prices = self.client.get_all_tickers()
        return prices

    def get_historical_klines(self, symbol, interval):
        klines = self.client.futures_klines(symbol=symbol, interval=interval)
        historical_data= []
        for kline in klines:
            historical_data.append({
                "Date": kline[0],
                "Prix d'ouverture": kline[1],
                "Prix de clôture": kline[4]
            })
        return historical_data

    def display_historical_klines(self, historical_klines):
        for kline in historical_klines:
            print(f"Date : {kline['Date']}")
            print(f"Prix d'ouverture : {kline['Prix d ouverture']}")
            print(f"Prix de clôture : {kline['Prix de clôture']}")
            # Vous pouvez ajouter d'autres informations au besoin

            # Exemple d'utilisation
            api_key = 'key'
            api_secret = 'secret'
            symbol = 'BTCUSDT'
            interval = '1d'

            data_fetcher = HistoricalData(api_key, api_secret)
            historical = data_fetcher.get_historical_klines(symbol, interval)
            data_fetcher.display_historical_klines(historical_klines)
