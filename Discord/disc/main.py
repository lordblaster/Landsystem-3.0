import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import os


client = commands.Bot(command_prefix='?')
client.remove_command('help')
status = ['Conquest of Siberia', 'Signing peace treaty with France', 'blitzing the Ardennes', 'doing homework',
          'coming up with more of these things', 'your mother', 'contemplating if I want to continue with this bot',
          'probably math hw', 'not doing the ela reading', 'bobert']




# Help panel thing
@client.command(aliases=['help'])
async def _help(ctx):
    helps = 'https://docs.google.com/document/d/1ejEcjtisv64PeU3XKkCKePSB5QdTAp-8AgSvV33FSb8/edit?usp=sharing'
    await ctx.send(f'Here\'s a link to a doc with all the commands:\n{helps}')

    await ctx.author.send('bob')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Your mother'))
    print("bot is ready")


async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed():
        current_status = next(msgs)
        await client.change_presence(activity=discord.Game(name=current_status))
        await asyncio.sleep(5)


@client.command()
async def reload(ctx, cog):
    try:
        client.unload_extension(f'cogs.{cog}')
        client.load_extension(f'cogs.{cog}')
        await ctx.send(f'{cog} got reloaded')
    except Exception as e:
        await ctx.send(f'{cog} could not be reload')
        print(f'{cog} could not be reloaded:')
        raise e


@client.command()
async def work(ctx):
    await ctx.send("this is working")


for cog in os.listdir(".\\cogs"):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            client.load_extension(cog)
            print("1")
        except Exception as e:
            print(f'{cog} can not be loaded')
            raise e

client.loop.create_task(change_status())
client.run('NjgyMDEwMjc2NTk3NDY1MTcy.XqsMYg.9tn4mr2mE1Y0sjjEebgIj9e9rGU')
