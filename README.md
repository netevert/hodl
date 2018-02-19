![Icon](https://github.com/errantbot/hodl/blob/dev/docs/icon.png)
=================================================================
[![PyPI](https://img.shields.io/pypi/v/hodl.svg)](https://pypi.python.org/pypi/hodl)
[![PyPI](https://img.shields.io/pypi/status/hodl.svg)](https://pypi.python.org/pypi/hodl)
[![PyPI](https://img.shields.io/pypi/pyversions/hodl.svg)](https://pypi.python.org/pypi/hodl)
[![Build Status](https://travis-ci.org/errantbot/hodl.svg?branch=master)](https://travis-ci.org/errantbot/hodl)
[![Coverage Status](https://coveralls.io/repos/github/errantbot/hodl/badge.svg?branch=master)](https://coveralls.io/github/errantbot/hodl?branch=master)
[![Donations](https://img.shields.io/badge/donate-bitcoin-orange.svg?logo=bitcoin)](https://github.com/errantbot/hodl/tree/master#donations)

HODL is your friendly, no-nonsense tool to instantaneously check
cryptocurrency prices on the command line, helping you HODL one day at a
time :)

Running HODL is easy:

![Demo](https://github.com/errantbot/hodl/blob/master/docs/demo.gif)

Installation
============

To install HODL run:

    pip install hodl

Features
========
Currencies supported:
- Bitcoin ([BTC](https://bitcoin.org/en/))
- Bitcoin Cash ([BCH](https://www.bitcoincash.org/))
- Ethereum ([ETH](https://www.ethereum.org/))
- Litecoin ([LTC](https://litecoin.com/))
- Monero ([XMR](https://getmonero.org/))
- Ripple ([XRP](https://ripple.com/))

Set preferred conversion currency:

    C:\>hodl -sf USD
    [*] USD configured as standard fiat

View price for a single cryptocurrency:

    C:\>hodl -c btc
    1 BTC = 13500.01 USD  -0.05% decrease

Convert the price for a single cryptocurrency against your preferred
fiat currency:

    C:\>hodl -cc btc ltc
    1 BTC = 61.36111727 LTC

Convert the price for a single cryptocurrency against another cryptocurrency:

    C:\>hodl -c ltc -f CHF
    1 LTC = 223.93 CHF  -3.06% decrease

View total value of portfolio holdings:

    C:\>hodl -vp
    [*] BTC portfolio value: 123475.20 USD
    [*] BCH portfolio value: 234.15 USD
    [*] ETH portfolio value: 672.00 USD
    [*] LTC portfolio value: 120.05 USD
    [*] XMR portfolio value: 1122.43 USD
    [*] XRP portfolio value: 0.00 USD

Configure portfolio holdings:

    C:\hodl -cp btc 15
    [*] BTC portfolio value set at 15 coins

**HODL is under active development**, consult the [GitHub issue tracker](https://github.com/errantbot/hodl/issues)
to check what\'s in the development pipeline.

Bugs/Requests/Contributing
==========================

Please use the [GitHub issue tracker](https://github.com/errantbot/hodl/issues) to submit bugs or request
features.

To contribute please consult the [contribution guide](https://github.com/errantbot/hodl/blob/master/CONTRIBUTING.md).

License
=======

Distributed under the terms of the [MIT](http://www.linfo.org/mitlicense.html) license, HODL is free and open
source software.

Versioning
==========

This project adheres to [Semantic Versioning](https://semver.org/).

Donations
=========

If you like HODL please consider donating:

    Bitcoin:  13i3hFGN1RaQqdeWqmPTMuYEj9FiJWuMWf
    Litecoin: LZqLoRNHvJyuKz99mNAgVUj6M8iyEQuio9
