# bibliotecas
from discord.ext import commands
from discord import app_commands
from helpers import searchers
import discord


# realiza a criação da classe cog
class Image(commands.Cog):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Image is Ready!!')

    # reddit
    @app_commands.command(name='reddit', description='Gets a image from the chosen subreddit')
    async def reddit(self, interaction: discord.Interaction, *, subreddit: str):

        searchers.sub_reddit = str(subreddit)
        await interaction.response.send_message(await searchers.reddit_search(), ephemeral=True)


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Image(yume))
