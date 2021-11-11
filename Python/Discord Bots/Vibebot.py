# Vibe bot
import discord
import random
import time

from discord.ext import commands

running = False

# Youtube or Spotify links
songs = ['https://open.spotify.com/track/02TQFXm2cV6uwOr2OmlYBC?si=d4e850af047e4c7e',
         'https://open.spotify.com/track/7nnWIPM5hwE3DaUBkvOIpy?si=74f9df6726e14a70',
         'https://open.spotify.com/track/1MvJno497VkQR3RsiJcRVm?si=2873e68992df44ba',
         'https://open.spotify.com/track/6FnNZ53sbMwL71gE5yy0TF?si=ebfd367df52a45fb',
         'https://open.spotify.com/track/3uPfVXcjnpOjyzI3jb3js4?si=ab5459778a2348a6',
         'https://open.spotify.com/track/2ouURa1AIXp3AvkS52Jry5?si=16a4d2c0f7624297',
         'https://open.spotify.com/track/6zeDYmP3ARpURvpK29Q09P?si=ccefcda14fc94a38',
         'https://open.spotify.com/track/5ZsPy9wHH733NlU6c4v2Hi?si=9f059077dcd74635',
         'https://open.spotify.com/track/0whdond5Y89cdcNiXQT9bj?si=f507c47e85414fdf',
         'https://open.spotify.com/track/6zYKkrflJWGAH09GNzhvf9?si=2c219aa839eb4d41',
         'https://open.spotify.com/track/0rPajN9a6S6zIxWm7MOyVh?si=7e00af7ee8e9478a',
         'https://open.spotify.com/track/3cfOd4CMv2snFaKAnMdnvK?si=5c2fe0804faa48c3',
         'https://open.spotify.com/track/4TQeNHx85xcP9YRkvJC6K1?si=19bd66a444714842',
         'https://open.spotify.com/track/0UVIXwqfTjefBbDyY60MWB?si=88d1b158511c4172',
         'https://open.spotify.com/track/50MfV7a1pnOEcf2t9kobxW?si=66870ef088ba44c4',
         'https://open.spotify.com/track/2Wo9IRlgSTeQs76VuuYnpw?si=d2675210f3a1445e',
         'https://open.spotify.com/track/6StgqLwXaIHVWH3xD3xbMN?si=a36fcdcf87e14701',
         "https://open.spotify.com/track/1KSkLYZq9A4ZZ3kuZf5fbY?si=4d559a5ade1646e0",
         "https://open.spotify.com/track/2h3tCbgpPfpTpXuMb6Gd8W?si=70011789bd324bbd",
         "https://open.spotify.com/track/6M14BiCN00nOsba4JaYsHW?si=f72841f85fc64060",
         "https://open.spotify.com/track/6scNR7AS4kiG28hv6Zujqh?si=4eb35432545b4d99",
         "https://open.spotify.com/track/3ga8mjXg89biu4QrkVllTR?si=24d30d119cd9424e",
         "https://open.spotify.com/track/1uIUUtfrWMNcTPlCShgxwM?si=565425ae62bb463b",
         "https://open.spotify.com/track/4nnIqPtoDIwsqB81tilMpz?si=ec2261b930e24ca8",]
# File based?
gifs = ['https://tenor.com/view/sunset-sunrise-cute-pink-bling-gif-16886867',
        'https://tenor.com/view/beach-relaxing-waves-sun-surf-gif-15536525',
        'https://tenor.com/view/aesthetic-gif-19076349',
        'https://tenor.com/view/aesthetic-gif-19082930',
        'https://tenor.com/view/waves-awesome-splash-ocean-gif-11243520',
        'https://tenor.com/view/beach-waves-sunset-gif-4669371',
        'https://tenor.com/view/aesthetic-waves-beach-ocean-gif-16020776',
        'https://tenor.com/view/nature-scenery-beach-sunset-sunrise-gif-16146205',
        'https://tenor.com/view/new-york-manhat-beach-ocean-good-evening-gif-15030474']

client = commands.Bot(command_prefix = '~')

@client.event
async def on_ready():
    print("LOADED!\n")

@client.command()
async def vibe(ctx):
    current = ""
    previous = ""
    running = True
    while(running):
        current = random.choice(songs)
        if(current == previous):
            print('Already played!') # Do!
        else:
            await ctx.send('vibing...')
            await ctx.send(f'-play ' + current) # Find music bot and append prefix
            await ctx.send(random.choice(gifs))
            previous = current
            time.sleep(120)
    # Send gif
    # Play random song from list | Ensure it doesn't play the same

@client.command()
async def stopVibe(ctx):
    await ctx.send('-stop')
    running = False

@client.command()
async def gif(ctx):
    await ctx.send(random.choice(gifs))

client.run('ODMxOTczNDQwOTIyNzE0MTYz.YHdBpQ.l5t-xEkRO4mmub_9GIwFTe8-O44')