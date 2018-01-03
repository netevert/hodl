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
import os

# constants
description = "Your friendly, no-nonsense tool to instantaneously check cryptocurrency prices"
epilog = "hodl.py: helping you HODL one day at a time :)"
__version__ = "v.1.0.0a1"

# load config file
config_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                               'conf', 'config.ini')
config = cp.ConfigParser()
config.read(config_filename)


def get_price(crypto="BTC", fiat=config.get("currency", "FIAT")):
    """Returns the conversion price between the supplied crypto and fiat currencies"""
    try:
        url = 'https://api.coinbase.com/v2/prices/{}-{}/spot'.format(crypto,
                                                                     fiat)
        req = Request(url)
        r = urlopen(req).read()
        data = json.loads(r.decode('utf-8'))
        return "1 {} = {} {}".format(data['data']['base'],
                                     data['data']['amount'],
                                     data['data']['currency'])
    except HTTPError:
        return "[*] error, check you are using correct crypto and fiat symbols"


def get_majors(fiat=config.get("currency", "FIAT")):
    """Returns the conversion prices for all supported crypto-currencies"""
    return [get_price(crypto, fiat) for crypto in
            ['BTC', 'BCH', 'ETH', 'LTC']]


def set_fiat(fiat):
    """Sets the default fiat currency for the user"""
    try:
        config.set('currency', 'FIAT', fiat)
        with open(config_filename, 'w') as configfile:
            config.write(configfile)
        return "[*] {} configured as standard fiat".format(fiat)
    except Exception as e:
        return "[*] error while configuring fiat, report: ", e


def main():
    """Main program entry point; parses and interprets command line arguments"""
    parser = argparse.ArgumentParser(prog="HODL", description=description, epilog=epilog)
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('-c', '--crypto',
                        help='set the crypto-currency you wish to price check',
                        choices=['BTC', 'BCH', 'ETH', 'LTC'])
    group.add_argument('-f', '--fiat',
                       help='set the fiat currency you wish to use for comparison')
    group.add_argument('-sf', '--set_fiat',
                       help='set your preferred fiat currency')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s {version}'.format(
                            version=__version__))
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
