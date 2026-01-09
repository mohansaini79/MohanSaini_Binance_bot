import os
import logging
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

client = Client(
    os.getenv("BINANCE_API_KEY"),
    os.getenv("BINANCE_API_SECRET"),
    testnet=True
)

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def validate(symbol, quantity):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT pairs allowed")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")