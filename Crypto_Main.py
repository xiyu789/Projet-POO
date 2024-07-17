
#pip install pycoingecko
#pip install plotly

#libraries
from pycoingecko import CoinGeckoAPI
from binance.client import Client

import pandas as pd
import datetime as dt
import time as t
import plotly.graph_objects as go
from plotly.offline import plot

# Initialize client
cg = CoinGeckoAPI()

#Check API server status
cg.ping()

#get initial data using coingeckiapi
coin_list=cg.get_coins_list()
coinDateFrame=pd.DataFrame.from_dict(coin_list).sort_values('id').reset_index(drop=True)
index=pd.DataFrame(cg.get_indexes_list())
print(index.head())
#coinDateFrame[coinDateFrame['id'] == 'bitcoin']


coins = ['bitcoin','ethereum', 'dopex']
coinCategories=pd.DataFrame(cg.get_coins_categories_list())
#print(coinCategories['category_id'].head(100))

counterCurrency=cg.get_supported_vs_currencies()
#=vsCurrency=['usd','eru','link']

DataRequest = cg.get_price(ids=coins,
                            vs_currencies=counterCurrency,
                            include_market_cap = True,
                            include_24hr_vol = True,
                            include_24hr_change = True,
                            include_last_updated_at = True
                            )
#print(DataRequest)

#get price

#get marekt cap

#save the data in excel
#coinCategories.to_excel('crypto_data.xlsx', index=False)




#create dictionnaire
coin_dict = {item['id']: item['name'] for item in coin_list}


#Using python-Binance
api_key='key'
api_secret='secret'
client = Client(api_key, api_secret)
tickers = client.get_all_tickers()
#print(tickers)  #price is a list