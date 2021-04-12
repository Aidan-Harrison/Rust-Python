import discord
import threading
import time

from discord.ext import commands

running = False
client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
    print('LOADED!\n')

@client.command()
async def hewwo(ctx, amount : float):
    running = True
    while(running):
        await ctx.send('@everyone hewwo!!!!')
        time.sleep(amount * 60)
    #threading.Timer(amount * 60, hewwo(ctx, amount)).start()

@client.command()
async def stop(ctx):
    await ctx.send('Stopped :(')
    running = False

client.run('ODMwODE0MTA1MzM3ODU2MDUw.YHMJ7g.CwtkUeIXOADeTBohJoxvY_-5v4o')