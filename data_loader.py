"""
data_loader.py
Handles data input, cleaning, and preprocessing for options mispricing engine.
"""
import pandas as pd
import yfinance as yf
from datetime import datetime

class DataLoader:
    def __init__(self, risk_free_rate=0.01):
        self.risk_free_rate = risk_free_rate

    def load_csv(self, file_path):
        df = pd.read_csv(file_path)
        return self._preprocess(df)

    def fetch_yfinance(self, ticker):
        """
        Fetch option chain for the given ticker using yfinance.
        Fetches multiple expiration dates to support 3D volatility surface.
        """
        stock = yf.Ticker(ticker)
        expirations = stock.options
        if not expirations:
            raise ValueError(f"No options found for ticker {ticker}")

        # Fetch first 5 expiries (or all if fewer than 5)
        all_dfs = []
        underlying_price = stock.history(period='1d')['Close'].iloc[-1]
        today = datetime.now()

        for expiry in expirations[:5]:
            opt = stock.option_chain(expiry)
            
            calls = opt.calls.copy()
            calls['option_type'] = 'call'
            
            puts = opt.puts.copy()
            puts['option_type'] = 'put'
            
            df_expiry = pd.concat([calls, puts])
            df_expiry['expiry'] = expiry
            all_dfs.append(df_expiry)
        
        df = pd.concat(all_dfs)
        
        # Mapping yfinance columns to engine columns
        df = df.rename(columns={
            'strike': 'strike',
            'lastPrice': 'market_price',
            'impliedVolatility': 'implied_vol'
        })
        
        df['date'] = today.strftime('%Y-%m-%d')
        df['underlying_price'] = underlying_price
        
        # Select relevant columns
        df = df[['date', 'strike', 'expiry', 'option_type', 'market_price', 'underlying_price', 'implied_vol']]
        
        return self._preprocess(df)

    def _preprocess(self, df):
        df = df.dropna()
        df['expiry'] = pd.to_datetime(df['expiry'])
        df['date'] = pd.to_datetime(df['date'])
        df['time_to_maturity'] = (df['expiry'] - df['date']).dt.days / 365.0
        return df

    def set_risk_free_rate(self, rate):
        self.risk_free_rate = rate
