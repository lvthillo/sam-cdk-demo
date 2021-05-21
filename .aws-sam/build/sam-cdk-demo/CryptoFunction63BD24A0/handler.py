import ccxt
import json


# use CCXT library to connect with Binance API
exchange = getattr(ccxt, 'binance')({
    'timeout': 3000,
    'enableRateLimit': True
})

def get_current_price(coin_name, price_type):
    # fetch latest ticker data for coin pair xxx/BTC
    ticker = exchange.fetch_ticker('{}/BTC'.format(coin_name))
    # get ask/bid price from ticket data
    current_price = ticker[price_type]
    return current_price

def lambda_handler(event, context):
    # get values from query string parameters
    coin = event['queryStringParameters']['coin']
    price = event['queryStringParameters']['type']

    # CCXT exchange expects coin in uppercase
    valid_coin = coin.upper()

    # get current price based on coin name and price type (ask/bid)
    current_price = get_current_price(valid_coin, price)

    return {
        'statusCode': 200,
        'headers': { 
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'coin': valid_coin,
            'price': current_price,
        })
    }
