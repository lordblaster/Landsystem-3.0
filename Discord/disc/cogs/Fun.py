import discord
import random
from discord.ext import commands
import asyncio
import time


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Fun:
    # Qur'an
    @commands.command(aliases=['quran'])
    async def quote(self, ctx):
        quotes = ['Call upon me, I will respond to you...',
                  'And Allah would not punish them while they seek forgiveness',
                  'So remember me; I will remember you',
                  'And He has made me blessed wherever I am',
                  'He knows what is within the heavens and earth and knows what you conceal and what you declare. And '
                  'Allah (SWT) is Knowing of that within the breasts',
                  'Indeed, those who have believed and done righteous deeds will have gardens beneath which rivers flow '
                  'that is a great attainment',
                  'If you are grateful, I will surely increase you [in favor]',
                  'Respect and honour all human beings irrespective of their religion, colour, race, sex, language, '
                  'status, property, birth, profession/job and so on',
                  'Do not shout. Speak politely keeping your voice low',
                  'Do not be a bragging boaster',
                  'Speak in a civilised manner in a language that is recognised by the society and is commonly used',
                  'Say with your mouth what is in your heart',
                  'Keep yourself clean, pure',
                  'Do not squander your wealth senselessly',
                  'Eat and drink [what is lawful] in moderation'
                  'Seek your provision only by fair endeavour',
                  'The grace of God is infinite',
                  'Every soul gets what it deserves on none other than itself',
                  'Nothing on earth or in heaven is hidden from God',
                  'He [God] neither begets, nor was he begotten',
                  'Distress goes to all slanderers and libelers',
                  'In the name of Allah, Most Gracious, Most Merciful. Praise be to Allah, the Cherisher and Sustainer of '
                  'the worlds Most Gracious, Most Merciful Master of the Day of Judgment.Thee do we worship, '
                  'and Thine aid we seek. Show us the straight way,The way of those on whom Thou hast bestowed Thy Grace, '
                  'those whose (portion) is not wrath, and who go not astray',
                  'It is the most hateful sight to God when you say what you do not practice',
                  'God is aware of all you do',
                  'Avoid excessive suspicion'

                  ]
        await ctx.send(f"Allah says: \n {random.choice(quotes)} ")

    # nuke
    @commands.command()
    async def nuke(self, ctx, *, reason="nothing"):
        author = ctx.message.author
        await ctx.send(f'In the name of allah, {author} has nuked {reason}')

    # 8ball code
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['As I see it, yes.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Don’t count on it.',
                     'It is certain.',
                     'It is decidedly so.',
                     'Most likely.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Outlook good.',
                     'Reply hazy, try again.',
                     'Signs point to yes.',
                     'Very doubtful.',
                     'Without a doubt.',
                     'Yes.',
                     'Yes – definitely.',
                     'You may rely on it.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    #death
    @commands.command()
    async def death(self, ctx):

        await ctx.send('Enter an age(0-100)')

        def check(m):
            return 100 >= int(m.content) >= 0 and m.channel == ctx.channel

        try:
            age = await self.client.wait_for('message', timeout=10.0, check=check)

        except asyncio.TimeoutError:
            await ctx.send("You gonna answer me or sit there touching yourself?")
        else:
            if int(age.content) > 80:
                await ctx.send("You're above average life expectency, you beat the odds, congrats")
            else:
                times = 2524608000 - (int(age.content) * 31557600)
                await ctx.send(f'You\'ve got {times} seconds left to live(rough estimate)')


def setup(client):
    client.add_cog(Fun(client))
