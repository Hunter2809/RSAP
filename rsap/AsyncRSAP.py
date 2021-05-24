import aiohttp
from uuid import uuid4
from random import choice

__all__ = ["AsyncRSAP"]


class RSAPException(Exception):
    pass


class InvalidKey(RSAPException):
    pass


class InvalidArgument(RSAPException):
    pass


class AsyncRSAP:
    def __init__(self, api_key: str, **kwargs) -> None:
        """The async class for interacting with the Random Stuff API. It uses the aioHTTP module to get the responses from the API..

        Args:
            api_key (str): The API key which you can get from https://api-info.pgamerx.com/register
            dev_name (str, optional): The name of the developer who coded the chatbot. Used in responses. Defaults to None.
            unique_id (str, optional): The Unique ID to create custom sessions for each user. Defaults to None.
            bot_name (str, optional): The name of the chatbot. Used in responses. Defaults to None.
            type (str, optional): The type of API to use. Stable is recommended but can also be `unstable`. Defaults to "stable".
            language (str, optional): The language to chat with the chatbot in. Defaults to "en".
            plan(str, optional): The plan, if any, that you have subscribed to.
        """
        self.key = api_key,
        if self.api_key == "":
            raise InvalidKey(
                "The API key you provided is not a valid one. Please recheck it")
        self.dev = kwargs.get("dev_name", "Hunter"),
        self.bot = kwargs.get("bot_name", "PyChat"),
        self.type = kwargs.get("type", "stable"),
        self.language = kwargs.get("language", "en")
        self.plan = kwargs.get("plan", None)
        if self.plan not in self.plans and self.plan is not None:
            raise InvalidArgument(
                "The plan you mentioned is not valid")
        if self.plan in self._plans:
            pass
        self.headers = {"x-api-key": self.key[0]}
        self._plans = ("pro", "ultra", "biz", "mega")
        self._jokes_types = ("any", "dev", "spooky", "pun")
        self._image_types = ("aww", "duck", "dog", "cat", "memes",
                             "dankmemes", "holup", "art", "harrypottermemes", "facepalm")
        self.ai_links = ("https://api.pgamerx.com/v3/pro/ai/response", "https://api.pgamerx.com/v3/ultra/ai/response",
                         "https://api.pgamerx.com/v3/biz/ai/response", "https://api.pgamerx.com/v3/mega/ai/response")
        self.working_ai_links = []

    async def ai_response(self, message: str, unique_id: str = None) -> str:
        """The async method to get the AI response to a given message

        Args:
            message (str): The message to get the response of
            unique_id (str): The Unique ID to create custom sessions for each user. Defaults to None.

        Raises:
            InvalidKey: The exception raised when a wrong key is provided and the API returns a 401 error code

        Returns:
            str: The response recieved from the API
        """
        params = {"unique_id": unique_id or str(uuid4()), "dev_name": self.dev or "Hunter",
                  "bot_name": self.bot or "PyChat", "language": self.language or "en", "message": message, "type": self.type or "stable"}
        async with aiohttp.ClientSession(headers=self.headers) as ses:
            if self.plan is None:
                for link in self.ai_links:
                    async with ses.get(link, params=params) as response:
                        if response.status == 401:
                            return
                        if response.status == 200:
                            self.working_ai_links.append(link)
            if self.plan is not None:
                async with ses.get(f"https://api.pgamerx.com/v3/{self.plan}/ai/response", params=params) as response:
                    text = await response.json()
                    if response.status == 401:
                        async with ses.get(
                                "https://api.pgamerx.com/v3/ai/response", params=params) as response:
                            text = await response.json()
                            if response.status == 401:
                                raise InvalidKey(
                                    "The API key you provided is not a valid one. Please recheck it")
                            if response.status == 200:
                                return text[0]["message"]
                    if response.status == 200:
                        return text[0]["message"]
            if len(self.working_ai_links) == 0:
                async with ses.get("https://api.pgamerx.com/v3/ai/response", params=params) as response:
                    text = await response.json()
                    if response.status == 401:
                        raise InvalidKey(
                            "The API key you provided is not a valid one. Please recheck it")
                    if response.status == 200:
                        return text[0]["message"]
            if len(self.working_ai_links) != 0:
                async with ses.get(self.working_ai_links[0], params=params) as response:
                    text = await response.json()
                    if response.status == 401:
                        async with ses.get(
                                "https://api.pgamerx.com/v3/ai/response", params=params) as response:
                            text = await response.json()
                            if response.status == 401:
                                raise InvalidKey(
                                    "The API key you provided is not a valid one. Please recheck it")
                            if response.status == 200:
                                return text[0]["message"]
                    if response.status == 200:
                        return text[0]["message"]

    async def joke(self, type: str = "any") -> dict:
        f"""The async method to get a joke of a given category

        Args:
            type (str, optional): The type of the joke to get. The types supported are {self._jokes_types}. Defaults to "any".

        Raises:
            InvalidArgument: The exception raised when a non existing type is provided

            InvalidKey: The exception raised when a wrong key is provided and the API returns a 401 error code

        Returns:
            dict: The dict of the joke recieved. The dict is in the form of {{category: the joke category, type: the joke type, joke: the joke, language: the joke language, flags: the flags of the joke}}
            Category --> The category to which the joke belongs, like `Christmas`
            Type --> If the joke consists of two strings or one.
                     If the joke type is `twopart`, then the `joke` key is a list, with the first element being the question and second being the answer
                     If the joke type is `joke`, then the `joke` key is simply the joke
            Joke --> The main joke
            Flags --> The list of flags associated with the joke. If all the flags are False, then there would be no key named `flags`. There are numerous flags, which are named below -> 
                      -> NSFW
                      -> Religious
                      -> Political
                      -> Racist
                      -> Sexist
                      -> Explicit
            Language --> The language of the joke (mostly `en`)
        """
        if type.lower() not in self._jokes_types:
            raise InvalidArgument(
                "The arguments you specified is not a valid type")
        if type.lower() in self._jokes_types:
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.get(url=f'https://api.pgamerx.com/v3/joke/{type}') as response:
                    if response.status == 401:
                        raise InvalidKey(
                            "The API key you provided is not a valid one. Please recheck it")
                    text = await response.json()
                    joke_category = text["category"]
                    joke_type = text["type"]
                    flags = []
                    for flag in text["flags"].keys():
                        if text["flags"][flag] == "False":
                            return
                        if text["flags"][flag] == "True":
                            flags.append(flag)
                    if joke_type != "twopart":
                        joke = text["joke"]
                    if joke_type == "twopart":
                        joke = [text["setup"], text["delivery"]]
                    joke_lang = text["lang"]
                    if len(flags) == 0:
                        joke_dict = {"category": joke_category, "type": joke_type,
                                     "joke": joke, "language": joke_lang}
                    if len(flags) != 0:
                        joke_dict = {"category": joke_category, "type": joke_type,
                                     "joke": joke, "language": joke_lang, "flags": flags}
                    return joke_dict

    async def image(self, image_type: str) -> str:
        f"""The async method to get an image from the API

        Args:
            type (str): The type of image to return. The types supported are {self._image_types}. Defaults to memes

        Raises:
            InvalidArgument: The exception raised when a non existing type is provided

            InvalidKey: The exception raised when a wrong key is provided and the API returns a 401 error code

        Returns:
            str: The image URL
        """
        image_type = image_type or choice(self._image_types)
        if image_type.lower() not in self._image_types:
            raise InvalidArgument(
                "The arguments you specified is not a valid type")
        if image_type.lower() in self._image_types:
            async with aiohttp.ClientSession(headers=self.headers) as session:
                async with session.get(url=f'https://api.pgamerx.com/v3/image/{image_type}') as response:
                    if response.status == 401:
                        raise InvalidKey(
                            "The API key you provided is not a valid one. Please recheck it")
                    text = await response.json()
                    return text[0]

    async def meme(self) -> str:
        """The dedicated async method to get a meme from the API

        Raises:
            InvalidKey: The exception raised when a wrong key is provided and the API returns a 401 error code

        Returns:
            str: The meme's image URL
        """
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url=f'https://api.pgamerx.com/v3/image/{choice(["memes", "dankmemes"])}') as response:
                if response.status == 401:
                    raise InvalidKey(
                        "The API key you provided is not a valid one. Please recheck it")
                text = await response.json()
                return text[0]
