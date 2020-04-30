import discord
import os
from discord.ext import commands
import json


class Levels(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Leveling system

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('users.json', 'r') as f:
            users = json.load(f)

        await self.update_data(users, member)

        with open('users.json', 'w') as f:
            json.dump(users, f)

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            with open('users.json', 'r') as f:
                users = json.load(f)

            await self.update_data(users, message.author)
            await self.add_experience(users, message.author, 5)
            await self.level_up(users, message.author, message)

            with open('users.json', 'w') as f:
                json.dump(users, f)
        channel = message.channel
        await self.client.process_commands(message)

    async def update_data(self, users, user):
        if f'{user.id}' not in users:
            users[f'{user.id}'] = {}
            users[f'{user.name}'] = {}
            users[f'{user.id}']['experience'] = 0
            users[f'{user.id}']['level'] = 1

    async def add_experience(self, users, user, exp):
        users[f'{user.id}']['experience'] += exp

    async def level_up(self, users, user, message):
        experience = users[f'{user.id}']['experience']
        lvl_start = users[f'{user.id}']['level']
        lvl_end = int(experience ** (1 / 4))
        if lvl_start < lvl_end:
            await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
            users[f'{user.id}']['level'] = lvl_end
            print(f'{user} has leveled up to {lvl_end}')

    @commands.Cog.listener()
    async def level(self, ctx):
        with open('users.json', 'r') as f:
            users = json.load(f)
        level = users[f'{ctx.author.id}']['level']
        await ctx.send(f'You are level {level}')
        with open('users.json', 'w') as f:
            json.dump(users, f)


def setup(client):
    client.add_cog(Levels(client))
