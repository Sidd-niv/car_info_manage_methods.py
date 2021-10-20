"""
Document:   Car showroom info management system
Created on: 23rd of September 2021, 6:30:12 PM
Last updated : 30th of September 2021, 12 PM
"""


class Error(Exception):
    pass


class InputInvalid(Error):
    """Raise when input is not valid"""
    pass


class YearSizeInvalid(Error):
    """Raise when input length is greater or less than 4"""
    pass
