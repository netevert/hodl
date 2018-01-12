HODL
------
.. image:: https://img.shields.io/pypi/v/hodl.svg
    :target: https://pypi.python.org/pypi/hodl/1.0.0.dev3

.. image:: https://img.shields.io/pypi/status/hodl.svg
    :target: https://pypi.python.org/pypi/hodl/1.0.0.dev3

.. image:: https://img.shields.io/pypi/pyversions/hodl.svg
    :target: https://pypi.python.org/pypi/hodl/1.0.0.dev3

.. image:: https://travis-ci.org/errantbot/hodl.svg?branch=dev
    :target: https://travis-ci.org/errantbot/hodl

.. image:: https://coveralls.io/repos/github/errantbot/hodl/badge.svg?branch=master
    :target: https://coveralls.io/github/errantbot/hodl?branch=master

HODL is your friendly, no-nonsense tool to instantaneously check cryptocurrency
prices on the command line, helping you HODL one day at a time :)

Running HODL is easy::

    C:\>hodl
    1 BTC = 13507.09 USD  -0.14% decrease
    1 BCH = 2519.86 USD   0.23% increase
    1 ETH = 1229.74 USD   no change
    1 LTC = 231.01 USD    -0.15% decrease

Installation
------------

To install HODL run::

    pip install hodl

Features
--------

Set preferred conversion currency::

    C:\>hodl -sf USD
    [*] USD configured as standard fiat

View price for a single cryptocurrency::

    C:\>hodl -c btc
    1 BTC = 13500.01 USD  -0.05% decrease

Convert the price for a single cryptocurrency against your preferred fiat currency::

    C:\>hodl -c ltc -f CHF
    1 LTC = 223.93 CHF  -3.06% decrease

View total value of portfolio holdings::

    C:\>hodl -vp
    [*] BTC portfolio value: 123475.20 USD
    [*] BCH portfolio value: 234.15 USD
    [*] ETH portfolio value: 672.00 USD
    [*] LTC portfolio value: 120.05 USD

Configure portfolio holdings::

    C:\hodl -cp btc 15
    [*] BTC portfolio value set at 15 coins

**HODL is under active development**, consult the `GitHub issue tracker <https://github.com/errantbot/hodl/issues>`_ to
check what's in the development pipeline.

Bugs/Requests/Contributing
-------------

Please use the `GitHub issue tracker <https://github.com/errantbot/hodl/issues>`_ to submit bugs or request features.

To contribute please consult the `contribution guide <https://github.com/errantbot/hodl/blob/dev/CONTRIBUTING.md>`_.

License
-------

Distributed under the terms of the `MIT`_ license, HODL is free and open source software.

.. _`MIT`: https://github.com/errantbot/hodl/blob/master/LICENSE.txt

Versioning
----------

This project adheres to `Semantic Versioning <http://semver.org/>`_.

Donations
----------

If you like HODL please consider donating::

    Bitcoin:  13i3hFGN1RaQqdeWqmPTMuYEj9FiJWuMWf
    Litecoin: LZqLoRNHvJyuKz99mNAgVUj6M8iyEQuio9

