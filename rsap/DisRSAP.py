import discord
from .exceptions import InvalidArgument
from discord.ext.commands.bot import Bot
from .AsyncRSAP import AsyncRSAP

__all__ = ["DisRSAP"]


class DisRSAP(Bot):
    def __init__(self, api_key: str,  ai_channel_id: int, *args, **kwargs) -> None:
        """The async class to make the Bot/Client answer to the questions in a specific text channel...

        Args:
            text_channel_id (int): The channel ID to send the responses to.
            api_key (str): The API key which you can get from https://api-info.pgamerx.com/register

        Raises:
            InvalidArgument: Exception when the channel ID you supplied is either wrong, or the Bot/Client can't "see" the channel. Refer to discord.py docs for more information
        """
        self.ai_channel_id = ai_channel_id
        self.dev = kwargs.get("dev_name", "Hunter")
        self.language = kwargs.get("language", "en")
        self.type = kwargs.get("type", "stable")
        self.bot_name = kwargs.get("bot_name", "PyChat")
        super().__init__(intents=discord.Intents.all(), *args, **kwargs)
        self.AI = AsyncRSAP(
            api_key, dev_name=self.dev, type=self.type, language=self.language, bot_name=self.bot_name)

    async def on_ready(self):
        await self.wait_until_ready()
        print(f"{self.bot_name} is ready!!!")
        self.channel = self.get_channel(self.ai_channel_id)
        if self.channel is None:
            raise InvalidArgument(
                "The ID you provided is not a valid text channel ID")

    async def on_message(self, message):
        """The on_message event which is triggered when the message it sent in the AI chat channel...

        Args:
            message (discord.Message): The message to get the content from.
        """
        await self.wait_until_ready()
        if message.author == self.user:
            return
        if message.channel == self.channel:
            await message.channel.send(await self.AI.ai_response(message.content))
        await self.process_commands(message)
