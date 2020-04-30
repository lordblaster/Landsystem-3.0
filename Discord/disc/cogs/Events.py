import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        channel = reaction.message.channel
        await channel.send('{} has added {} to the message: {}'.format(user.name, reaction.emoji,
                                                                       reaction.message.content))

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        channel = reaction.message.channel
        await channel.send('{} has removed {} to the message: {}'.format(user.name, reaction.emoji,
                                                                         reaction.message.content))

    @commands.Cog.listener()
    async def on_message(self, ctx):
        pass

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Hey what are you trying to pull? You don't have permission to do that")
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("That's not a command bruv(check spelling)")
        # if isinstance(error, commands.MissingRequiredArgument):
        # await ctx.send(f'You\'re missing an input dude')
        if isinstance(error, commands.BadArgument):
            await ctx.send(f'You entered a bad argument(ex. you said 5 when I asked you for a color)')
        if isinstance(error, TimeoutError):
            await ctx.send("You ran out of time bud")


def setup(client):
    client.add_cog(Events(client))
