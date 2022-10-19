# bibliotecas
from discord.ext import commands
from discord import app_commands
from helpers.assets import embed
import discord
import booru


# realiza a criação da classe cog
class NSFW(commands.Cog):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('NSFW is Ready!!')


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(NSFW(yume))
