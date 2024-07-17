from datetime import datetime


class FinancialAsset:
    def __init__(self, ticker, price, currency):
        self.ticker: str = ticker
        self.price: float = price
        self.currency: str = currency

    def get_description(self):
        print(f'The ticker for this asset is {self.ticker} and its price is {self.price} {self.currency}')


class Equity(FinancialAsset):
    def __init__(self, ticker, price, currency, dividend):
        super().__init__(ticker, price, currency)
        # alternative way to do it : FinancialAsset.__init__(self, ticker, price, currency)
        self.dividend: float = dividend

    def calculate_pe_ratio(self):
        if self.dividend == 0:
            return float('inf')  # P/E is theoretically infinite if earnings are zero
        return self.price / self.dividend


class Bond(FinancialAsset):
    def __init__(self, ticker, price, currency, nominal, maturity_date, coupon_rate, coupon_frequency):
        super().__init__(ticker, price, currency)
        self.nominal = nominal
        self.maturity_date: datetime = maturity_date
        self.years_to_maturity = self.compute_ttm()
        self.coupon_rate: float = coupon_rate
        self.coupon_frequency: float = coupon_frequency

    def compute_ttm(self):
        today = datetime.now()
        delta = self.maturity_date - today
        return delta.days / 365


if __name__ == '__main__':
    asset = FinancialAsset('AAPL', 178, 'USD')  # create a Financial Asset object
    asset.get_description()  # call the method get description of the object
    print(asset.ticker)  # display the ticker of the object

    equity = Equity('AAPL', 178, 'USD', 5.95)  # create an Equity Asset object
    equity.get_description()  # call the method defined in the Parent class
    print(f"PE ratio for {equity.ticker} : {round(equity.calculate_pe_ratio(),2)}")

    bond_maturity = datetime(2030, 12, 31)
    bond = Bond("US10YT", 97, "USD", 100, bond_maturity, 0.0405, 1)
    bond.get_description()
