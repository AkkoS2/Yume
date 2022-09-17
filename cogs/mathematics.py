# bibliotecas
from discord.ext import commands
import math


# inicializa o cog
class Mathematics(commands.Cog):
    def __init__(self, saturn):
        self.saturn = saturn

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Math is Ready!')

    # adição
    @commands.command(aliases=['soma'])
    async def add(self, ctx, value=None):

        value = value.split(' ')
        value = [value]
        print(value)
        try:
            result = sum(value)
            await ctx.reply(f'O resultado da adição é {result}!', mention_author=False)

        except ValueError:
            await ctx.reply('Eu gostaria que utilizasse apenas números, por favor.')

    @add.error
    async def error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send('ue')
        else:
            raise error


# registra a classe no cogs
def setup(saturn):
    saturn.add_cog(Mathematics(saturn))
