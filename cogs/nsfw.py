# bibliotecas
from utils import helpers
from discord.ext import commands
from discord import app_commands
# from utils.assets import embed
import discord


# realiza a criação da classe cog
class NSFW(commands.Cog):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('NSFW is Ready!!')

    # yande.re

    # rule34

    # gelbooru
    @app_commands.choices(rating=[
        discord.app_commands.Choice(name='Safe', value='safe'),
        discord.app_commands.Choice(name='Questionable', value='questionable'),
        discord.app_commands.Choice(name='Sensitive', value='sensitive'),
        discord.app_commands.Choice(name='Explicit', value='explicit')
    ])
    @app_commands.command(name='gelbooru', description='You tell the tags, and Yume gives you a fresh NSFW image!')
    async def gelbooru(self, interaction: discord.Interaction, *, rating: discord.app_commands.Choice[str], tags: str):

        helpers.lewd = tags.replace(" ", "_")
        helpers.lewd_rate = rating.value

        await interaction.response.send_message(await helpers.gel())

    # safebooru

    # danbooru

    # konachan

    # sankaku

    # lewd ascii

    # e621


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(NSFW(yume))
