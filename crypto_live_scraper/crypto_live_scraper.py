from concurrent.futures import ThreadPoolExecutor
import os
import sys
import time
import threading

import requests

prices = {'btc': {'price': 0.00}}

if len(sys.argv) < 2:
    print('Please provide some symbols')
    quit()

coins = sys.argv[1:]
for coin in coins:
    prices[coin.lower()] = {'price': 0.00}


def update_price(coin: str) -> None:
    while True:
        template = r'https://api.bittrex.com/api/v1.1/public/getticker?market={}-{}'
        first_coin = 'usd' if coin == 'btc' else 'btc'
        get_response = requests.get(template.format(first_coin, coin))
        prices[coin]['price'] = get_response.json()['result']['Last']
        time.sleep(3)


def display_prices_on_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

    for coin, _ in prices.items():
        sym_formatted = coin.ljust(5)
        coin_btc_price = prices[coin]['price']
        coin_usd_price = prices['btc']['price'] * coin_btc_price
        if coin == 'btc':
            print('{} -> ${:.2f}'.format(sym_formatted, coin_btc_price))
        else:
            print('{} -> {:.8f} btc (${:.2f})'.format(sym_formatted, coin_btc_price, coin_usd_price))


print(f'Symbols passed {coins}')
# for coin, _ in prices.items():
with ThreadPoolExecutor() as executor:
    executor.map(update_price, prices.keys())
    # t = threading.Thread(target=update_price, args=(coin,))
    # t.start()

try:
    while True:
        display_prices_on_terminal()
        time.sleep(1)
except KeyboardInterrupt:
    print('Shutting down')
