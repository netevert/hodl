import argparse
import hodl


def create_parser():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('-c', '--crypto',
                        help='the crypto you wish to price check',
                        choices=['BTC', 'BCH', 'ETH', 'LTC'])
    group.add_argument('-f', '--fiat',
                       help='the fiat currency you wish to use for comparison')
    group.add_argument('-sf', '--set_fiat',
                       help='set your preferred fiat currency')
    parser.add_argument('-v', '--version', action='version',
                        version='HODL {version}'.format(
                            version=hodl.__version__))
    return parser
