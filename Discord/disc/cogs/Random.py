import discord
from discord.ext import commands


class Random(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()

    async def bip(self, ctx):
        await ctx.send(f'bop {round(self.client.latency * 1000)} ms')
        # await on_command_error(ctx, error)

    @commands.command()
    async def displayembed(self, ctx):
        embed = discord.Embed(
            title="this is a title",
            description="An interesting description",
            colour=discord.Colour.blue()
        )
        embed.set_footer(text="This is a footer.")
        embed.set_image(url="https://mma.prnewswire.com/media/490474/KFC_Zinger_5_Dollar_Fill_Up.jpg")
        embed.set_thumbnail(url="https://i.ytimg.com/vi/bwvd6zCCPdY/maxresdefault.jpg")
        embed.set_author(name='Author Name', icon_url="https://i.ytimg.com/vi/5zj0qmDlNGo/hqdefault.jpg")
        embed.add_field(name='Field name', value='Field value', inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

        embed.set_author(name=f'User Info - {member}')
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

        embed.add_field(name='ID:', value=member.id)
        embed.add_field(name='Guild name:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
        embed.add_field(name='Joined at:', value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))

        embed.add_field(name=f'Roles ({len(roles)})', value=" ".join([role.mention for role in roles]))
        embed.add_field(name='Top Role:', value=member.top_role.mention)

        embed.add_field(name='Bot?', value=member.bot)
        embed.add_field(name='Gay?:', value="yes")

        await ctx.send(embed=embed)

    @commands.command()
    async def echo(self, ctx, *args):
        output = ''
        for word in args:
            output += word
            output += ' '
        await ctx.send(output)


def setup(client):
    client.add_cog(Random(client))
