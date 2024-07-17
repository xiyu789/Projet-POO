import math
from scipy.stats import norm


class Option:
    def __init__(self, spot, strike, risk_free, time_to_maturity, volatility):
        self.spot: float = spot  # Spot price of the underlying asset
        self.strike: float = strike  # Strike price of the option
        self.risk_free: float = risk_free  # Risk-free interest rate
        self.ttm: float = time_to_maturity  # Time to expiration (in years)
        self.vol: float = volatility  # Volatility of the underlying asset

    def compute_d1(self):
        d1 = (math.log(self.spot / self.strike) + (self.risk_free + 0.5 * self.vol ** 2) * self.ttm) / \
             (self.vol * math.sqrt(self.ttm))
        return d1

    def compute_d2(self):
        d2 = self.compute_d1() - self.vol * math.sqrt(self.ttm)
        return d2

    def compute_vega(self):
        return self.spot * norm.pdf(self.compute_d1()) * math.sqrt(self.ttm)


class Call(Option):
    def compute_price(self):
        n_d1 = norm.cdf(self.compute_d1())
        n_d2 = norm.cdf(self.compute_d2())
        return self.spot * n_d1 - self.strike * math.exp(-self.risk_free * self.ttm) * n_d2

    def compute_delta(self):
        return norm.cdf(self.compute_d1())

    def compute_rho(self):
        return self.strike * self.ttm * math.exp(-self.risk_free * self.ttm) * norm.cdf(self.compute_d2())

    def compute_theta(self):
        return (-self.spot * self.vol * norm.pdf(self.compute_d1()) / (2 * math.sqrt(self.ttm))) \
               + self.risk_free * self.strike * math.exp(-self.risk_free * self.ttm) * norm.cdf(self.compute_d2())


class Put(Option):
    def compute_price(self):
        n_minus_d1 = norm.cdf(-self.compute_d1())
        n_minus_d2 = norm.cdf(-self.compute_d2())
        return self.strike * math.exp(-self.risk_free * self.ttm) * n_minus_d2 - self.spot * n_minus_d1

    def compute_delta(self):
        return norm.cdf(self.compute_d1()) - 1

    def compute_rho(self):
        return -self.strike * self.ttm * math.exp(-self.risk_free * self.ttm) * norm.cdf(-self.compute_d2())

    def compute_theta(self):
        return (-self.spot * self.vol * norm.pdf(self.compute_d1()) / (2 * math.sqrt(self.ttm))) \
               - self.risk_free * self.strike * math.exp(-self.risk_free * self.ttm) * norm.cdf(-self.compute_d2())


if __name__ == "__main__":
    call = Call(spot=300, strike=250, risk_free=0.05, time_to_maturity=1, volatility=0.15)
    print(call.compute_price())
    put = Put(spot=300, strike=250, risk_free=0.05, time_to_maturity=1, volatility=0.15)
    print(put.compute_price())
