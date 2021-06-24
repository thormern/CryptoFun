from binance.client import Client
from binance.enums import *
#Constants:
api_key = "sGBn9zQp2bdiemmSIrO8NcXlI9JxTyb3JouR7oJ9NRTaeGgyoi91iyBnuDvWDqgw"
api_secret = "et1zGdlsqRDN8vcZUPqKpGyJhi7Q0N6e1n1W2Kf40kDQLr0uVO7nKJsIc0IiViWU"

api_test_key = "Mic7siN5JJ33ujjckJtpupzNDtjZsq8LnGmSJ4nL8L6Kz5oEda6NWGm3IsN3Oz3H"
api_test_secret = "KbFLCkPScLmDpnzd8eqjbxpqeFCyd58zoy6wo3OmMw0ldqH3is48G6IqbeqrPqh1"


SIDE_BUY = 'BUY'
SIDE_SELL = 'SELL'

ORDER_TYPE_LIMIT = 'LIMIT'

TIME_IN_FORCE_GTC = 'GTC'
FILL_OR_KILL = 'FOK'
IMMEDIATE_OR_CANCEL = 'IOC'


client = Client(api_test_key, api_test_secret)
client.API_URL = "https://testnet.binance.vision/api"

client.get_server_time()

def buy():

def sell():

def run_trade(run, client, asset, symbol):

    current_server_time = client.get_server_time()

    crypto_balance = client.get_asset_balance(asset=asset)["free"]
    BUSD_balance = client.get_asset_balance(asset='BUSD')["free"]

    crypto_price = client.get_ticker(symbol=symbol)["lastPrice"]

    while run:



balanceLTC = client.get_asset_balance(asset='LTC')
LTCBUSD_price = client.get_ticker(symbol='LTCBUSD')

print(balanceLTC["free"], LTCBUSD_price)
order = client.create_order(
    symbol='LTCBUSD',
    side=SIDE_SELL,
    type=ORDER_TYPE_LIMIT,
    timeInForce=IMMEDIATE_OR_CANCEL,
    quantity=500,
    price=LTCBUSD_price["lastPrice"]
)

balanceLTC = client.get_asset_balance(asset='LTC')
LTCBUSD_price = client.get_ticker(symbol='LTCBUSD')

print(balanceLTC["free"], LTCBUSD_price)


orders = client.get_all_orders(symbol='LTCBUSD')
print(orders)

balanceBUSD = client.get_asset_balance(asset='BUSD')
print(balanceBUSD)


order_status = client.get_order(symbol='LTCBUSD', orderId=22524)
print(order_status)


open_orders = client.get_open_orders(symbol='LTCBUSD')
print(open_orders)

orders = client.get_all_orders(symbol='LTCBUSD')
print(orders)


SIDE = SIDE_BUY
tmp = 'BTCBUSD'
BUY_PERCENT = 0.0

while True:

    price = client.get_ticker(symbol=tmp)

    if SIDE == 'BUY' and price['priceChangePercent'] >= BUY_PERCENT:
        something = 0





# result = client.cancel_order(symbol='LTCBUSD', orderId=22524)
# print(result)