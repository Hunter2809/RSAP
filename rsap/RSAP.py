from uuid import uuid4
import requests
from random import choice
import logging
from rsap.exceptions import *

__all__ = ["RSAP"]


class RSAP:
    def __init__(self, api_key: str, **kwargs) -> None:
        """The sync class for interacting with the Random Stuff API. It uses the requests module to get the responses from the API..

        Args:
            api_key (str): The API key which you can get from https://api-info.pgamerx.com/register
            dev_name (str, optional): The name of the developer who coded the chatbot. Used in responses. Defaults to Hunter.
            unique_id (str, optional): The Unique ID to create custom sessions for each user. Defaults to a random uuid4 string.
            bot_name (str, optional): The name of the chatbot. Used in responses. Defaults to PyChat.
            type (str, optional): The type of API to use. Stable is recommended but can also be `unstable`. Defaults to "stable".
            language (str, optional): The language to chat with the chatbot in. Defaults to "en".
            plan(str, optional): The plan, if any, that you have subscribed to.
        """
        self.key = api_key
        if self.key == "":
            logging.critical(
                msg=f"The API Key you supplied is not a valid one... The one you supplied was {self.key}")
            raise InvalidKey(
                "The API key you provided is not a valid one. Please recheck it")
        self.dev = kwargs.get("dev_name", "Hunter")
        logging.info(msg=f"The bot's dev name is set to {self.dev}")
        self.bot = kwargs.get("bot_name", "PyChat")
        logging.info(msg=f"The bot's name is set to {self.bot}")
        self.type = kwargs.get("type", "stable")
        logging.info(msg=f"The API's type is set to {self.type}")
        self.language = kwargs.get("language", "en")
        logging.info(msg=f"The API's language is set to {self.language}")
        self.plan = kwargs.get("plan", None)
        logging.info(msg=f"The API's plan is set to {self.type or 'Free'}")
        self.plans = ("pro", "ultra", "biz", "mega")
        if self.plan not in self.plans and self.plan is not None:
            logging.error(
                msg=f"The API plan you supplied is not a valid one... The one you supplied was {self.key}. Setting it to 'Free")
            self.plan = None
        self.headers = {"x-api-key": self.key}
        logging.info(msg=f"Setting the GET request header to {self.headers}")
        self._jokes_types = ("any", "dev", "spooky", "pun")
        self._image_types = ("aww", "duck", "dog", "cat", "memes",
                             "dankmemes", "holup", "art", "harrypottermemes", "facepalm")
        self.ai_links = ("https://api.pgamerx.com/v3/pro/ai/response", "https://api.pgamerx.com/v3/ultra/ai/response",
                         "https://api.pgamerx.com/v3/biz/ai/response", "https://api.pgamerx.com/v3/mega/ai/response")
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def ai_response(self, message: str, unique_id: str = uuid4()) -> str:
        """The sync method to get the AI response to a given message

        Args:
            message (str): The message to get the response of

        Raises:
            InvalidKey: The exception raised when a wrong key is provided and the API returns a 401 error code

        Returns:
            str: The response recieved from the API
        """
        params = {"unique_id": str(unique_id), "dev_name": str(self.dev),
                  "bot_name": str(self.bot), "language": str(self.language), "message": str(message), "type": str(self.type)}
        logging.info(
            f"Setting the GET request paramss to the API. Params = {params}")
        if self.plan is None:
            logging.info(
                msg=f"You supplied either an invalid plan or wrong plan.. Checking the plans automatically")
            for link in self.ai_links:
                session = self.session.get(link, params=params)
                if session.status_code == 401:
                    session = self.session.get(
                        "https://api.pgamerx.com/v3/ai/response", params=params)
                    if session.status_code == 401:
                        logging.critical(
                            msg=f"The API Key you supplied is not a valid one... The one you supplied was {self.key}")
                        raise InvalidKey(
                            "The API Key you provided is not a valid one. Please recheck it")
                    if session.status_code == 200:
                        logging.info(
                            msg=f"You did not have a premium plan associated with this API Key.. Using the Free plan")
                        text = session.json()
                        return text[0]["message"]
                if session.status_code == 200:
                    logging.info(
                        msg=f"A premium plan associated with your API Key has been detected. Using that plan ({link})..")
                    text = session.json()
                    return text[0]["message"]
        if self.plan is not None:
            logging.info(
                msg=f"Checking if the plan you supplied is associated with your API Key or not")
            session = self.session.get(
                f"https://api.pgamerx.com/v3/{self.plan}/ai/response", params=params)
            if session.status_code == 401:
                logging.info(
                    msg=f"You did not have a premium plan associated with this API Key.. Using the Free plan")
                session = self.session.get(
                    "https://api.pgamerx.com/v3/ai/response", params=params)
                if session.status_code == 401:
                    logging.critical(
                        msg=f"The API Key you supplied is not a valid one... The one you supplied was {self.key}")
                    raise InvalidKey(
                        "The API key you provided is not a valid one. Please recheck it")
                if session.status_code == 200:
                    logging.info(
                        msg=f"You did not have a premium plan associated with this API Key.. Using the Free plan")
                    text = session.json()
                    return text[0]["message"]
            if session.status_code == 200:
                logging.info(
                    msg=f"A premium plan associated with your API Key has been detected. Using that plan (https://api.pgamerx.com/v3/{self.plan}/ai/response)..")
                text = session.json()
                return text[0]["message"]

    def joke(self, type: str = "any") -> dict:
        f"""The sync method to get a joke of a given category

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
            logging.critical(
                msg=f"The joke type you specified is not a valid one. The supplied type was {type}")
            raise InvalidArgument(
                "The arguments you specified is not a valid type")
        if type.lower() in self._jokes_types:
            logging.info(msg=f"Trying to fetch the joke from the API...")
            session = self.session.get(
                url=f'https://api.pgamerx.com/v3/joke/{type}')
            if session.status_code == 401:
                logging.critical(
                    msg=f"The API Key you supplied is not a valid one... The one you supplied was {self.key}")
                raise InvalidKey(
                    "The API key you provided is not a valid one. Please recheck it")
            logging.info(
                msg=f"Fetched the joke from the API and converting it into the dict")
            text = session.json()
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
                logging.info(
                    msg=f"The joke did not have any flags, so skipping the flags key")
            if len(flags) != 0:
                joke_dict = {"category": joke_category, "type": joke_type,
                             "joke": joke, "language": joke_lang, "flags": flags}
                logging.info(
                    msg=f"The joke had some flags, so adding the flags key")
            return joke_dict

    def image(self, image_type: str = None) -> str:
        f"""The sync method to get an image from the API

        Args:
            type (str, optional): The type of image to return. The types supported are {self._image_types}.

        Raises:
            InvalidArgument: The exception raised when a non existing type is provided

            InvalidKey: The exception raised when a wrong key is provided and the API returns a 401 error code

        Returns:
            str: The image URL
        """
        if image_type is None:
            logging.error(
                msg=f"You did not specify any image type.. Randomly choosing from the available types")
            image_type = choice(self._image_types)
        if image_type.lower() not in self._image_types:
            logging.critical(
                msg=f"The image type you specified is not a valid one. The supplied type was {image_type}")
            raise InvalidArgument(
                "The arguments you specified is not a valid type")
        if image_type.lower() in self._image_types:
            logging.info(msg=f"Trying to fetch the image from the API...")
            session = self.session.get(
                url=f'https://api.pgamerx.com/v3/image/{image_type}')
            if session.status_code == 401:
                logging.critical(
                    msg=f"The API Key you supplied is not a valid one... The one you supplied was {self.key}")
                raise InvalidKey(
                    "The API key you provided is not a valid one. Please recheck it")
            logging.info(msg=f"Got the image from the API.. Returning it")
            text = session.json()
            return text[0]

    def meme(self) -> str:
        """The dedicated sync method to get a meme from the API

        Raises:
            InvalidKey: The exception raised when a wrong key is provided and the API returns a 401 error code

        Returns:
            str: The meme's image URL
        """
        logging.info(msg=f"Trying to fetch the meme from the API...")
        session = self.session.get(
            url=f'https://api.pgamerx.com/v3/image/{choice(["memes", "dankmemes"])}')
        if session.status_code == 401:
            logging.critical(
                msg=f"The API Key you supplied is not a valid one... The one you supplied was {self.key}")
            raise InvalidKey(
                "The API key you provided is not a valid one. Please recheck it")
        logging.info(msg=f"Got the meme from the API... Returning it")
        text = session.json()
        return text[0]

    def close(self) -> None:
        """Closes the connection gracefully
        """
        logging.info(msg=f"Closing the connection...")
        self.session.close()
