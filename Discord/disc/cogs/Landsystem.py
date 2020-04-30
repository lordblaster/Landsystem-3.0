import discord
from discord.ext import commands
import json


class Landsystem(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Join
    @commands.command(aliases=['join'])
    async def join_a_country(self, ctx, message):
        user = ctx.message.author

        if message in countries:
            with open('land.json', 'r') as f:
                users = json.load(f)

            await self.joinc(users, user, message, ctx)

            with open('land.json', 'w') as f:
                json.dump(users, f)

        else:
            await ctx.send("please pick a valid country(capitalization counts)")

    async def joinc(self, users, user, message, ctx):
        if f'{user.id}' not in users:

            await ctx.send(f'{ctx.message.author} has joined {message}')
            users[f'{user.id}'] = {}
            users[f'{user.name}'] = {}
            users[f'{user.name}']['country'] = message
            users[f'{user.name}']['territories'] = country_territory[message]


        else:
            with open('land.json') as f:
                data = json.load(f)
                coun = data[f'{user.name}']['country']
            await ctx.send(f'You\'ve already joined {coun} bud.')
            with open('land.json', 'w') as f:
                json.dump(users, f)

    # adds an item
    async def add_item(self, users, user, ctx, item):
        if f'{user.id}' in users:
            users[f'{user.name}']['items'] = item
            await ctx.send(f'{item} has been bought')
        else:
            await ctx.send('You don\'t have an eco man')

    # List out countries and stuff
    @commands.command(aliases=['list'])
    async def _list(self, ctx):
        con = ''
        for i in country_territory:
            con += f'{i} - {country_territory[i]}\n'
        await ctx.send(con)

    # Shows Map
    @commands.command(aliases=['map'])
    async def _map(self, ctx):
        my_files = [
            discord.File('mapwithregions2.png')
        ]
        await ctx.send('The Map:', files=my_files)

    # Shows your territories
    @commands.command(aliases=['info', 'countryinfo'])
    async def country_info(self, ctx):
        user = ctx.message.author
        with open('land.json', 'r') as f:
            users = json.load(f)
            if f'{user.id}' in users:
                territories = (users[user.name]['territories'])
                country = (users[user.name]['country'])
                await ctx.send(f'Your country is {country}\nYou own: {territories}')

    # Buying items
    @commands.command()
    async def buy(self, message, ctx):
        if message in items:
            user = ctx.message.author
            with open('land.json', 'r') as f:
                users = json.load(f)

            await self.add_item(users, user, ctx, message)

            with open('land.json', 'w') as f:
                json.dump(users, f)


# Info
countries = ["Laiwania", "Hadmania", "Kasia", "Kagih", "Madro", "Nairk", "Panvia", "Sartnia", "Pesnarom", "Potland",
             "Bokia", "Fisland", "Xinjiang", "Gaseong", "Seonguk", "Eoyanguk"]

country_territory = {"Laiwania": ["l1", "l2", "l3", "l4", "l5", "l6", "l7", "l8c", "l9"],
                     "Hadmania": ["h1", "h2c", "h3", "h4", "h5", "h6", "h7", "h8"],
                     "Kasia": ["k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "k10", "k11c", "k12", "k13"],
                     "Kagih": ["kk1", "kk2", "kk3", "kk4", "kk5", "kk6", "kk7", "kk8", "kk9c"],
                     "Madro": ["m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8", "m9c"],
                     "Nairk": ["n1", "n2c", "n3", "n4", "n5", "n6", "n7", "n8", "n9"],
                     "Panvia": ["p1", "p2", "p3", "p4", "p5", "p6c", "p7", "p8", "p9", "p10", "p11"],
                     "Sartnia": ["s1", "s2", "s3", "s4", "s5c", "s6", "s7", "s8", "s9"],
                     "Pesnarom": ["ppp1", "ppp2", "ppp3", "ppp4", "ppp5", "ppp6", "ppp7c", "ppp8", "ppp9", "ppp10"],
                     "Potland": ["pp1", "pp2", "pp3", "pp4", "pp5", "pp6c", "pp7", "pp8", "pp9", "pp10"],
                     "Bokia": ["b1", "b2", "b3", "b4", "b5c", "b6", "b7", "b8", "b9", "b10"],
                     "Fisland": ["f1c", "f2", "f3", "f4", "f5", "f6", "f7"],
                     "Xinjiang": ["x1", "x2", "x3c", "x4", "x5", "x6", "x7", "x8"],
                     "Gaseong": ["g1", "g2", "g3c"],
                     "Seonguk": ["ss1", "ss2c", "ss3", "ss4", "ss5", "ss6", "ss7", "ss8"],
                     "Eoyanguk": ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10c"]}
items = ['motorized inf', 'mechanized inf', 'battleship']
item_type = {
    'motorized inf': 'inf',
    'mechanized inf': 'inf',
    'battleship': 'naval'
}


def setup(client):
    client.add_cog(Landsystem(client))
