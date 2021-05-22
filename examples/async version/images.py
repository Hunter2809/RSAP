"""
    An Example telling about how to use this module's images feature on command line (async)
"""

from rsap import AsyncRSAP
from asyncio import run

images_bot = AsyncRSAP("api_key")  # Put your own API KEY here


print(run(images_bot.image()))
