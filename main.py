import argparse
from binance.enums import *
from basic_bot import BasicBot

def parse_args():
    parser = argparse.ArgumentParser(description="Simple Binance Futures Trading Bot")
    parser.add_argument('--symbol', required=True)
    parser.add_argument('--side', choices=['buy', 'sell'], required=True)
    parser.add_argument('--type', choices=['market', 'limit'], required=True)
    parser.add_argument('--quantity', type=float, required=True)
    parser.add_argument('--price', type=float, help='Required for limit orders')
    return parser.parse_args()

def main():
    args = parse_args()
    bot = BasicBot()

    side = SIDE_BUY if args.side == 'buy' else SIDE_SELL
    order_type = ORDER_TYPE_MARKET if args.type == 'market' else ORDER_TYPE_LIMIT

    if order_type == ORDER_TYPE_LIMIT and args.price is None:
        print("Price is required for limit orders.")
        return

    result = bot.place_order(
        symbol=args.symbol.upper(),
        side=side,
        order_type=order_type,
        quantity=args.quantity,
        price=args.price
    )

    print("Order Result:", result)

if __name__ == '__main__':
    main()
