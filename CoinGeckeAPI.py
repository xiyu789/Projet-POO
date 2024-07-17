from pycoingecko import CoinGeckoAPI

class CoinGecko:
    def __init__(self):
        self.cg = CoinGeckoAPI()

    def get_assets(self):
        coins_list = self.cg.get_coins_markets(vs_currency='usd', ids='', order='market_cap_desc', per_page=10, page=1)
        return coins_list

    def display_assets(self, coins_list):
        for coin in coins_list:
            print(f"name: {coin['name']}")
            print(f"market cap: {coin['market_cap']}")
            print(f"symbol: {coin['symbol']}")

# test
data = CoinGecko()
assets = data.get_assets()
data.display_assets(assets)
