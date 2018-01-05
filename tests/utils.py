import argparse
import hodl


def create_parser():
    """Creates a copy of hodl's argument parser for testing purposes"""
    parser = argparse.ArgumentParser()
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
                            version=hodl.__version__))
    return parser
