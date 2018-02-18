#!bin/python
from __future__ import print_function, unicode_literals

try:
    from urllib.request import urlopen, Request, HTTPError
    import configparser as cp
except ImportError:
    import ConfigParser as cp
    from urllib2 import urlopen, Request, HTTPError
import argparse
from colorama import init, Fore, Back
from concurrent.futures import ThreadPoolExecutor
import json
import os

init(autoreset=True)

# constants
description = "Your friendly, no-nonsense tool to " \
              "instantaneously check cryptocurrency prices"
epilog = "hodl.py: helping you HODL one day at a time :)"
__version__ = "v.1.1.0"
cryptos = ['btc', 'bch', 'eth', 'ltc', 'xmr', 'xrp']
iso4217codes = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG",
                "AZN",
                "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB",
                "BRL",
                "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP",
                "CNY",
                "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP",
                "DZD",
                "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GGP",
                "GHS",
                "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG",
                "HUF",
                "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD",
                "JOD",
                "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD",
                "KZT",
                "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA",
                "MKD",
                "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR",
                "MZN",
                "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN",
                "PGK",
                "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF",
                "SAR",
                "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SPL",
                "SRD",
                "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP",
                "TRY",
                "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS",
                "VEF",
                "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER",
                "ZAR",
                "ZMW", "ZWD"]

# load config file
config_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                               'conf', 'config.ini')
config = cp.ConfigParser()
config.read(config_filename)


def binance_convert_crypto(frm="LTC", to="BTC"):
    """Returns the conversion price from one cypto to another
    using the binance API"""
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol={}{}".format(
            frm.upper(), to.upper())
        req = Request(url)
        r = urlopen(req).read()
        data = json.loads(r.decode("utf-8"))
        return "1 {} = {} {}".format(frm.upper(), data["price"], to.upper())
    except HTTPError:
        try:
            url = "https://api.binance.com/api/v3/" \
                  "ticker/price?symbol={}{}".format(to.upper(), frm.upper())
            req = Request(url)
            r = urlopen(req).read()
            data = json.loads(r.decode("utf-8"))
            return "1 {} = {} {}".format(frm.upper(),
                                         1.0 / float(data["price"]), to.upper())
        except HTTPError:
            return "[*] error, check you are using correct crypto symbols"


def coinbase_convert_crypto(frm="LTC", to="BTC"):
    """Returns the conversion price between the supplied crypto
    and fiat currencies using the coinbase API"""
    try:
        if frm in ['btc', 'bch', 'eth', 'ltc'] and \
                to in ['btc', 'bch', 'eth', 'ltc']:
            url = "https://api.coinbase.com/v2/prices/{}-{}/spot"
            req = Request(url.format(frm.upper(), "USD"))
            r = urlopen(req).read()
            data = json.loads(r.decode("utf-8"))
            frm_price = float(data["data"]["amount"])
            req = Request(url.format(to.upper(), "USD"))
            r = urlopen(req).read()
            data = json.loads(r.decode("utf-8"))
            to_price = float(data["data"]["amount"])
            return "1 {} = {} {}".format(frm.upper(),
                                         round(frm_price /
                                               to_price, 8), to.upper())
        else:
            return "1 {} = {} {}".format(frm.upper(),
                                         str(binance_convert_crypto(frm, to)),
                                         to.upper())
    except (HTTPError, IndexError):
        return "[*] error, check that you are using correct crypto symbols"


def get_price(crypto="BTC", fiat=config.get("currency", "FIAT")):
    """Returns the conversion price between the supplied
    crypto and fiat currencies"""
    try:
        if crypto in ['btc', 'bch', 'eth', 'ltc']:
            url = 'https://api.coinbase.com/v2/prices/{}-{}/spot'.format(
                crypto.upper(),
                fiat)
            req = Request(url)
            r = urlopen(req).read()
            data = json.loads(r.decode('utf-8'))
            return "1 {} = {} {}".format(data['data']['base'],
                                         data['data']['amount'],
                                         data['data']['currency'])
        else:
            return "1 {0} = {1:.2f} {2}".format(crypto.upper(),
                                                get_crypto_price(crypto, fiat),
                                                fiat)
    except (HTTPError, IndexError):
        return "[*] error, check you are using correct crypto and fiat symbols"


def get_crypto_price(crypto, fiat):
    """Helper function to convert any cryptocurrency to fiat"""
    converted_btc_value = float(binance_convert_crypto(
        crypto, "BTC").split('=')[1].strip().split()[0])

    # grab latest bitcoin price
    btc_price = float(get_price("btc", fiat).split('=')[1].strip().split()[0])
    # converted_btc_value * latest reading
    return converted_btc_value * btc_price


def get_majors(fiat=config.get("currency", "FIAT")):
    """Returns the conversion prices for all supported crypto-currencies"""
    reports = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        for crypto in cryptos:
            future = executor.submit(get_price, crypto.lower(), fiat)
            reports.append(future.result())
    return reports


def set_fiat(fiat):
    """Sets the default fiat currency for the user"""
    # todo: data sanitisation, restrict fiat to ISO 4217 codes
    try:
        config.set('currency', 'FIAT', fiat)
        with open(config_filename, 'w') as configfile:
            config.write(configfile)
        return "[*] {} configured as standard fiat".format(fiat)
    except Exception as e:
        return "[*] error while configuring fiat, report: ", e


def record_data(section, base, amount):
    """Helper function to sanitise and save data to config.ini"""
    try:
        if float(amount) >= 0:
            config.set(section, base, str(amount))
            with open(config_filename, 'w') as configfile:
                config.write(configfile)
            if section == "portfolio":
                print("[*] {} portfolio value set at {} coins".format(
                    base.upper(), amount))
        else:
            print(
                "HODL: error: invalid choice: {} "
                "(please supply a positive number)".format(
                    amount))
    except ValueError:
        print("HODL: error: invalid choice: {} (please supply a number)".format(
            amount))


