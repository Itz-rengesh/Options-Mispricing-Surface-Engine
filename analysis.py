"""
analysis.py
Advanced quant features: volatility smile, surface, mispricing detection, ranking.
"""
import numpy as np
import pandas as pd
from pricing import BlackScholes
from greeks import Greeks

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Analysis:
    def __init__(self, risk_free_rate=0.01):
        self.bs = BlackScholes(risk_free_rate)
        self.greeks = Greeks(risk_free_rate)

    def compute_metrics(self, df):
        mean_abs = np.mean(np.abs(df['mispricing']))
        max_dev = np.max(np.abs(df['mispricing']))
        arbitrage_score = np.sum(np.abs(df['zscore']) > 2)
        return {'mean_abs_mispricing': mean_abs, 'max_deviation': max_dev, 'arbitrage_score': arbitrage_score}

    def rank_arbitrage(self, df):
        df['abs_zscore'] = np.abs(df['zscore'])
        return df.sort_values('abs_zscore', ascending=False).head(10)

    def implied_vol_smile(self, df):
        grouped = df.groupby('strike')['implied_vol'].mean()
        plt.figure('Implied Volatility Smile', figsize=(8,5))
        plt.plot(grouped.index, grouped.values, marker='o')
        plt.title('Implied Volatility Smile')
        plt.xlabel('Strike')
        plt.ylabel('Implied Volatility')
        plt.grid(True)
        plt.show()

    def volatility_surface(self, df):
        piv = df.pivot_table(index='strike', columns='time_to_maturity', values='implied_vol', aggfunc='mean')
        piv = piv.sort_index(axis=0).sort_index(axis=1)
        piv = piv.interpolate(method='linear', axis=0).interpolate(method='linear', axis=1).bfill().ffill()

        X, Y = np.meshgrid(piv.columns, piv.index)
        Z = piv.values
        
        fig = plt.figure('Volatility Surface', figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9, antialiased=True)
        
        ax.set_title('3D Volatility Surface (Interactable: Click & Drag to Rotate)')
        ax.set_xlabel('Time to Maturity (Years)')
        ax.set_ylabel('Strike Price')
        ax.set_zlabel('Implied Volatility')
        
        # Set a better initial view angle for rotation
        ax.view_init(elev=30, azim=225)
        
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Implied Volatility')
        plt.tight_layout()
        plt.show()

    def mispricing_heatmap(self, df):
        piv = df.pivot_table(index='strike', columns='expiry', values='mispricing')
        plt.figure('Mispricing Heatmap', figsize=(10,6))
        plt.imshow(piv, aspect='auto', cmap='coolwarm')
        plt.title('Mispricing Heatmap (Strike vs Expiry)')
        plt.xlabel('Expiry')
        plt.ylabel('Strike')
        plt.colorbar(label='Mispricing')
        plt.show()

    def price_comparison(self, df):
        # Filter for scatter plot to avoid too many points if data is large
        plt.figure('Price Comparison', figsize=(8,5))
        plt.scatter(df['theoretical_price'], df['market_price'], alpha=0.7)
        plt.plot([df['theoretical_price'].min(), df['theoretical_price'].max()], [df['theoretical_price'].min(), df['theoretical_price'].max()], 'r--')
        plt.title('Theoretical vs Market Price')
        plt.xlabel('Theoretical Price')
        plt.ylabel('Market Price')
        plt.grid(True)
        plt.show()

    def mispricing_histogram(self, df):
        plt.figure('Mispricing Distribution', figsize=(8,5))
        plt.hist(df['mispricing'], bins=30, color='skyblue', edgecolor='black')
        plt.title('Distribution of Mispricing')
        plt.xlabel('Mispricing')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
