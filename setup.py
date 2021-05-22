from setuptools import setup
from rsap.__init__ import __version__

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()


setup(
    name="rsap",
    version=__version__,
    author="Hunter",
    description="A simple wrapper for the Random Stuff API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hunter2807/RSAP",
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Developers",
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
    packages=["rsap"],
    python_requires='>3.6'
)
