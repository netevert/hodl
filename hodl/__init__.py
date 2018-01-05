#!bin/python
from __future__ import print_function, unicode_literals

try:
    from urllib.request import urlopen, Request, HTTPError
    import configparser as cp
except ImportError:
    import ConfigParser as cp
    from urllib2 import urlopen, Request, HTTPError
import argparse
from colorama import init, Fore
import json
import os

init(autoreset=True)

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
        return "1 {} = {} {} | ".format(data['data']['base'],
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


def record_data(section, base, amount):
    """Helper function to save data to config.ini"""
    try:
        config.set(section, base, str(amount))
        with open(config_filename, 'w') as configfile:
            config.write(configfile)
        if section == "portfolio":
            print("[*] {} portfolio value set at {} coins".format(base.upper(), amount))
    except Exception as e:
        print(e)


def print_portfolio_value(base=None):
    """Prints the value of the user's portfolio holdings"""
    portfolio_currency = config.get("currency", "FIAT")
    if base:
        holding = float(config.get("portfolio", base)) * float(config.get("readings", base))
        print("[*] {} portfolio value: ".format(base) +
              "{0:.2f} ".format(holding) +
              "{}".format(portfolio_currency))
    else:
        for base in ["btc", "bch", "eth", "ltc"]:
            holding = float(config.get("portfolio", base)) * float(config.get("readings", base))
            print("[*] {} portfolio value: ".format(base) +
                  "{0:.2f} ".format(holding) +
                  "{}".format(portfolio_currency))


def print_report(report):
    """Prints a crypto-currency exchnge rate report"""
    if "[*] error, check you are using correct crypto and fiat symbols" in report:
        print(report)
    else:
        base = report.split("=")[0].split(" ")[1]
        current_amount = float(report.split("=")[1].split(" ")[1])
        # recover cached record
        previous_amount = float(config.get("readings", base.upper()))
        if current_amount > previous_amount:
            change = Fore.GREEN + "{0:.2f}% increase".format(100.0 * current_amount / previous_amount - 100)
            print(report + change)
            record_data("readings", base, str(current_amount))
        elif current_amount < previous_amount:
            change = Fore.RED + "{0:.2f}% decrease".format(100.0 * current_amount / previous_amount - 100)
            print(report + change)
            record_data("readings", base, str(current_amount))
        elif current_amount == previous_amount:
            change = Fore.YELLOW + "no change"
            print(report + change)
            record_data("readings", base, str(current_amount))


def main():
    """Main program entry point; parses and interprets command line arguments"""
    parser = argparse.ArgumentParser(prog="HODL", description=description, epilog=epilog)
    group = parser.add_mutually_exclusive_group()
    subparsers = parser.add_subparsers(title="portfolio tools", dest='choice',
                                       description="utilities to configure and view"
                                                   " your portfolio crypto-currency holdings")
    portfolio_config = subparsers.add_parser("cp", help="configure portfolio command")
    portfolio_view = subparsers.add_parser("vp", help="view portfolio command")
    portfolio_config.add_argument('-btc', type=int, help="set your bitcoin portfolio value")
    portfolio_view.add_argument('-btc', action='store_true', help="view your bitcoin portfolio value")
    portfolio_config.add_argument('-bch', type=int, help="set your bitcoin cash portfolio value")
    portfolio_view.add_argument('-bch', action='store_true', help="view your bitcoin cash portfolio value")
    portfolio_config.add_argument('-eth', type=int, help="view your ethereum portfolio value")
    portfolio_view.add_argument('-eth', action='store_true', help="view your ethereum portfolio value")
    portfolio_config.add_argument('-ltc', type=int, help="set your litecoin portfolio value")
    portfolio_view.add_argument('-ltc', action='store_true', help="view your litecoin portfolio value")
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
        print_report(get_price(args.crypto, args.fiat))
    elif (args.set_fiat and args.crypto) or (args.crypto and args.set_fiat):
        print(set_fiat(args.set_fiat))
        print_report(get_price(args.crypto))
    elif args.crypto:
        print_report(get_price(args.crypto))
    elif args.set_fiat:
        print(set_fiat(args.set_fiat))
    elif args.choice == "cp":  # check if portfolio configuration invoked
        if args.btc or args.btc == 0:
            record_data("portfolio", "btc", args.btc)
        elif args.bch or args.bch == 0:
            record_data("portfolio", "bch", args.bch)
        elif args.eth or args.eth == 0:
            record_data("portfolio", "eth", args.eth)
        elif args.ltc or args.ltc == 0:
            record_data("portfolio", "ltc", args.ltc)
        else:
            portfolio_config.print_help()
    elif args.choice == "vp":
        if args.btc:
            print_portfolio_value("btc")
        elif args.bch:
            print_portfolio_value("bch")
        elif args.eth:
            print_portfolio_value("eth")
        elif args.ltc:
            print_portfolio_value("ltc")
        else:
            print_portfolio_value()
    else:
        for report in get_majors():
            print_report(report)


if __name__ == '__main__':
    main()
