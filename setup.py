from setuptools import setup
from RASPI.__init__ import __version__

with open("README.md", "r") as file:
    long_description = file.read()


setup(
    name="RASPI",
    version=__version__,
    author="Hunter",
    description="A simple wrapper for the Random Stuff API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hunter2807/RASPI",
    keywords=[
    "chatbot",
    "ai",
    "api",
    "images",
    "memes",
    "prsaw",
    "random stuff",
    "jokes",
    "memes",
    "bot",
    "discord.py"
    ],
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Everyone",
        "License :: OSI Approved :: GNU License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
        "discord.py",
        "aiohttp",
        "requests"
    ],
    python_requires='>3.6'
)
