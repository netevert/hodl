# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [1.2.0] - unreleased
### Added
- DASH support
- ZEC support
- Improved documentation
- New icon

### Changed
- Moved price change report under a dedicated argument (-r)

### Fixed
- Improved speed of price lookups

### Removed
- Price change reports from single cryptocurrency price and conversion lookups

## [1.1.2] - 2018-03-01
### Changed
- Project ownership
- Updated homepage links to new project owner
- Updated license references to new project owner

### Fixed
- Broken travis links and setup

## [1.1.1] - 2018-02-28
### Added
- Maintenance status badge on README.md

### Changed
- Updated changelog
- Updated contribution guide

### Fixed
- Fixed bug that caused incorrect price change percentage reports to be
displayed when fiat currency is changed

## [1.1.0] - 2018-02-18
### Added
- Changelog file
- XMR support
- XRP support
- Crypto to crypto exchange rates
- Multi-threading to speed up price retrieval
- Interim project icon
- Donations badge

### Changed
- Colorized output: colorized background in price data for more intuitive reading
- Updated setup.py
- Updated requirements.txt
- Updated demo GIF

### Removed
- Verbose price reports

## [1.0.0] - 2018-01-17
### Added
- Video demo to documentation
- User portfolio
- Colorized output
- Added docstrings
- Improved documentation
- Contribution guide
- Version argument
- Travis continuous integration
- Test suite

### Changed
- Converted readme from .rst to .md
- Updated setup.py

### Fixed
- Align the formatting of the currency exchange rate report
- Increased code coverage to 100%
- Restricted fiat selection to ISO 4217 codes
- Applied minor fixes to setup.py description
- Improved argparse user help menu
- Improved project description in setup.py
