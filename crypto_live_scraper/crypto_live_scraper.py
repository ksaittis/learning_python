import os
import sys
import time
import threading

import requests

prices = {'btc': {'price': 0.00}}

if len(sys.argv) < 2:
    print('Please provide some symbols')
    quit()


def update_price(coin: str) -> None:
    while True:
        template = r'https://api.bittrex.com/api/v1.1/public/getticker?market={}-{}'
        first_coin = 'usd' if coin == 'btc' else 'btc'
        get_response = requests.get(template.format(first_coin, coin))
        if get_response.ok and get_response.json()['success']:
            prices[coin]['price'] = get_response.json()['result']['Last']
        time.sleep(3)


def display_prices_on_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

    for sym, _ in prices.items():
        sym_formatted = sym.ljust(5)
        price_in_btc = prices[sym]['price']
        usd_price = prices['btc']['price'] * price_in_btc

        if sym == 'btc':
            print('{} -> ${:.2f}'.format(sym_formatted, price_in_btc))
        else:
            print('{} -> {:.8f} btc (${:.2f})'.format(sym_formatted, price_in_btc, usd_price))


coins = sys.argv[1:]
for coin in coins:
    prices[coin.lower()] = {'price': 0.00}

print(f'Symbols passed {coins}')
for coin in coins:
    t = threading.Thread(target=update_price, args=(coin,))
    t.start()

try:
    while True:
        display_prices_on_terminal()
        time.sleep(1)
except KeyboardInterrupt:
    print('Shutting down')
