![Icon](https://github.com/netevert/hodl/blob/dev/docs/icon_2.png)
==================================================================
[![Maintenance](https://img.shields.io/maintenance/yes/2018.svg)]()
[![PyPI](https://img.shields.io/pypi/v/hodl.svg)](https://pypi.python.org/pypi/hodl)
[![PyPI](https://img.shields.io/pypi/status/hodl.svg)](https://pypi.python.org/pypi/hodl)
[![PyPI](https://img.shields.io/pypi/pyversions/hodl.svg)](https://pypi.python.org/pypi/hodl)
[![Build Status](https://travis-ci.org/netevert/hodl.svg?branch=master)](https://travis-ci.org/netevert/hodl)
[![Coverage Status](https://coveralls.io/repos/github/netevert/hodl/badge.svg?branch=master)](https://coveralls.io/github/netevert/hodl?branch=master)
[![Donations](https://img.shields.io/badge/donate-bitcoin-orange.svg?logo=bitcoin)](https://github.com/netevert/hodl/blob/master/README.md#donations)

HODL is your friendly, no-nonsense tool to instantaneously check
cryptocurrency prices on the command line, helping you HODL one day at a
time :)


Running HODL is easy:

![Demo](https://github.com/netevert/hodl/blob/master/docs/demo.gif)

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
- Dash ([DASH](https://www.dash.org/))
- Zcash ([ZEC](https://z.cash/))

<details><summary>View price percentage variations between lookups</summary>
<p>

    C:\>hodl -r
    [*] generating price change report
    1 BTC = 11092.47 USD  -0.07%
    1 BCH = 1243.01 USD   -0.12%
    1 ETH = 849.53 USD    -0.06%
    1 LTC = 208.18 USD     0.00%
    1 XMR = 347.17 USD     0.03%
    1 XRP = 0.92 USD       0.00%
    1 DASH = 599.18 USD   -0.07%
    1 ZEC = 389.29 USD    -0.03%
</p>
</details>

<details><summary>Set preferred conversion currency</summary>
<p>

    C:\>hodl -sf USD
    [*] updating standard fiat to USD ...
    [*] success: USD configured as standard fiat
</p>
</details>

<details><summary>View price for a single cryptocurrency</summary>
<p>

    C:\>hodl -c btc
    1 BTC = 13500.01 USD
    
</p>
</details>

<details><summary>Convert the price for a single cryptocurrency against your preferred
fiat currency</summary>
<p>

    C:\>hodl -cc btc ltc
    1 BTC = 61.36111727 LTC
</p>
</details>

<details><summary>Convert the price for a single cryptocurrency against another cryptocurrency</summary>
<p>

    C:\>hodl -c ltc -f CHF
    1 LTC = 223.93 CHF
</p>
</details>

<details><summary>View total value of portfolio holdings</summary>
<p>

    C:\>hodl -vp
    [*] BTC portfolio value: 123475.20 USD
    [*] BCH portfolio value: 234.15 USD
    [*] ETH portfolio value: 672.00 USD
    [*] LTC portfolio value: 120.05 USD
    [*] XMR portfolio value: 1122.43 USD
    [*] XRP portfolio value: 0.00 USD
    [*] DASH portfolio value: 0.00 USD
    [*] ZEC portfolio value: 0.00 USD
</p>
</details>

<details><summary>Configure portfolio holdings</summary>
<p>

    C:\hodl -cp btc 15
    [*] BTC portfolio value set at 15 coins
</p>
</details>
<p></p>

**HODL is under active development**, consult the [GitHub issue tracker](https://github.com/errantbot/hodl/issues)
to check what\'s in the development pipeline.

Bugs/Requests/Contributing
==========================

Please use the [GitHub issue tracker](https://github.com/netevert/hodl/issues) to submit bugs or request
features.

To contribute please consult the [contribution guide](https://github.com/netevert/hodl/blob/master/CONTRIBUTING.md).

License
=======

Distributed under the terms of the [MIT](http://www.linfo.org/mitlicense.html) license, HODL is free and open
source software.

Versioning
==========

This project adheres to [Semantic Versioning](https://semver.org/).

Donations
=========

<details><summary>If you like HODL please consider donating</summary>
<p>
    
    Bitcoin:  13i3hFGN1RaQqdeWqmPTMuYEj9FiJWuMWf
    Litecoin: LZqLoRNHvJyuKz99mNAgVUj6M8iyEQuio9
</p>
</details>
