"""
    An Example telling about how to use this module's AI feature on command line (async)
"""

from rsap import AsyncRSAP
from asyncio import run

chatbot = AsyncRSAP("api_key")  # Put your own API KEY here

while True:
    question = input("> ")
    run(chatbot.ai_response(question))
