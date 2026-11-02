import csv
import math
from datetime import datetime
from pathlib import Path

import yfinance as yf

# Keep the input and output files beside this script.
folder = Path(__file__).resolve().parent
stock_list = folder / "SP500 Tickers.csv"
report_file = folder / "portfolio_summary.csv"


def load_companies():
    companies = {}
    try:
        with stock_list.open("r", encoding="utf-8-sig", newline="") as file:
            for row in csv.DictReader(file):
                companies[row["Symbol"].upper()] = row["Security"]
    except (OSError, KeyError) as error:
        print("Could not read the stock list:", error)
    return companies


def positive_number(message):
    while True:
        try:
            number = float(input(message))
            if math.isfinite(number) and number > 0:
                return number
        except ValueError:
            pass
        print("Please enter a number greater than zero.")


companies = load_companies()
portfolio = {}

print("\nSTOCK PORTFOLIO TRACKER")
print("Prices come from Yahoo Finance and may be delayed.")
print("Enter one ticker at a time, or type done to finish.\n")

while True:
    symbol = input("Stock ticker (AAPL, MSFT, etc.): ").strip().upper()
    if symbol == "DONE":
        break
    if not symbol or not symbol.replace(".", "").replace("-", "").isalnum():
        print("Please enter a valid ticker symbol.")
        continue
    if symbol in portfolio:
        print("You have already entered this ticker.")
        continue

    print("Company:", companies.get(symbol, "Not found in the sample stock list"))
    buy_price = positive_number("Price paid per share (USD): ")
    shares = positive_number("Number of shares: ")
    portfolio[symbol] = {"buy_price": buy_price, "shares": shares}

if not portfolio:
    print("No stocks entered. Nothing was saved.")
    raise SystemExit

checked_at = datetime.now().astimezone().isoformat(timespec="seconds")
results = []
total_invested = 0.0
total_value = 0.0

print("\nFetching the latest available prices...\n")

for symbol, holding in portfolio.items():
    try:
        # Yahoo Finance uses BRK-B instead of BRK.B, for example.
        yahoo_symbol = symbol.replace(".", "-")
        market_price = float(yf.Ticker(yahoo_symbol).fast_info.last_price)
        if not math.isfinite(market_price) or market_price <= 0:
            raise ValueError("No usable market price returned")
    except Exception as error:
        print(f"Skipped {symbol}: could not get a market price ({error})")
        continue

    shares = holding["shares"]
    buy_price = holding["buy_price"]
    invested = buy_price * shares
    value = market_price * shares
    change = value - invested
    percent = (change / invested) * 100

    total_invested += invested
    total_value += value

    results.append({
        "Checked At": checked_at,
        "Ticker": symbol,
        "Company": companies.get(symbol, "Not in stock list"),
        "Shares": f"{shares:.4f}",
        "Buy Price USD": f"{buy_price:.2f}",
        "Market Price USD": f"{market_price:.2f}",
        "Invested USD": f"{invested:.2f}",
        "Value USD": f"{value:.2f}",
        "Gain or Loss USD": f"{change:.2f}",
        "Gain or Loss Percent": f"{percent:.2f}",
    })

    print(f"{symbol:<7} Invested: ${invested:>10.2f} | "
          f"Value: ${value:>10.2f} | Change: {percent:+.2f}%")

if not results:
    print("No valid prices were retrieved. No report was saved.")
    raise SystemExit

profit = total_value - total_invested
profit_percent = (profit / total_invested) * 100
print("\nPORTFOLIO TOTAL")
print(f"Total invested: ${total_invested:.2f}")
print(f"Current value:  ${total_value:.2f}")
print(f"Gain or loss:   ${profit:.2f} ({profit_percent:+.2f}%)")

results.append({
    "Checked At": checked_at,
    "Ticker": "TOTAL",
    "Company": "Portfolio total",
    "Shares": "",
    "Buy Price USD": "",
    "Market Price USD": "",
    "Invested USD": f"{total_invested:.2f}",
    "Value USD": f"{total_value:.2f}",
    "Gain or Loss USD": f"{profit:.2f}",
    "Gain or Loss Percent": f"{profit_percent:.2f}",
})

try:
    has_data = report_file.exists() and report_file.stat().st_size > 0
    with report_file.open("a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys())
        if not has_data:
            writer.writeheader()
        writer.writerows(results)
    print("\nReport saved to:", report_file)
except OSError as error:
    print("Could not save the CSV report:", error)
