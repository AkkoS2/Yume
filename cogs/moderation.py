# bibliotecas
from discord.ext import commands


# inicializa o cog
class Moderation(commands.Cog):
    def __init__(self, saturn):
        self.saturn = saturn

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation is Ready!')

    # clear
    @commands.has_permissions(manage_messages=True)
    @commands.command(aliases=['deletar'])
    async def clear(self, ctx, amount):

        try:
            amount = int(amount)
            if amount == 0 or amount < 0 or amount >= 101:
                await ctx.send('Não posso aceitar esses valores, tente outra quantidade.', mention_author=False)

            elif amount == 1:
                await ctx.channel.purge(limit=amount + 1)
                await ctx.send(f'Apaguei **{amount}** mensagem!', delete_after=2)

            else:
                await ctx.channel.purge(limit=amount + 1)
                await ctx.send(f'Apaguei **{amount}** mensagens!', delete_after=2)

        except ValueError:
            await ctx.reply('Peço que utilize apenas números inteiros, por favor.', mention_author=False)


# registra a classe no cogs
def setup(saturn):
    saturn.add_cog(Moderation(saturn))
