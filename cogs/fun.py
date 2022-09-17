# bibliotecas
from helpers.phrases import fortune
from discord.ext import commands
import discord
import asyncio
import random


# inicializa o cog
class Fun(commands.Cog):
    def __init__(self, saturn):
        self.saturn = saturn

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun is Ready!')

    # FortuneTeller
    @commands.command(aliases=['vidente'])
    async def fortune(self, ctx, *, question):
        await ctx.reply(f'{random.choice(fortune())}', mention_author=False)

    # Coin Flip
    @commands.command(aliases=['caracoroa'])
    async def coin(self, ctx):

        coin01 = discord.File('media/Coin01.gif', filename='Coin01.gif')
        coin02 = discord.File('media/Coin02.gif', filename='Coin02.gif')
        coin03 = discord.File('media/Coin03.gif', filename='Coin03.gif')
        coin04 = discord.File('media/Coin04.gif', filename='Coin04.gif')

        heads_tails = discord.Embed(color=discord.Colour.random())
        heads_tails.set_author(name='Heads or Tails?')

        value = random.randrange(10)
        if value == 5:
            coin = ['half']
            heads_tails.set_image(url='attachment://Coin04.gif')
        else:
            coin = ['heads', 'tails']
            heads_tails.set_image(url=f'attachment://')

        coin_choice = random.choice(coin)
        await ctx.send(f'Heads or Tails?')

        try:

            message = await self.saturn.wait_for('message', check=lambda m: m.author == ctx.author and
                                                                            m.channel == ctx.channel, timeout=15.0)
        except asyncio.TimeoutError:
            await ctx.send('Tired of waiting, sorry :p', delete_after=5)

        else:
            if message.content.lower() == coin_choice:
                await ctx.reply(f'The result is... **{coin_choice}**. Congrats!', mention_author=False)

            elif message.content.lower() != coin_choice:
                await ctx.reply(f'Hmmm... it appears that you just missed, the result was **{coin_choice}**!',
                                mention_author=False)

        await ctx.send(embed=heads_tails)


# registra a classe no cogs
def setup(saturn):
    saturn.add_cog(Fun(saturn))
