# Bibliotecas utilizadas neste arquivo
from utils.embeds import GenericEmbed
from utils import buttons, helpers
from discord.ext import commands
from discord import app_commands
import discord


# Realiza a definição da classe cog
class Image(commands.Cog):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # Avisa quando a classe cog iniciar
    @commands.Cog.listener()
    async def on_ready(self):
        print('Image is Ready!')

    # Reddit
    @app_commands.command(name='reddit', description='Gets a image from the chosen subreddit')
    async def reddit(self, interaction: discord.Interaction, *, subreddit: str):

        helpers.sub_reddit = subreddit
        result = await helpers.reddit_search()
        url = 'https://reddit.com' + result[4]

        embed = GenericEmbed.embed
        embed.set_author(name=result[3], url='https://reddit.com' + result[4])
        embed.set_footer(text=result[5] + f' on r/{subreddit}')
        embed.set_image(url=str(result[0]))

        nsfw_content = "Looks like the post I got is tagged as NSFW, you can try again or you can use a NSFW channel."

        if result[2] is True and result[1] is False and not interaction.channel.is_nsfw():
            await interaction.response.send_message(nsfw_content, ephemeral=True)

        elif result[2] is True and result[1] is False and interaction.channel.is_nsfw():
            await interaction.response.send_message(result[3] + '\n' + url)

        if result[2] is True and result[1] is True:
            await interaction.response.send_message(result[3] + '\n' + url)

        if result[1] is False and not interaction.channel.is_nsfw():
            await interaction.response.send_message(nsfw_content, ephemeral=True)

        if result[1] is True:
            await interaction.response.send_message(embed=embed)

        elif result[1] is False and interaction.channel.is_nsfw():
            await interaction.response.send_message(embed=embed)


# Realiza o registro da classe nos cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Image(yume))
