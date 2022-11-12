# bibliotecas
from helpers.assets import embed
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

        searchers.sub_reddit = subreddit
        result = await searchers.reddit_search()

        if result[2] is True and result[1] is False and not interaction.channel.is_nsfw():
            await interaction.response.send_message("Looks like the post I got is tagged as NSFW and the channel isn't", ephemeral=True)

        elif result[2] is True and result[1] is False and interaction.channel.is_nsfw():
            url = 'https://reddit.com' + result[4]
            await interaction.response.send_message(result[3] + '\n' + url)

        if result[2] is True and result[1] is True:
            url = 'https://reddit.com' + result[4]
            await interaction.response.send_message(result[3] + '\n' + url)

        if result[1] is False and not interaction.channel.is_nsfw():
            await interaction.response.send_message("Looks like the post I got is tagged as NSFW and the channel isn't", ephemeral=True)

        if result[1] is True:
            embed.set_author(name=result[3], url='https://reddit.com' + result[4])
            embed.set_footer(text=result[5] + f'on r/{subreddit}')
            embed.set_image(url=str(result[0]))
            await interaction.response.send_message(embed=embed)

        elif result[1] is False and interaction.channel.is_nsfw():
            embed.set_author(name=result[3], url='https://reddit.com' + result[4])
            embed.set_footer(text=result[5] + f'on r/{subreddit}')
            embed.set_image(url=str(result[0]))
            await interaction.response.send_message(embed=embed)


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Image(yume))
