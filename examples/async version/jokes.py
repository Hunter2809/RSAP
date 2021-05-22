"""
    An Example telling about how to use this module's jokes feature on command line (async)
"""

from rsap import AsyncRSAP
from asyncio import run

jokes_bot = AsyncRSAP("api_key")  # Put your own API KEY here


print(run(jokes_bot.joke()))
