import os
import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is online!')

@client.command()
async def ping(ctx):
    await ctx.send(f'ping : ``{round(client.latency * 1000)}ms``')
async def hi(ctx):
    await ctx.send('Hello!')

client.run('MTAzNjU2NTI2NTY4Njc0NTExOQ.G0m2Bg.LO0w_j0agIlCgli2y93McsWNax4KFFD3mnSmLc')