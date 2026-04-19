# 📊 Options Mispricing & Volatility Surface Engine

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Financial Analysis](https://img.shields.io/badge/finance-quantitative-orange.svg)

> **Created By Rengesh**

A modular, high-performance engine for detecting option mispricing using the Black-Scholes model, visualizing complex volatility surfaces, and ranking arbitrage opportunities.

---

## 🚀 About This Project

This project is a modular engine designed for **quantitative finance analysis**. It focuses on identifying discrepancies between market prices and theoretical values, helping users understand patterns in options pricing through sophisticated mathematical models and interactive visualizations.

## ✨ Key Features

- 📥 **Flexible Data Input**: Support for local CSV files or real-time data via `yfinance`.
- 🧮 **Black-Scholes Core**: Custom implementation of the Black-Scholes pricing model (no external pricing black-boxes).
- 📐 **The Greeks**: Full calculation suite for **Delta, Gamma, Vega, and Theta**.
- 🔍 **Mispricing Detection**: Statistical ranking of pricing anomalies and arbitrage potential.
- 📉 **Advanced Visualization**: 
  - 2D Volatility Smiles
  - Interactive 3D Volatility Surfaces
  - Heatmaps, Histograms, and Scatter plots.
- 🏗️ **Professional Architecture**: Clean, object-oriented, and modular Python structure.

## 🛠️ Quick Start

### 1. Fork & Clone
Click the **Fork** button on the top right, then run:
```bash
git clone https://github.com/rengesh/options-mispricing-vol-surface-engine.git
cd options-mispricing-vol-surface-engine
```

### 2. Install Dependencies
```bash
pip install -r "Options Mispricing Surface Engine/requirements.txt"
```

### 3. Run the Engine
**Using a stock ticker:**
```bash
python "Options Mispricing Surface Engine/main.py" AAPL
```

**Using a custom CSV:**
```bash
python "Options Mispricing Surface Engine/main.py" --csv "Options Mispricing Surface Engine/sample.csv" --risk_free_rate 0.01
```

---

## 🖼️ Visualizations

The engine generates five interactive windows. *Note: You must close one window to view the next.*

1. **📉 Implied Volatility Smile**: Shows how IV varies with strike price for the nearest maturity.
2. **🌐 3D Volatility Surface**: A rotatable 3D plot of IV against Strike Price and Time to Maturity.
3. **🔥 Mispricing Heatmap**: A color-coded grid visualizing mispricing magnitude across strikes and expirations.
4. **🎯 Price Comparison**: Scatter plot of Market vs. Black-Scholes prices with a 45° reference line.
5. **📊 Mispricing Histogram**: Statistical distribution of pricing errors to identify bias or outliers.

---

## 📂 Project Structure

- `data_loader.py` 📥: Data input, cleaning, and preprocessing.
- `pricing.py` 🧮: Black-Scholes logic and mispricing calculations.
- `greeks.py` 📐: Mathematical derivations for Delta, Gamma, Vega, and Theta.
- `analysis.py` 🔬: Quantitative analysis and visualization logic.
- `main.py` 🕹️: CLI orchestration and end-to-end execution.

## 📋 CSV Requirements

If providing custom data, ensure it follows this format:
```csv
date,strike,expiry,option_type,market_price,underlying_price,implied_vol
```

## 📦 Requirements

- `pandas`
- `numpy`
- `scipy`
- `matplotlib`
- `yfinance`

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---
⭐ *If you find this project useful, consider giving it a star!*
