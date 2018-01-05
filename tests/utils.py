import argparse
import hodl


def create_parser():
    """Creates a copy of hodl's argument parser for testing purposes"""
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("-cp", "--configure_portfolio", help="configure portfolio command",
                        nargs=2, metavar=('CRYPTOCURRENCY', 'AMOUNT'))
    parser.add_argument("-vp", "--view_portfolio", help="view portfolio command", const='all', nargs="?")
    parser.add_argument('-c', '--crypto',
                        help='set the crypto-currency you wish to price check',
                        choices=hodl.cryptos)
    group.add_argument('-f', '--fiat',
                       help='set the fiat currency you wish to use for comparison')
    group.add_argument('-sf', '--set_fiat',
                       help='set your preferred fiat currency')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s {version}'.format(
                            version=hodl.__version__))
    return parser
