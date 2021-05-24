[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
![Maintaner](https://img.shields.io/badge/Maintainer-Hunter-blue)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

![Hunter's GitHub stats](https://github-readme-stats.vercel.app/api?username=Hunter2807&show_icons=true&theme=radical)
<br><br>


#### RSAP.... well it is not a proper acronym, but you can think of it as `Random Stuff API Python`.. It makes use of [PGamerX](https://github.com/pgamerxdev)'s Random Stuff API to provide you features such as jokes, memes, images and also an **AI CHATBOT!!**

### The installation is also very very very simple.
```
pip install rsap
```
### This will install `rsap` **with only** [requests](https://docs.python-requests.org/en/master/) module.. You need to install [aioHTTP](https://docs.aiohttp.org/en/stable/) for AsyncRSAP and [discord.py](https://discordpy.readthedocs.io/en/latest/) for DisRSAP

<br><br>
### The usage is very very very simple.. There are mainly two classes of this module (well there are three but I would consider two because third, you can't say that it is a proper "class" of the module.)

<br><br>
# ASYNC USAGE
To use this module asynchronously, RSAP provides you with the `AsyncRSAP` class of the module... It uses the [aioHTTP](https://docs.aiohttp.org/en/stable/) module to send GET request to the API... A small example for the same is shown below

<br>

```python
from rsap import AsyncRSAP
import asyncio

bot = AsyncRSAP("api_key_here", "other_kwargs_here")

# For AI Response
response = asyncio.run(bot.ai_response("message_here", "unique_id"))
print(response)

# For Jokes
response = asyncio.run(bot.jokes("type"))
print(response)

# For Images
response = asyncio.run(bot.image("type"))
print(response)
```
The code above would use the [aioHTTP](https://docs.aiohttp.org/en/stable/) module..

<br><br>
# SYNC USAGE
To use this module synchronously, RSAP provides you with the `RSAP` class of the module... It uses the [requests](https://docs.python-requests.org/en/master/) module to send the GET request to the API... A small example for the same is shown below
```python
from rsap import RSAP

bot = RSAP("api_key_here", "other_kwargs_here")

# For AI Response
response = bot.ai_response("message", "unique_id") 
print(response)

# For Jokes
response = bot.joke("type")
print(response)

# For Images
response = bot.image("type")
print(response)

# For Closing
bot.close()
```
The code above would use the [requests](https://docs.python-requests.org/en/master/) module..

<br><br>
So last of all that, we have that other so-called "class" known as `DisRSAP` class.. It is just an extension of the RSAP module, which uses the discord.py's [commands.Bot](https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=bot#discord.ext.commands.Bot) module to send the bot responses in a particular Text Channel. It uses the `on_message` trigger to check for messages in the chat channel.. The example for the same is shown below

```python
from rsap import DisRSAP
bot = DisRSAP("api_key_here", text_channel_id_here, command_prefix="!", "other_kwargs_here") #Don't specify any intents because "discord.Intents.all()" is already enabled in the source code.

bot.run("bot_token_here")

```
### So the above code would simply run your bot and the bot would reply to **every single message** sent in that channel!!

<br>
So lemme guess, you are now thinking what are even those `kwargs` mentioned above 😁

So here is a list of kwargs that you can add to your code!!!

👉 api_key ([str](https://docs.python.org/3/library/stdtypes.html#str)): The API key which you can get from https://api-info.pgamerx.com/register
<br><br>
👉 dev_name ([str](https://docs.python.org/3/library/stdtypes.html#str), optional): The name of the developer who coded the chatbot. Used in responses. Defaults to Hunter.
<br><br>
👉 unique_id ([str](https://docs.python.org/3/library/stdtypes.html#str), optional): The Unique ID to create custom sessions for each user. Defaults to a random [uuid.uuid4](https://docs.python.org/3/library/uuid.html#uuid.uuid4) string.
<br><br>
👉 bot_name ([str](https://docs.python.org/3/library/stdtypes.html#str), optional): The name of the chatbot. Used in responses. Defaults to PyChat.
<br><br>
👉 type ([str](https://docs.python.org/3/library/stdtypes.html#str), optional): The type of API to use. Stable is recommended but can also be `unstable`. Defaults to "stable".
<br><br>
👉 language ([str](https://docs.python.org/3/library/stdtypes.html#str), optional): The language to chat with the chatbot in. Defaults to "en".
<br><br>
👉 plan ([str](https://docs.python.org/3/library/stdtypes.html#str), optional): The plan, if any, that you have subscribed to. Defaults to `None`


## List of Types of Jokes 

😆 `any` 

😆 `dev`

😆 `spooky`

😆 `pun`


# List of Types of Images

📸 `aww`

📸 `duck`

📸 `dog`

📸 `cat`

📸 `memes`

📸 `dankmemes`

📸 `holup`

📸 `art`

📸 `harrypottermemes`

📸 `facepalm`

# List of Plans

📝 `pro`

📝 `ultra`

📝 `biz`

📝 `mega`


# CONTACT ME
Need some help for some things?? Join [this discord](https://discord.gg/GWugD56QnE) (is of a friend), and you can always find me here or add me on discord `нυηтєя#8785` :D
<br><br>
## Also, if you want to buy the pro plans of the API, be sure to check [this out](https://form.jotform.com/211240494443449)!
