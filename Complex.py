import threading
import queue
import random
import time
import logging
from statistics import mean, stdev

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(threadName)s | %(message)s"
)

# Shared queue for communication between threads
data_queue = queue.Queue()

class StockDataFetcher(threading.Thread):
    """Fetches stock price data and adds it to the queue."""
    def __init__(self, symbol, data_queue):
        super().__init__()
        self.symbol = symbol
        self.data_queue = data_queue

    def run(self):
        try:
            logging.info(f"Fetching data for {self.symbol}")
            # Simulate API call delay
            time.sleep(random.uniform(0.5, 2.0))
            
            # Simulate stock prices (normally you'd use `requests.get` here)
            prices = [round(random.uniform(100, 500), 2) for _ in range(10)]
            self.data_queue.put((self.symbol, prices))
            logging.info(f"Data fetched for {self.symbol}: {prices}")
        except Exception as e:
            logging.error(f"Error fetching data for {self.symbol}: {e}")


class StockDataAnalyzer:
    """Analyzes fetched stock data."""
    def __init__(self, data_queue):
        self.data_queue = data_queue
        self.results = {}

    def process_data(self):
        while not self.data_queue.empty():
            symbol, prices = self.data_queue.get()
            avg = mean(prices)
            volatility = stdev(prices)
            trend = "Upward" if prices[-1] > prices[0] else "Downward"
            self.results[symbol] = {
                "Average": round(avg, 2),
                "Volatility": round(volatility, 2),
                "Trend": trend
            }
            logging.info(f"Analyzed {symbol}: {self.results[symbol]}")

    def display_results(self):
        print("\n=== Stock Analysis Summary ===")
        for symbol, stats in self.results.items():
            print(f"{symbol}: {stats}")


if __name__ == "__main__":
    stock_symbols = ["AAPL", "GOOG", "TSLA", "AMZN", "MSFT"]
    threads = []

    # Start fetching data concurrently
    for symbol in stock_symbols:
        thread = StockDataFetcher(symbol, data_queue)
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Analyze the fetched data
    analyzer = StockDataAnalyzer(data_queue)
    analyzer.process_data()
    analyzer.display_results()
