import hodl
from tests.utils import create_parser


def test_get_price():
    """Tests the output of get_price()"""
    out = hodl.get_price(crypto="BTC", fiat="USD")
    assert "1 BTC =" in out
    assert "USD" in out
    # test HTTPError handling
    out = hodl.get_price(crypto="ABC")
    assert "[*] error, check you are using " \
           "correct crypto and fiat symbols" in out


def test_get_majors():
    """Tests the output of get_majors()"""
    out = hodl.get_majors(fiat="USD")
    assert "1 BTC =" and "USD" in out[0]
    assert "1 BCH =" and "USD" in out[1]
    assert "1 ETH =" and "USD" in out[2]
    assert "1 LTC =" and "USD" in out[3]


def test_set_fiat():
    """Tests the output and behavior of set_fiat()"""
    try:
        import configparser as cp
    except ImportError:
        import ConfigParser as cp
    config = cp.ConfigParser()
    config.read('../hodl/conf/config.ini')
    backup = config.get("currency", "FIAT")
    out = hodl.set_fiat(fiat="CHF")
    config.read('../hodl/conf/config.ini')
    assert "[*] CHF configured as standard fiat" in out
    assert config.get("currency", "FIAT") == "CHF"
    # return to previous settings and test
    hodl.set_fiat(fiat=backup)
    config.read('../hodl/conf/config.ini')
    assert config.get("currency", "FIAT") == backup


def test_main():
    """Tests the output and behaviour of test_main()"""
    parser = create_parser()
    args = parser.parse_args(['-c', 'LTC'])
    assert args.crypto == 'LTC'
    args = parser.parse_args(['-f', 'GBP'])
    assert args.fiat == 'GBP'
    args = parser.parse_args(['-sf', 'USD'])
    assert args.set_fiat == 'USD'