def print_portfolio_value(base=None):
    """Prints the value of the user's portfolio holdings"""
    portfolio_currency = config.get("currency", "FIAT")
    if base:
        holding = float(config.get("portfolio", base)) * float(
            config.get("readings", base))
        print("[*] {} portfolio value: ".format(base.upper()) +
              "{0:.2f} ".format(holding) +
              "{}".format(portfolio_currency))
    else:
        for base in cryptos:
            holding = float(config.get("portfolio", base)) * float(
                config.get("readings", base))
            print("[*] {} portfolio value: ".format(base.upper()) +
                  "{0:.2f} ".format(holding) +
                  "{}".format(portfolio_currency))


def print_report(report, alignment=0, first_run=False):
    """Prints a crypto-currency exchange rate report"""
    i = alignment - len(report) + 2
    try:
        if "[*] error, check you are using correct " \
           "crypto and fiat symbols" in report:
            print(report)
        else:
            base = report.split("=")[0].split(" ")[1]
            current_amount = float(report.split("=")[1].split(" ")[1])
            # recover cached record
            previous_amount = float(config.get("readings", base.upper()))
            if current_amount > previous_amount and not first_run:
                change = Fore.WHITE + " ".rjust(
                    i) + Back.GREEN + " {0:.2f}%".format(
                    100.0 * current_amount / previous_amount - 100)
                print(report + change)
            elif current_amount < previous_amount and not first_run:
                change = Fore.WHITE + " ".rjust(
                    i) + Back.RED + "{0:.2f}%".format(
                    100.0 * current_amount / previous_amount - 100)
                print(report + change)
            elif current_amount == previous_amount and not first_run:
                change = Fore.WHITE + " ".rjust(i) + Back.BLUE + " 0.00%"
                print(report + change)
            elif first_run:
                print(report)
            record_data("readings", base, str(current_amount))
    except ZeroDivisionError:
        # all readings in the config are set to 0, meaning the user is running
        # the script for the first time. We can thus skip calculating the
        # percentage change in the report by setting first_run to True
        base = report.split("=")[0].split(" ")[1]
        current_amount = float(report.split("=")[1].split(" ")[1])
        record_data("readings", base, str(current_amount))
        print_report(report=report, first_run=True)


def main():
    """Main program entry point; parses and interprets command line arguments"""
    parser = argparse.ArgumentParser(prog="HODL", description=description,
                                     epilog=epilog)
    group = parser.add_mutually_exclusive_group()
    group_2 = parser.add_mutually_exclusive_group()
    group_2.add_argument("-cp", "--configure_portfolio",
                         help="configure portfolio command",
                         nargs=2, metavar=('CRYPTOCURRENCY', 'AMOUNT'))
    group_2.add_argument("-vp", "--view_portfolio",
                         help="view portfolio command", const='all', nargs="?")
    parser.add_argument('-c', '--crypto',
                        help='set the crypto-currency you wish to price check',
                        choices=cryptos)
    group.add_argument('-f', '--fiat',
                       help='set fiat conversion currency',
                       choices=iso4217codes,
                       metavar="ISO 4217 CODE")
    group.add_argument('-sf', '--set_fiat',
                       help='set your preferred fiat currency',
                       choices=iso4217codes,
                       metavar="ISO 4217 CODE")
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s {version}'.format(
                            version=__version__))
    parser.add_argument('-cc', '--convert_crypto',
                        help="convert one crypto to another",
                        choices=cryptos,
                        nargs=2)
    args = parser.parse_args()

    if args.crypto and args.fiat:
        report = get_price(args.crypto, args.fiat)
        print_report(report, len(report))
    elif (args.set_fiat and args.crypto) or (args.crypto and args.set_fiat):
        print(set_fiat(args.set_fiat))
        report = get_price(args.crypto)
        print_report(report, len(report))
    elif args.crypto:
        report = get_price(args.crypto)
        print_report(report, len(report))
    elif args.set_fiat:
        print(set_fiat(args.set_fiat))
    elif args.configure_portfolio:
        if args.configure_portfolio[0] in cryptos:
            record_data("portfolio", args.configure_portfolio[0],
                        args.configure_portfolio[1])
        else:
            print(
                "HODL: error: argument -cp/--configure_portfolio: invalid choice:"
                " '{}' (choose from {})".format(
                    args.configure_portfolio[0],
                    [str(crypto) for crypto in cryptos]))
    elif args.view_portfolio:
        if args.view_portfolio == "all":
            print_portfolio_value()
        else:
            if args.view_portfolio in cryptos:
                print_portfolio_value(args.view_portfolio)
            else:
                print(
                    "HODL: error: argument -vp/--view_portfolio: invalid choice:"
                    " '{}' (choose from {})".format(
                        args.view_portfolio,
                        [str(crypto) for crypto in cryptos]))
    elif args.convert_crypto:
        if args.convert_crypto[0] in cryptos \
                and args.convert_crypto[1] in cryptos:
            print(coinbase_convert_crypto(args.convert_crypto[0],
                                          args.convert_crypto[1]))
        else:
            print("HODL: error: argument -cc/--convert_crypto: invalid choice:"
                  " '{}' (choose from {})".format(
                args.view_portfolio, [str(crypto) for crypto in cryptos]))

    else:
        reports = get_majors()
        i = len(max(reports, key=len))
        for report in reports:
            print_report(report, i)


if __name__ == '__main__':
    main()
