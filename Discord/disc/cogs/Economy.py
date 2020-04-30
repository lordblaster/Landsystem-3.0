import discord
from discord.ext import commands
import json
import math


class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Collecting tax
    @commands.command()
    @commands.cooldown(1, 7200)
    async def tax(self, ctx):
        user = ctx.message.author
        with open('money.json', 'r') as f:
            users = json.load(f)
        await self.add_money(users, user, 50, ctx)

        with open('money.json', 'w') as f:
            json.dump(users, f)
        discord.ext.commands.CommandOnCooldown(cooldown=30, retry_after=5)

    @tax.error
    async def tax_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            hours = math.floor(error.retry_after / 3600)
            minutes = math.floor((error.retry_after % 3600) / 60)
            seconds = int((error.retry_after % 3600) % 60)

            await ctx.send(f'You have to wait {hours} hours, {minutes} minutes, and {seconds} seconds')

    async def add_money(self, users, user, money_add, ctx):
        if f'{user.id}' in users:
            users[f'{user.name}']['money'] += money_add
            await ctx.send(f"you got {money_add} bucks wise guy")

        else:
            await ctx.send("You don't have an eco mans")

    async def make_items(self, users, user, ctx):
        with open('items.json', 'w') as f:
            users = json.load(f)
            if f'{user.id}' not in users:
                users[f'{user.id}'] = {}
                users[f'{user.name}'] = {}
                users[f'{user.name}']['items'] = []
        with open('items.json', 'w') as f:
            json.dump(users, f)

    async def make_economy(self, users, user, money, ctx):
        if f'{user.id}' not in users:
            users[f'{user.id}'] = {}
            users[f'{user.name}'] = {}
            users[f'{user.name}']['money'] = money
            await ctx.send("You're economy has been made")
        else:
            await ctx.send("You already have an eco my person")

    # Start an economy
    @commands.command(aliases=["makeeconomy"])
    async def makeeco(self, ctx):
        user = ctx.message.author
        print('work')
        with open('money.json', 'r') as f:
            users = json.load(f)


        await self.make_economy(users, user, 0, ctx)

        with open('money.json', 'w') as f:
            json.dump(users, f)

        await self.make_items(users, user, ctx)


    # Checks how much money you have
    @commands.command(aliases=['eco'])
    async def economy(self, ctx):
        user = ctx.message.author

        with open('money.json', 'r') as f:
            users = json.load(f)
            if f'{user.id}' in users:
                money = (users[f'{user.name}']['money'])
                await ctx.send(f"You've got {money} washingtons smart guy")
            else:
                await ctx.send("You've got 0 big ones because you don't have a eco my g")

        with open('money.json', 'w') as f:
            json.dump(users, f)

    # Shop
    @commands.command(name='shop')
    async def shop(self, ctx):
        embed = discord.Embed(
            title="The shops",
            description="You buy stuff... cause it's a shop",
            colour=discord.Color.red())

        embed.set_footer(text="page 1 of (I don't know)")
        print('work')
        embed.add_field(name="mechanized inf: _coins --Type", value='description 1')
        embed.add_field(name="motorized inf: _coins --Type", value='description 2')
        embed.add_field(name="Item 3: _coins --Type", value='description 3')
        embed.add_field(name="Item 4: _coins --Type", value='description 4')
        embed.add_field(name="Item 5: _coins --Type", value='description 5')
        embed.add_field(name="Item 6: _coins --Type", value='description 6')

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Economy(client))
