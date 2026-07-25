"""
AI Trading Bot — Live BTC Price Monitor
Part of the "Build Your Own AI Trading Bot" series.
https://github.com/hovinng/ai-trading-bot

This bot fetches live BTC/USDT prices from Binance and prints
predictions. The real AI model will be trained in Part 5.
"""

import time
import sys
import ccxt


# ─── Configuration ───────────────────────────────────────────
SYMBOL = "BTC/USDT"       # Trading pair
INTERVAL = 60             # Seconds between updates
CONFIDENCE = 65.0         # Simulated model confidence (Part 5 replaces this)


def fetch_price(exchange):
    """Fetch current BTC/USDT price from Binance."""
    ticker = exchange.fetch_ticker(SYMBOL)
    return ticker["last"]


def predict(price):
    """
    Simulated AI prediction.
    In Part 5, this will be replaced with a trained ML model
    that outputs real probability scores.
    """
    return {
        "price": price,
        "direction": "UP" if price % 2 == 0 else "DOWN",  # placeholder
        "confidence": CONFIDENCE,
    }


def main():
    print("=" * 50)
    print(f"  AI Trading Bot — {SYMBOL}")
    print("  Build Your Own AI Trading Bot (Part 2)")
    print("=" * 50)
    print()
    print(f"Fetching {SYMBOL} every {INTERVAL}s...")
    print("Press Ctrl+C to stop.")
    print()

    exchange = ccxt.binance()

    try:
        while True:
            try:
                price = fetch_price(exchange)
                prediction = predict(price)

                arrow = "▲" if prediction["direction"] == "UP" else "▼"
                print(f"  {arrow} {SYMBOL}: ${price:,.2f}  |  "
                      f"confidence: {prediction['confidence']:.0f}%  |  "
                      f"prediction: {prediction['direction']}")

            except ccxt.NetworkError:
                print("  ⚠ Network error — retrying in 30s...")
                time.sleep(30)
                continue
            except ccxt.ExchangeError as e:
                print(f"  ⚠ Exchange error: {e}")
                time.sleep(30)
                continue

            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print()
        print("Bot stopped. See you in Part 3!")
        sys.exit(0)


if __name__ == "__main__":
    main()
