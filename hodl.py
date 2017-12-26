#!bin/python3
import argparse
import json
import urllib.request

# constants
description = """
Your friendly, no-nonsense script to instantaneously check cryptocurrency prices, 
helping you HODL one day at a time :)
"""


def get_price(crypto="BTC", fiat="USD"):
    url = 'https://api.coinbase.com/v2/prices/{}-{}/spot'.format(crypto, fiat)
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()
    data = json.loads(r.decode('utf-8'))
    return "1 {} == {} {}". format(data['data']['base'],
                                   data['data']['amount'],
                                   data['data']['currency'])


def get_majors(fiat="USD"):
    return [get_price(crypto, fiat) for crypto in
               ['BTC', 'BCH', 'ETH', 'LTC']]


# display prices
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-cr', '--crypto',
                        help='the crypto you wish to price check',
                        choices=['BTC', 'BCH', 'ETH', 'LTC'])
    parser.add_argument('-c', '--currency',
                        help='the fiat currency you wish to use for comparison')
    args = parser.parse_args()
    if args.crypto and args.currency:
        print(get_price(args.crypto, args.currency))
    else:
        for report in get_majors():
            print(report)
