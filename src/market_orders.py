import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils import client, validate
import logging

symbol = sys.argv[1]
side = sys.argv[2]
quantity = float(sys.argv[3])

try:
    validate(symbol, quantity)

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    logging.info(f"Market Order Placed: {order}")
    print("✅ Market Order Success")

except Exception as e:
    logging.error(str(e))
    print("❌ Error:", e)