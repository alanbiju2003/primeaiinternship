from basic_bot import BasicBot
from binance.enums import *

def main():
    bot = BasicBot()
    while True:
        print("\n--- Binance Trading Bot ---")
        symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
        side = input("Buy or Sell [buy/sell]: ").lower()
        order_type = input("Order type [market/limit]: ").lower()
        quantity = float(input("Quantity: "))
        price = None

        if order_type == 'limit':
            price = float(input("Price: "))

        side_enum = SIDE_BUY if side == 'buy' else SIDE_SELL
        type_enum = ORDER_TYPE_MARKET if order_type == 'market' else ORDER_TYPE_LIMIT

        result = bot.place_order(symbol, side_enum, type_enum, quantity, price)
        print("Order Result:", result)

        cont = input("Place another order? [y/n]: ").lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    main()
