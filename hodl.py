#!bin/python
from __future__ import print_function, unicode_literals

try:
    from urllib.request import urlopen, Request, HTTPError
    import configparser as cp
except ImportError:
    import ConfigParser as cp
    from urllib2 import urlopen, Request, HTTPError
import argparse
import json

# constants
description = """
Your friendly, no-nonsense script to instantaneously check cryptocurrency prices, 
helping you HODL one day at a time :)
"""

# read config
config = cp.ConfigParser()
config.read('config.ini')


def get_price(crypto="BTC", fiat=config.get("currency", "FIAT")):
    try:
        url = 'https://api.coinbase.com/v2/prices/{}-{}/spot'.format(crypto, fiat)
        req = Request(url)
        r = urlopen(req).read()
        data = json.loads(r.decode('utf-8'))
        return "1 {} = {} {}".format(data['data']['base'],
                                     data['data']['amount'],
                                     data['data']['currency'])
    except HTTPError:
        return "[*] error, check you are using correct crypto and fiat symbols"


def get_majors(fiat=config.get("currency", "FIAT")):
    return [get_price(crypto, fiat) for crypto in
            ['BTC', 'BCH', 'ETH', 'LTC']]


def set_fiat(fiat):
    try:
        config.set('currency', 'FIAT', fiat)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        return "[*] {} configured as standard fiat".format(fiat)
    except Exception as e:
        return "[*] error while configuring fiat, report: ", e


def main():
    parser = argparse.ArgumentParser(description=description)
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('-c', '--crypto',
                        help='the crypto you wish to price check',
                        choices=['BTC', 'BCH', 'ETH', 'LTC'])
    group.add_argument('-f', '--fiat',
                        help='the fiat currency you wish to use for comparison')
    group.add_argument('-sf', '--set_fiat',
                        help='set your preferred fiat currency')
    args = parser.parse_args()

    if args.crypto and args.fiat:
        print(get_price(args.crypto, args.fiat))
    elif (args.set_fiat and args.crypto) or (args.crypto and args.set_fiat):
        print(set_fiat(args.set_fiat))
        print(get_price(args.crypto))
    elif args.crypto:
        print(get_price(args.crypto))
    elif args.set_fiat:
        print(set_fiat(args.set_fiat))
    else:
        for report in get_majors():
            print(report)


if __name__ == '__main__':
    main()
