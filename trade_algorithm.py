import os
import time
from binance.client import Client
from Models import Ticker, Order, Balance
SIDE_BUY = 'BUY'
SIDE_SELL = 'SELL'

ORDER_TYPE_LIMIT = 'LIMIT'

TIME_IN_FORCE_GTC = 'GTC'
FILL_OR_KILL = 'FOK'
IMMEDIATE_OR_CANCEL = 'IOC'

CONSTANT = 10.0
CURRENCY = "BUSD"
COIN = "BTC"
SYMBOL = CURRENCY + COIN


SELL_DECREASE = 0.0         # The loss we aim for before selling.
BUY_INCREASE = 0.0          # The growth we aim for before buying.

api_test_key = "Mic7siN5JJ33ujjckJtpupzNDtjZsq8LnGmSJ4nL8L6Kz5oEda6NWGm3IsN3Oz3H"
api_test_secret = "KbFLCkPScLmDpnzd8eqjbxpqeFCyd58zoy6wo3OmMw0ldqH3is48G6IqbeqrPqh1"


client = Client(api_test_key, api_test_secret)
client.API_URL = "https://testnet.binance.vision/api"



def buy(quantity):
    #@TODO - CREATE BUY ORDER --> DONE
    order = Order(Client.order_market_buy(symbol=SYMBOL, quantity=quantity))
    return order

    #BUY MAX AMOUNT IOC

def sell(quantity):
    #@TODO - CREATE SELL ORDER --> DONE
    order = Order(client.order_market_sell(symbol=SYMBOL, quantity=quantity))
    return order
    #SELL ALL GTC
def just_trade_algorithm(side, order):

    #@TODO - Fetch current price of selected --> DONE

    ticker = Ticker(client.get_ticker(symbol=SYMBOL))

    #@TODO - Fetch change in price --> DONE

    price_change_percent = ticker.priceChangePercent
    price = ticker.lastPrice

    if side == "BUY" and price_change_percent >= BUY_INCREASE:
        #@TODO Make class for balance object --> DONE
        balance = Balance(client.get_asset_balance(asset=CURRENCY))
        quantity = (balance / price) - CONSTANT
        order = buy(quantity)

    if side == "SELL" and price_change_percent <= SELL_DECREASE:
        balance = Balance(client.get_asset_balance(asset=COIN))
        order = sell(balance)

    return order

def run():
    order = None
    timer = 0.0
    while True: # How long should the programme run for
        #@TODO - Check the response time, to ensure low latency.
        response = os.system("ping  " + "@https://testnet.binance.vision/api")

        if response < 200:

            #@TODO - Check last order --> DONE

            if order.side == "BUY":
                order = just_trade_algorithm(SIDE_SELL, order)
            elif order.side  == "SELL":
                order = just_trade_algorithm(SIDE_BUY, order)
            else: order = just_trade_algorithm(SIDE_BUY, order)


        else:
             time.sleep(10000)


run('BTCBUSD')