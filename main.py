import json
import requests

from settings import headers,start_sale
import time

def headers_is_right() -> bool:
    user_info = 'https://www.binance.com/bapi/accounts/v1/private/account/user/base-detail'
    response = requests.post(user_info, headers=headers)

    if response.status_code == 200:
        print('Successfully connected\n')
        return True
    else:
        print('Something wrong...')
        print('Check please: COOKIE, CSRFTOKEN, headers')
        return False



headers_is_right()


js_order_create = {'amount': '4.7', 'productId': '44816796', 'tradeType': 0}

url = 'https://www.binance.com/bapi/nft/v1/private/nft/nft-trade/order-create'

while True:
    if time.time() < 	start_sale:
       print(1650018602-time.time())
    else:
        for _ in range(1000):
            response = requests.post(url=url, headers= headers, data= json.dumps(js_order_create))
            print(response.json())