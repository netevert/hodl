# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
long_description = """
HODL is your friendly, no-nonsense tool to instantaneously check cryptocurrency
prices on the command line, helping you HODL one day at a time :)

Please visit the project's main documentation page, found at:
https://github.com/errantbot/hodl
"""

setup(
    name='hodl',
    version='1.0.0',
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'venv']),
    install_requires=['colorama'],  # Required,
    url='https://github.com/errantbot/hodl',
    license='MIT',
    author='errantbot',
    author_email='errantbot@tutanota.com',
    description='A  friendly, no-nonsense tool to instantaneously check '
                'cryptocurrency prices.',
    # This is an optional longer description of your project that represents
    # the body of text which users will see when they visit PyPI.
    #
    # Often, this is the same as your README, so you can just read it in from
    # that file directly (as we have already done above)
    #
    # This field corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Other Audience',
        'Intended Audience :: System Administrators',
        'Topic :: Office/Business :: Financial',
        'Topic :: Other/Nonlisted Topic',
        'Topic :: Terminals',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        # project language
        'Natural Language :: English',

        # compatible os
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
    ],
    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a string of words separated by whitespace, not a list.
    keywords="cryptocurrencies exchange-rates coinbase command-line-tool hodl bitcoin bitcoin-api litecoin "
             "litecoin-price bitcoin-price ethereum bitcoin-cash",
    # Optional

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    #
    # If using Python 2.6 or earlier, then these have to be included in
    # MANIFEST.in as well.
    package_data={  # Optional
        'hodl': ['conf/*', ],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
        'console_scripts': [
            'hodl=hodl:main',
        ], },
)
