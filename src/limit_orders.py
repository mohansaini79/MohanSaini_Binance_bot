import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils import client, validate
import logging

symbol = sys.argv[1]
side = sys.argv[2]
quantity = float(sys.argv[3])
price = float(sys.argv[4])

try:
    validate(symbol, quantity)

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        timeInForce="GTC",
        quantity=quantity,
        price=price
    )

    logging.info(f"Limit Order Placed: {order}")
    print("✅ Limit Order Success")

except Exception as e:
    logging.error(str(e))
    print("❌ Error:", e)