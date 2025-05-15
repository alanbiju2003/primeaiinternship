from binance.enums import *
from binance.exceptions import BinanceAPIException
import logging

def place_stop_limit_order(client, symbol, side, quantity, stop_price, limit_price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_STOP,
            quantity=quantity,
            stopPrice=stop_price,
            price=limit_price,
            timeInForce=TIME_IN_FORCE_GTC
        )
        logging.info("Stop-Limit Order: %s", order)
        return order
    except BinanceAPIException as e:
        logging.error("Stop-Limit API Error: %s", e)
        return {"error": str(e)}
