import discord
from random import randint
from time import sleep
from discord import ext
from discord.ext import commands
import asyncio
import sys
import requests
import aiohttp
import io

client = discord.Client()
token = "Ur token here"

@client.event
async def on_ready():
    print ("Logged in")
    print ("--------------------------")
    

@client.event
async def on_message(message):
    if (message.content.lower() == "pls use bomb") or (message.content.lower() == "pls use coinbomb") or (message.content.lower() == "pls use coin"):
        print ("Found a coin bomb from "+ str(message.author))
        time = "0." + str(randint(500,3500))
        sleep(float(time))
        await message.channel.send("i want money")

client.run(token, bot=False)
