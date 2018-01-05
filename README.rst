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
    1 BTC = 14960.63 USD | -0.05% decrease
    1 BCH = 2362.93 USD | 0.00% increase
    1 ETH = 953.00 USD | 0.15% increase
    1 LTC = 233.41 USD | 0.10% increase

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

    C:\>hodl -c BTC
    1 BTC = 14953.41 USD | -0.05% decrease

Convert the price for a single cryptocurrency against your preferred fiat currency::

    C:\>hodl -c LTC -f CHF
    1 LTC = 227.56 CHF | -2.51% decrease

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

Distributed under the terms of the `MIT`_ license, pytest is free and open source software.

.. _`MIT`: https://github.com/errantbot/hodl/blob/master/LICENSE.txt

Versioning
----------

This project adheres to `Semantic Versioning <http://semver.org/>`_.

Donations
----------

If you like HODL please consider donating::

    Bitcoin:  13i3hFGN1RaQqdeWqmPTMuYEj9FiJWuMWf
    Litecoin: LZqLoRNHvJyuKz99mNAgVUj6M8iyEQuio9

