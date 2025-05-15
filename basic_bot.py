import logging
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
import os
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BasicBot:
    def __init__(self, testnet=True):
        api_key = os.getenv('BINANCE_API_KEY')
        api_secret = os.getenv('BINANCE_API_SECRET')
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        logging.info("Bot initialized using testnet: %s", testnet)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
    "symbol": symbol,
    "side": side.upper(),
    "type": order_type.upper(),
    "quantity": quantity,
    "positionSide": "LONG" if side.lower() == "buy" else "SHORT"  # Add this line
}

            if order_type == ORDER_TYPE_LIMIT:
                params['price'] = price
                params['timeInForce'] = TIME_IN_FORCE_GTC

            order = self.client.futures_create_order(**params)
            logging.info("Order placed: %s", order)
            return order

        except BinanceAPIException as e:
            logging.error("API Error: %s", e)
            return {"error": str(e)}
        except Exception as e:
            logging.error("Unexpected Error: %s", e)
            return {"error": str(e)}
