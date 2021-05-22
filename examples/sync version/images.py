"""
    An Example telling about how to use this module's images feature on command line
"""

from rsap import RSAP

images_bot = RSAP("api_key")  # Put your own API KEY here


print(images_bot.image("optional type here"))  # Put optional type kwarg here
