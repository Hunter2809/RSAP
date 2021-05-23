"""
    An Example telling about how to use this module's AI feature on command line (sync)
"""

from rsap import RSAP

chatbot = RSAP("api_key")  # Put your own API KEY here


print(chatbot.ai_response("Hey"))
