# Thanos bot ---
import discord
import random
import math

from discord.ext import commands # Get commands

intents = discord.Intents().all()
client = commands.Bot(command_prefix = '>', intents=intents) # Create client variable

@client.event # Func declaration
async def on_ready():
    print("LOADED!\n")

# Join and leave
    #@client.event
    #async def on_member_join(member):
        #print(f'{member} has joined a server')

    #@client.event
    #async def on_member_remove(member):
        #print(f'{member} has fallen to Thanos')
    
@client.command()
async def printMembers(ctx):
    print(ctx.guild.members)

@client.command()
async def getMember(ctx):
    await ctx.send(random.choice(ctx.guild.members))

@client.command() # Target an individual to kick
async def targetSnap(ctx, member : discord.Member):
    print(member)
    await ctx.send('Balanced the universe, a little...')
    await member.kick()

@client.command() # Randomly kicks half the server
async def snap(ctx): #member : discord.Member): # Context is automatically passed in, parameter needed
    await ctx.send('Balancing universe....')
    #print(f'{round(client.latency * 1000)} |ms') # Convert to milliseconds
    total = ctx.guild.member_count / 2
    total = int(math.floor(total))
    print(total)
    owner = ctx.guild.owner
    for member in range(total):
        member = random.choice(ctx.guild.members)
        if member.id == 829742951789494273: continue # Bot
        if member == owner: continue
        print(member)
        await member.kick()
    await ctx.send(f'{total} | members have been eradicated...')

@client.command(aliases=['8ball']) # Any string in list can call below function
async def _8ball(ctx, *, question = "Generic question?"): # Underscore allows for numerical names | '*' allows for multiple arguments
    responses = ['I am thanos',
                 'Leave me alone', ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#@client.command() # Need to give perm
#async def clear(ctx, amount = 5):
    #await ctx.channel.purge(limit = amount + 1)

@client.command()
async def tHelp(ctx):
    await ctx.send('|=====HELP=====|\n>snap : Kicks half a servers userbase at random\n>targetSnap : Kicks a specific member')

client.run('ODI5NzQyOTUxNzg5NDk0Mjcz.YG8kVw._fB6k9mf9Yj77o3AjIEoB58EzLE')