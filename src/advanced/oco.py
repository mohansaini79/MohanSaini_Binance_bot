import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from utils import client
import logging

def place_oco(symbol, take_profit, stop_loss):
    try:
        client.futures_create_order(
            symbol=symbol,
            side="SELL",
            type="TAKE_PROFIT_MARKET",
            stopPrice=take_profit,
            closePosition=True
        )

        client.futures_create_order(
            symbol=symbol,
            side="SELL",
            type="STOP_MARKET",
            stopPrice=stop_loss,
            closePosition=True
        )

        logging.info("OCO Order Placed")
        print("✅ OCO Order Success")

    except Exception as e:
        logging.error(str(e))
        print("❌ Error:", e)