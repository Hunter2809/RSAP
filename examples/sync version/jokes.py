"""
    An Example telling about how to use this module's jokes feature on command line (sync)
"""

from rsap import RSAP

jokes_bot = RSAP("api_key")  # Put your own API KEY here


print(jokes_bot.joke())
