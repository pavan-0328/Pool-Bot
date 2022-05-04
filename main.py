
import discord 
from dotenv import load_dotenv
from discord.ext import commands
import os

from matplotlib.pyplot import eventplot


load_dotenv()
__TOCKEN__ = os.getenv('tocken')

#------------------------
client = commands.Bot(command_prefix=".")
@client.event
async def on_ready():
    print("Bot Ready")


"""Load the cogs"""
@client.command()
async def load(ctx,extension):
     client.load_extension(f'cogs.{extension}')

"""Unload the cogs"""
@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

"""Load all files in Cogs folder"""
for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(__TOCKEN__)
