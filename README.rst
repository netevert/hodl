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
    1 BTC = 13864.74 USD
    1 BCH = 2468.34 USD
    1 ETH = 734.34 USD
    1 LTC = 230.11 USD

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

    C:\>hodl -c LTC
    1 LTC = 229.32 USD

Convert the price for a single cryptocurrency against preferred fiat currency::

    C:\>hodl -c BTC -f CHF
    1 BTC = 13506.89 CHF

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

If you like HODL and would like to donate, please send Litecoins to::

    LZqLoRNHvJyuKz99mNAgVUj6M8iyEQuio9

